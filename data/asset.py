from utils.strings import camel_to_snake_case
import inspect
from data.asset_validation_state import AssetValidationState

# Metaclass that registers NBTAsset subtypes
class AssetMeta(type):
    def __new__(cls, name, bases, dct):
        subclass = super().__new__(cls, name, bases, dct)
        
        if name == 'Asset':
            subclass.types.append(subclass)
            subclass.assets_by_type_name['asset'] = []
        else:
            register_asset_subclass(subclass)            

        return subclass

BASE_TYPES_CLASS_NAMES = ('Asset', 'NBTAsset')
BASE_TYPE_NAMES = ('asset', 'nbtasset')

def register_asset_subclass(cls):
    Asset.types.append(cls)
    
    # Type name must be distinct from parent
    if cls.type_name == cls.__bases__[0].type_name:
        cls.type_name = camel_to_snake_case(cls.__name__)

    cls.parent_types = []
    for type in inspect.getmro(cls)[1:-1]:
        if type.type_name not in BASE_TYPE_NAMES:
            cls.parent_types.append(type)
            

    Asset.assets_by_type_name[cls.type_name] = []

# Error used for loading in assets
class AssetError(ValueError):
    def __init__(self, message : str) -> None:
        self.message =  message

# Decorator that allows for defaults to be set for certain values before validate is called
# Try to make them pass-by-value types. I'll copy lists and dicts, but you'll have problems otherwise.
def asset_defaults(**kwargs):
    # Inner function adds defaults
    def register_defaults(cls):
        Asset.defaults[cls.type_name] = kwargs
        return cls

    return register_defaults

# Base Class for all assets loaded from json files
class Asset(metaclass=AssetMeta):
    type_name = 'asset'

    # Used to store loaded assets by type
    assets_by_type_name : dict[str, list] = {}

    # Defaults by type
    defaults : dict[str, dict[str, any]] = {}

    # Tracks all types of assets
    types : list[type] = []

    # Tracks all parent types of this asset, not including Asset or NBTAsset
    parent_types : list[type] = []

    # Object Fields
    name : str
    type : str

    # Called after fields are loaded in 
    # This function ensures all required fields are there
    def validate(self) -> AssetValidationState:
        state = AssetValidationState()
        annotated_fields = set()

        for tp in inspect.getmro(type(self))[:-1]:
            for field_name in tp.__annotations__:
                annotated_fields.add(field_name)
                if not hasattr(self, field_name):
                    field_type = tp.__annotations__[field_name].__name__
                    state.missing_args.append((field_name, field_type))
                    
        for field in self.__dict__:
            if field not in annotated_fields:
                state.surplus_args.append((field, type(field).__name__))
        
        return state

    def set_defaults(self) -> None:
        for tp in inspect.getmro(type(self))[:-1]:
            if tp.type_name not in Asset.defaults:
                continue

            for field_name, field_value in Asset.defaults[tp.type_name].items():
                value = field_value

                if isinstance(value, list) or isinstance(value, dict):
                    value = value.copy()

                if not hasattr(self, field_name):
                    setattr(self, field_name, value)
    
    def on_construct(self) -> None: # Called after fields are validated
        self.origin = tuple(self.origin) # convert list to tuple

    # Adds object to global pool of objects
    def add_to_pool(self) -> None:
        for tp in (type(self), *self.parent_types):
            Asset.assets_by_type_name[tp.type_name].append(self)

    # -------------
    # CLASS METHODS

    @classmethod
    def new(cls, name, type, filepath, origin):
        obj = Asset()
        obj.name = name
        obj.type = type
        obj.filepath = filepath
        obj.origin = origin
        return obj

    @classmethod
    def find_type(cls, name):
        for tp in Asset.types:
            if tp.type_name == name:
                return tp

    # Returns all instances of a type
    @classmethod
    def all(cls):
        return Asset.assets_by_type_name[cls.type_name]

    # Returns asset with specified name
    @classmethod
    def find(cls, name):
        for asset in cls.all():
            if asset.name == name:
                return asset

    # This is used to create an asset without raising an exception on failure
    # IMPORTANT: This can return None when the asset created is invalid. It will NOT throw an error.
    @classmethod
    def construct_unsafe(cls, add_to_pool = True, **kwargs) -> tuple[any, AssetValidationState]:
        obj = cls()

        for key, val in kwargs.items():
            obj.__setattr__(key, val)

        obj.set_defaults()

        state = obj.validate()

        if state.is_invalid():
            return None, state

        obj.on_construct()

        if add_to_pool:
            obj.add_to_pool()

        return obj, state

    # Call this to properly create an asset
    @classmethod
    def construct(cls, add_to_pool = True, **kwargs) -> any:
        asset, state = cls.construct_unsafe(add_to_pool, **kwargs)

        if state.is_invalid():
            raise AssetError(f'Asset is missing the following arguments: {[state.missing_args]}')
        
        return asset
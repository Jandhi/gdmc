from core.structures.nbt.nbt_asset import NBTAsset
from gdpc.vector_tools import ivec3

class AssetStructure(NBTAsset):
    size: ivec3 #size of the structure to be used when placing
    facing: str = None #east/west/south/north
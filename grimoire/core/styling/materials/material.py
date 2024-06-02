import abc
from dataclasses import dataclass
from typing import Callable

from gdpc import Editor, Block
from glm import ivec3

from grimoire.core.assets.asset import Asset, asset_defaults, default_subtype
from grimoire.core.noise.hash import recursive_hash, hash_string
from grimoire.core.noise.seed import Seed
from grimoire.core.styling.blockform import BlockForm
from grimoire.core.styling.materials.dithering import (
    DitheringPattern,
)
from grimoire.core.utils.strings import trim_minecraft_namespace


@dataclass
class MaterialParameters:
    position: ivec3

    # 0 for darkest, 1 for lightest
    shade: float

    # 0 for no age, 1 for oldest
    age: float

    # 0 for no moisture, 1 for most moisture
    moisture: float

    # dithering pattern, optional
    dithering_pattern: DitheringPattern | None


@dataclass
class MaterialParameterFunction:
    shade_func: Callable[[ivec3], float] | None
    age_func: Callable[[ivec3], float] | None
    moisture_func: Callable[[ivec3], float] | None
    dithering_pattern: DitheringPattern | None

    def eval(self, position: ivec3) -> MaterialParameters:
        return MaterialParameters(
            position=position,
            shade=0.5 if self.shade_func is None else self.shade_func(position),
            age=0 if self.age_func is None else self.age_func(position),
            moisture=(
                0 if self.moisture_func is None else self.moisture_func(position)
            ),
            dithering_pattern=None,
        )


class Material(Asset):
    dithering_pattern: DitheringPattern

    def place_block(
        self,
        editor: Editor,
        form: BlockForm,
        states: dict[str, str] | None,
        data: str | None,
        parameters: MaterialParameters,
    ):
        pass

    def has_block(self, block: Block) -> bool:
        pass

    def has_form(self, form: BlockForm) -> bool:
        pass

    def get_id(self, form: BlockForm, parameters: MaterialParameters) -> str | None:
        pass


CALCULATE_RANGE = -1


@default_subtype(Material)
@asset_defaults(
    shade_range=CALCULATE_RANGE,
    age_range=CALCULATE_RANGE,
    moisture_range=CALCULATE_RANGE,
    lighter=None,
    darker=None,
    older=None,
    younger=None,
    more_moist=None,
    less_moist=None,
    dithering_pattern=None,
)
class BasicMaterial(Material):
    # Range
    # this refers to the amount of gradation that exists for a parameter
    # CALCULATE_RANGE means that the range will be determined at creation
    # for shade, this is determined by the maximum depth of lighter or darker
    # for age and moisture, this is determined by the depth of older and more_moist
    shade_range: int
    age_range: int
    moisture_range: int

    # CONNECTIONS
    # Shade
    lighter: Material | None
    darker: Material | None
    # Age
    older: Material | None
    younger: Material | None
    # Moisture:
    more_moist: Material | None
    less_moist: Material | None

    # BLOCK TYPES
    blocks: dict[BlockForm, str]

    def on_link(self) -> None:
        # shade
        lighter_amt = 0
        root = self
        while root.lighter is not None:
            lighter_amt += 1
            root = root.lighter

            while isinstance(root, CompositeMaterial):
                root = list(root.submaterials.keys())[0]

        darker_amt = 0
        root = self
        while root.darker is not None:
            darker_amt += 1
            root = root.darker

            while isinstance(root, CompositeMaterial):
                root = list(root.submaterials.keys())[0]

        self.shade_range = 1 + 2 * min(lighter_amt, darker_amt)

        # age
        age_range = 1
        root = self
        while root.older is not None:
            age_range += 1
            root = root.older

            while isinstance(root, CompositeMaterial):
                root = list(root.submaterials.keys())[0]
        self.age_range = age_range

        # moisture
        moisture_range = 1
        root = self
        while root.more_moist is not None:
            moisture_range += 1
            root = root.more_moist

            while isinstance(root, CompositeMaterial):
                root = list(root.submaterials.keys())[0]
        self.moisture_range = moisture_range

    def place_block(
        self,
        editor: Editor,
        form: BlockForm,
        states: dict[str, str],
        data: str | None,
        parameters: MaterialParameters,
    ):
        block_id = self.get_id(form, parameters)
        editor.placeBlock(
            parameters.position,
            Block(
                id=block_id,
                states=states,
                data=data,
            ),
        )

    def traverse(
        self,
        params: MaterialParameters,
    ) -> "BasicMaterial":
        dithering_pattern = (
            params.dithering_pattern
            if params.dithering_pattern is not None
            else self.dithering_pattern
        )

        shade_index = self.calculate_index(
            params.shade,
            self.shade_range,
            params.position,
            dithering_pattern,
        )
        material = self

        shade_diff = shade_index - int(self.shade_range / 2)
        if shade_diff > 0:
            # lighter
            for _ in range(shade_diff):
                if material.lighter is None:
                    break
                material = material.lighter
        elif shade_diff < 0:
            # darker
            for _ in range(-1 * shade_diff):
                if material.darker is None:
                    break
                material = material.darker

        age_index = self.calculate_index(
            params.age, self.age_range, params.position, dithering_pattern
        )
        for _ in range(age_index):
            if material.older is None:
                break
            material = material.older

        moist_index = self.calculate_index(
            params.moisture, self.moisture_range, params.position, dithering_pattern
        )
        for _ in range(moist_index):
            if material.more_moist is None:
                break
            material = material.more_moist

        return material

    def calculate_index(
        self,
        value: float,
        dimension_range: int,
        position: ivec3,
        dithering_pattern: DitheringPattern,
    ) -> int:
        if dimension_range == 1:
            return 0

        return dithering_pattern.calculate_index(
            value,
            dimension_range,
            position,
            Seed(recursive_hash(hash_string(0, self.name), *position)),
        )

    def has_block(self, block: Block) -> bool:
        return trim_minecraft_namespace(block.id) in self.blocks.values()

    def has_form(self, form: BlockForm) -> bool:
        return form in self.blocks.keys()

    def get_id(self, form: BlockForm, parameters: MaterialParameters) -> str | None:
        material = self.traverse(parameters)

        return material.blocks[form] if form in material.blocks else None


class CompositeMaterial(Material):
    submaterials: dict[Material, int]

    def random_submaterial(self, seed: Seed) -> Material:
        return seed.choose_weighted(self.submaterials)

    def place_block(
        self,
        editor: Editor,
        form: BlockForm,
        states: dict[str, str] | None,
        data: str | None,
        parameters: MaterialParameters,
    ):
        seed = Seed(recursive_hash(hash_string(0, self.name), *parameters.position))
        return self.random_submaterial(seed).place_block(
            editor, form, states, data, parameters
        )

    def has_block(self, block: Block) -> bool:
        return any(material.has_block(block) for material in self.submaterials)

    def has_form(self, form: BlockForm) -> bool:
        return any(material.has_form(form) for material in self.submaterials)

    def get_id(
        self,
        form: BlockForm,
        parameters: MaterialParameters,
    ) -> str | None:
        seed = Seed(recursive_hash(hash_string(0, self.name), *parameters.position))
        return self.random_submaterial(seed).get_id(form, parameters)

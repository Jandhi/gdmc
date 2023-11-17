from gdpc.editor import Editor
from gdpc.vector_tools import ivec3

from core.structures.nbt.convert_nbt import convert_nbt
from core.structures.nbt.nbt_asset import NBTAsset
from core.structures.transformation import Transformation
from palette.palette import Palette
from palette.palette_swap import palette_swap


# Constructs an NBTAsset given an editor and transformation
def build_nbt(
        editor: Editor,
        asset: NBTAsset,
        palette: Palette = None,
        transformation: Transformation = None,
        place_air: bool = False,
        allow_non_solid_replacement: bool = False,
):
    structure = convert_nbt(asset.filepath)
    transformation = transformation or Transformation()  # construct default value

    transformed_palette = transformation.apply_to_palette(structure.palette)

    for (pos, palette_index_and_nbt) in structure.blocks.items():
        palette_index = palette_index_and_nbt[0]
        nbt = palette_index_and_nbt[1]
        block = transformed_palette[palette_index]

        if block.name in asset.do_not_place or block.name.removeprefix('minecraft:') in asset.do_not_place:
            continue

        if block.name == 'minecraft:air' and not place_air:
            continue

        # don't swap if either are null
        if asset.palette and palette:
            block = block.copy()  # I do this to avoid doubly swapping palettes
            block.name = palette_swap(block.name, asset.palette, palette)

        x, y, z = transformation.apply_to_point(
            point=pos,
            structure=structure,
            asset=asset
        )

        # Doesn't allow non-solid blocks to replace blocks
        if (not allow_non_solid_replacement) and any(
                blocktype in block.name for blocktype in ('stairs', 'slab', 'walls', 'fence')):
            curr_block = editor.getBlock(position=(x, y, z))

            if 'air' not in curr_block.id:
                continue

        if block.name == 'minecraft:barrier':
            block.name = 'minecraft:air'

        editor.placeBlock(position=(x, y, z), block=block.to_gdpc_block(nbt))

    for (pos, entity) in structure.entities.items():
        id = entity[0]
        nbt = entity[1]

        x, y, z = transformation.apply_to_point(
            point=pos,
            structure=structure,
            asset=asset
        )
        summon_entity_command = f'summon {id} {x} {y} {z} {nbt}'
        editor.runCommand(summon_entity_command, position=ivec3(x, y, z))

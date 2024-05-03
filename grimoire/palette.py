from .core.assets.asset import Asset, asset_defaults
from gdpc.lookup import WOOD_TYPES


PLURALS = ["brick", "plank", "tile"]


@asset_defaults(
    primary_wood="oak",
    secondary_wood="spruce",
    primary_stone="cobblestone",
    primary_stone_accent="stone_brick",
)
class Palette(Asset):
    primary_wood: str  # FIXME: Unused variable
    secondary_wood: str
    primary_stone: str
    primary_stone_accent: str  # FIXME: Unused variable

    fields = ["primary_wood", "secondary_wood", "primary_stone", "primary_stone_accent"]


def palette_swap(block_name: str, input_palette: Palette, output_palette: Palette):
    replacements = {
        getattr(input_palette, key): getattr(output_palette, key)
        for key in input_palette.fields
    }

    for target, result in replacements.items():
        if target in block_name:
            # Don't mistake dark_oak for oak
            if target == "oak" and "dark_oak" in block_name:
                continue

            new_val = block_name.replace(target, result)

            for plural in PLURALS:
                # remove plural for combo bricks
                if (
                    target.endswith(plural)
                    and block_name.endswith(f"{plural}s")
                    and not result.endswith(f"{plural}")
                ):
                    new_val = new_val.removesuffix("s")

                # No block ends in a plural without s
                if new_val.endswith(plural):
                    new_val = f"{new_val}s"

                # plank is not used in between words
                if "plank_" in new_val:
                    new_val = new_val.replace("plank_", "")

            return fix_block_name(new_val)

    return fix_block_name(block_name)


# This is used to make a block name consistent with the annoying inconsistencies minecraft has
def fix_block_name(name: str) -> str:
    for plural in PLURALS:
        if name.endswith(plural):
            name = f"{name}s"

    if "plank_" in name:
        name = name.replace("plank_", "")

    for plural in PLURALS:
        if f"{plural}s" in name and not name.endswith(f"{plural}s"):
            name = name.replace(f"{plural}s", plural)

    if "smooth_" in name and "wall" in name:
        name = name.replace("smooth_", "")

    if "wall" in name and any(wood in name for wood in WOOD_TYPES):
        name = name.replace("wall", "fence")

    return name

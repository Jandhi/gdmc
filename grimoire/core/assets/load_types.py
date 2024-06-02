# PUT ALL TYPES HERE SO THAT THEY ARE LOADED


# IMPORTANT: DO NOT OPTIMIZE IMPORTS
def load_types():
    # WALLS
    from ...buildings.walls.wall import Wall
    from ...buildings.walls.wall_nbt import WallNBT

    _ = Wall, WallNBT

    # ROOFS
    from ...buildings.roofs.roof import Roof
    from ...buildings.roofs.roof_component import RoofComponent

    _ = Roof, RoofComponent

    # ROOMS
    from ...buildings.rooms.room import Room

    _ = Room

    # PALETTES
    from grimoire.core.styling.legacy_palette import LegacyPalette

    _ = LegacyPalette

    # BUILDING SHAPE
    from ...buildings.building_shape import BuildingShape

    # Material
    from grimoire.core.styling.materials.material import (
        Material,
        BasicMaterial,
        CompositeMaterial,
    )

    _ = (Material, BasicMaterial, CompositeMaterial)

    _ = BuildingShape

    # PAINT PALETTES
    from ...districts.paint_palette import PaintPalette

    _ = PaintPalette

    # FORESTS
    from ...terrain.forest import Forest

    _ = Forest

    # ASSET STRUCTURE
    from ...core.structures.asset_structure import AssetStructure

    _ = AssetStructure

    # GATE
    from grimoire.districts.gate import Gate

    _ = Gate

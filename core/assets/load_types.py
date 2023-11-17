# PUT ALL TYPES HERE SO THAT THEY ARE LOADED


# IMPORTANT: DO NOT OPTIMIZE IMPORTS
def load_types():
    # WALLS
    from buildings.walls.wall import Wall
    from buildings.walls.wall_nbt import WallNBT 
    from buildings.walls.wall_blueprint import WallBlueprint
    _ = Wall, WallNBT, WallBlueprint

    # ROOFS
    from buildings.roofs.roof import Roof
    from buildings.roofs.roof_component import RoofComponent
    _ = Roof, RoofComponent

    # STYLES
    from style.style import Style
    from style.substyle import Substyle
    _ = Style, Substyle

    # ROOMS
    from buildings.rooms.room import Room
    _ = Room

    # PALETTES
    from palette.palette import Palette
    _ = Palette

    # BUILDING SHAPE
    from buildings.building_shape import BuildingShape
    _ = BuildingShape

    # PAINT PALETTES
    from districts.paint_palette import PaintPalette
    _ = PaintPalette

    # FORESTS
    from terrain.forest import Forest
    _ = Forest

    # ASSET STRUCTURE
    from core.structures.asset_structure import AssetStructure
    _ = AssetStructure

# PUT ALL TYPES HERE SO THAT THEY ARE LOADED

def load_types():
    # WALLS
    from buildings.walls.wall import Wall
    from buildings.walls.wall_nbt import WallNBT 
    from buildings.walls.wall_blueprint import WallBlueprint 

    # ROOFS
    from buildings.roofs.roof import Roof
    from buildings.roofs.roof_component import RoofComponent

    # STYLES
    from style.style import Style
    from style.substyle import Substyle

    # ROOMS
    from buildings.rooms.room import Room

    # PALETTES
    from palette.palette import Palette

    # BUILDING SHAPE
    from buildings.building_shape import BuildingShape
    
    # PAINT PALETTES
    from districts.paint_palette import PaintPalette

    # FORESTS
    from terrain.forest import Forest

    # ASSET STRUCTURE
    from structures.asset_structure import AssetStructure

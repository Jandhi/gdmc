from core.structures.nbt.nbt_asset import NBTAsset
from buildings.walls.wall import Wall
from core.assets.asset import default_subtype

# NBT class for walls
@default_subtype(Wall)
class WallNBT(NBTAsset, Wall):
    type_name = 'wall_nbt'
    facing : str
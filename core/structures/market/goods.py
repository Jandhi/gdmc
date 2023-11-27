from dataclasses import dataclass

@dataclass
class Flower_Shop:
    counter_goods : list = ('flower_pot', 'potted_lily_of_the_valley', 
        'potted_dandelion', 'potted_cornflower', 'potted_poppy',
        'potted_allium', 'potted_blue_orchid', 'potted_azure_bluet',
        'potted_red_tulip', 'potted_pink_tulip', 'potted_white_tulip',
        'potted_orange_tulip', 'potted_oxeye_daisy', 'flower_pot',
        'flower_pot')

    floor_goods : list = ('flower_pot', 'potted_lily_of_the_valley', 
        'potted_dandelion', 'potted_cornflower', 'potted_poppy',
        'potted_allium', 'potted_blue_orchid', 'potted_azure_bluet',
        'potted_red_tulip', 'potted_pink_tulip', 'potted_white_tulip',
        'potted_orange_tulip', 'potted_oxeye_daisy', 'flower_pot',
        'flower_pot')

@dataclass
class Plant_Shop:
    counter_goods : list = ('flower_pot', 'potted_fern', 
        'potted_birch_sapling', 'potted_oak_sapling', 'potted_jungle_sapling',
        'potted_spruce_sapling', 'potted_acacia_sapling', 'potted_dark_oak_sapling',
        'potted_cactus', 'potted_bamboo', 'potted_dead_bush',
        'flower_pot')

    floor_goods : list = ('flower_pot', 'potted_fern', 
        'potted_birch_sapling', 'potted_oak_sapling', 'potted_jungle_sapling',
        'potted_spruce_sapling', 'potted_acacia_sapling', 'potted_dark_oak_sapling',
        'potted_cactus', 'potted_bamboo', 'potted_dead_bush',
        'flower_pot')

@dataclass
class Head_Shop:
    counter_goods : list = ('dragon_head', 'creeper_head', 
        'zombie_head', 'skeleton_skull', 'wither_skeleton_skull')

    floor_goods = False

@dataclass
class Wool_Shop:
    counter_goods : list = ('cyan_carpet', 'light_gray_carpet', 
        'lime_carpet', 'light_blue_carpet', 'purple_carpet',
        'green_carpet', 'blue_carpet', 'brown_carpet',
        'red_carpet', 'black_carpet', 'orange_carpet',
        'magenta_carpet', 'white_carpet', 'white_carpet',
        'gray_carpet', 'pink_carpet', 'yellow_carpet')

    floor_goods = False

@dataclass
class Glazed_Terracotta_Shop:
    counter_goods : list = ('cyan_glazed_terracotta', 'light_gray_glazed_terracotta', 
        'lime_glazed_terracotta', 'light_blue_glazed_terracotta', 'purple_glazed_terracotta',
        'green_glazed_terracotta', 'blue_glazed_terracotta', 'brown_glazed_terracotta',
        'red_glazed_terracotta', 'black_glazed_terracotta', 'orange_glazed_terracotta',
        'magenta_glazed_terracotta', 'white_glazed_terracotta', 'white_glazed_terracotta',
        'gray_glazed_terracotta', 'pink_glazed_terracotta', 'yellow_glazed_terracotta')

    floor_goods = False

@dataclass
class Glass_Shop:
    counter_goods : list = ('cyan_stained_glass', 'light_gray_stained_glass', 
        'lime_stained_glass', 'light_blue_stained_glass', 'purple_stained_glass',
        'green_stained_glass', 'blue_stained_glass', 'brown_stained_glass',
        'red_stained_glass', 'black_stained_glass', 'orange_stained_glass',
        'magenta_stained_glass', 'white_stained_glass', 'white_stained_glass',
        'glass', 'glass', 'glass',
        'gray_stained_glass', 'pink_stained_glass', 'yellow_stained_glass')

    floor_goods = False

@dataclass
class Shulker_Shop:
    counter_goods : list = ('cyan_shulker_box', 'light_gray_shulker_box', 
        'lime_shulker_box', 'light_blue_shulker_box', 'purple_shulker_box',
        'green_shulker_box', 'blue_shulker_box', 'brown_shulker_box',
        'red_shulker_box', 'black_shulker_box', 'orange_shulker_box',
        'magenta_shulker_box', 'white_shulker_box', 'white_shulker_box',
        'shulker_box', 'shulker_box', 'shulker_box',
        'gray_shulker_box', 'pink_shulker_box', 'yellow_shulker_box')

    floor_goods = False

@dataclass
class Fruit_Shop:
    counter_goods : list = ('melon', 
        'pumpkin', 'sea_pickle[waterlogged=false]',
        'player_head{SkullOwner:{Id:[I;440871046,979259357,-1150162889,656058295],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvM2U4MGM3M2I3NjVkOWYyZTJhMWFlNmQ5ZGY5NmM1ZmJjNjEyNmVlNTRmOWRmMGE0NmJiMWYwMGVmMGIwMjc5ZSJ9fX0="}]}}}', #grapes
        'player_head{SkullOwner:{Id:[I;63039476,2129742085,-1180142245,879747787],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMWMxZGYzYjA5NWU2YTc3NGUyNjg1MjkwMWRiMjM0MDAzOTc5YzdhNzVjZTM1ZDhkMjY5YmIzNjUxZTA5Y2ZhMiJ9fX0="}]}}}',
        'player_head{SkullOwner:{Id:[I;250894311,-426423829,-1288085365,-1025692468],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZTZlZjYxNGIzYTVmYmVjOWI4YWYzNWQ4YTQwZTkxZGNjZGQ4OTc3YzcxMmVjZWY2Y2U1MmQ5MWFmNDljNGM5MyJ9fX0="}]}}}',
        'player_head{SkullOwner:{Id:[I;-804584272,-2025894249,-1991833207,1934450085],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvN2U1N2NjNTZmYjIxZDUwYWY0ODkwYTU5YTE4Y2Y5MTliZWExYzJiMTMxNzFlMTA0ZDMyYWU2N2VkYTQ5YWExNiJ9fX0="}]}}}',
        'player_head{SkullOwner:{Id:[I;-599632864,420759340,-1682349005,306850637],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZTI0YzAzMDkzNmU0NWVhNTAwMjI3ZjgyNGM4NDQzOTllM2Q4MjdlMThkZDllNWNjMTA2YTFmMTIzZTNkMTE4ZCJ9fX0="}]}}}', #coconut
        'player_head{SkullOwner:{Id:[I;-1780260428,444088566,-1336051849,2051489197],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZTQ4OTVhYTY3MjQ3YzNlYjQwNmZiOTA1ZDNmNmQzNWFjZDY2MGM2ZjE0YTg1YmNmN2JmYjg5OGI4MjY0NmU3MCJ9fX0="}]}}}', #mango
        'player_head{SkullOwner:{Id:[I;78628529,943473184,-1084272797,1344757089],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNjkwNGY2Yzg2ZDlkZTQxNTEyNmRkMWVjOGRkMDliZGVmNzkyOWY0M2YwZGIwOTI3ODQ1N2Y1YzEzZjgzMWQzMSJ9fX0="}]}}}', #watermelon
        'player_head{SkullOwner:{Id:[I;59444613,353258137,-1673204155,-85291877],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYWE5NTJkMjcyYjc0ODVmYzNiNDE5ZTU2ZDczMDc0ZmMxOGNmMzExZTU0MTNhODNhMTFlMWU5Njc3YmQ1MDBmIn19fQ=="}]}}}', #berry
        'player_head{SkullOwner:{Id:[I;195096767,-673101249,-1383848161,-384997094],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZmFkYmJhYjM4ODFhYWNiYTU3N2UyN2JiZWUxZmJlNGI5YTUwZTE5ZjVhODdmOGQ0OWI2MzYwNTRmYTE3ODhmYyJ9fX0="}]}}}', #peach
        'player_head{SkullOwner:{Id:[I;1132898532,-1424472158,-1939797510,2120188451],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNTM0MTA0YmIxNDQyYjQwMzRjZjMyNTk1YTA4N2I3YTUxZDk2Y2U1OTE1YzE4MmQ4MzNlZWZhNjhlMWNlYzFmZiJ9fX0="}]}}}', #apricot
        'player_head{SkullOwner:{Id:[I;-1708676441,-400405197,-2089810782,114161513],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvN2M3MWZmZmM1ZmViZDc2MGRkYzg5ZmQxZDM3ZTJhZGFjMzZjYTZkMjNhMWRjMTNlMTY0OWY0YTdmYTNkYTRhIn19fQ=="}]}}}', #mulberry
        'player_head{SkullOwner:{Id:[I;-625799911,-1259515920,-1473823578,1164892648],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMzA3ODJjMjNiOTBmMDFiMzVhZTMwMTZjN2NkNGJjMzg0NzA5NzIxZWI3MDkwOGM3ZDc4YmExNzJmMGU5NzBmMyJ9fX0="}]}}}', #plum
        'player_head{SkullOwner:{Id:[I;1642145058,488521807,-1658809039,-1691057906],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYzY4ZGQ1OTViZGM2OGUxYThkYzg0ZDc4OWYyMTc5MWVkZDA1M2JhM2JiZWRiZmVjMmU3ZGFhNzI0M2FlYTIxNyJ9fX0="}]}}}', #pear
        'player_head{SkullOwner:{Id:[I;-757963522,-214414840,-1797638249,-121624633],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNWNkYWQyMzQ5NDgzYzBkNDg5Y2M0NjRiZWVkNzI4YzZhMDQxOTkyYTIwMWQyM2FlNTU1MzFmMDMzNGZjMTQwOSJ9fX0="}]}}}', #tangerine
        'player_head{SkullOwner:{Id:[I;-483863813,-2117778070,-2110758150,349817437],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNzJkZjRlNjc0OTUxYzEzOGU3MzExMTI3NTYxZmRiZDI3ZTIxNTA3MTZiMDJiYjU2ODc0N2Y4NTQ1ZmIyMDE0NSJ9fX0="}]}}}') #tomato

    floor_goods = False

@dataclass
class Armour_Shop:
    counter_goods : list = ('light_weighted_pressure_plate', 'heavy_weighted_pressure_plate',
        'player_head{SkullOwner:{Id:[I;864431335,1436894342,-1274960042,1899380984],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNGFmZjNmZmYzYWQ1ZDEwODA4Mzc5YWUyMDFiODMyYmZlZThhYzIyNjVmYmJlNjg0MTdkMTBmYjVmNThiMmQ4NSJ9fX0="}]}}}') #knight helmet

    floor_goods : list = ('armor_stand{ShowArms:1b,NoBasePlate:1b,ArmorItems:[{id:"minecraft:leather_boots",Count:1b},{id:"minecraft:leather_leggings",Count:1b},{id:"minecraft:leather_chestplate",Count:1b},{id:"minecraft:leather_helmet",Count:1b}]}',
    'armor_stand{ShowArms:1b,NoBasePlate:1b,ArmorItems:[{id:"minecraft:golden_boots",Count:1b},{id:"minecraft:golden_leggings",Count:1b},{id:"minecraft:golden_chestplate",Count:1b},{id:"minecraft:golden_helmet",Count:1b}]}',
    'armor_stand{ShowArms:1b,NoBasePlate:1b,ArmorItems:[{id:"minecraft:iron_boots",Count:1b},{id:"minecraft:iron_leggings",Count:1b},{id:"minecraft:iron_chestplate",Count:1b},{id:"minecraft:iron_helmet",Count:1b}]}')

@dataclass
class Bakery_Shop:
    counter_goods : list = ('cake', 
        'player_head{SkullOwner:{Id:[I;-21398596,-1543683656,-1597670807,-634417771],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOTA0NzcxMzRkMmFjNTI1NjlmMDYyNzA3YjA0ZTRhMzdhNzBhOWZlZDYxMTBjN2QyZjE0NWY3NmJlMWNkODI2ZSJ9fX0="}]}}}', #pie
        'player_head{SkullOwner:{Id:[I;843234447,-1704705483,-1304221926,751006699],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOTFhZjQ4ZGNhNDQ5NGMzNDEzYjk5MTc1OThlOWFmNWRjZjc4ODAwYTIxOGI1ZTg4NTY5Njk1ZDAyMjQyMjNkOSJ9fX0="}]}}}', #cake
        'player_head{SkullOwner:{Id:[I;-897978921,-643543982,-1992335549,230496868],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNTUyN2Q4Yjg0NjJiNzlkYjdmODE2OTY4YjliY2MzMDlhNTRjMzBlZDFiZTY5MjMwNTUzN2JjZmY4MjgzZDNkMCJ9fX0="}]}}}', #toast
        'player_head{SkullOwner:{Id:[I;1019301451,653542912,-1625067858,1609338968],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYWQyNTJmM2M1NTI2ZGU4MTNlNzg5ZmQzMWNhMDQ1MWY2OGQ4MGJlMWQ1ZjJjODlkYzY1NDJjMTQxZTFhODMzMSJ9fX0="}]}}}', #cake
        'player_head{SkullOwner:{Id:[I;-1768855902,-1259189138,-1596916416,327187835],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNzI5ZTNhMTFiYmRjNzhjNjZkNzkwNmVlOWNhNGE5Y2Y3ZDIyMDVhNDE3Y2FhM2M4ZWZmNzRmNTNiZDQzMDZiNyJ9fX0="}]}}}', #cookie
        'player_head{SkullOwner:{Id:[I;-228580091,-1028111819,-1318891776,1652123010],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNjMyNTQ1YTk4OTdjNGYwODA5ZDdlOWQ3ZGU0YjQ5OWNhZmQ4ZDZhNDJhMGVhY2Y0Y2FhYmYzNDg4YWRjYTIxMSJ9fX0="}]}}}') #bread

    floor_goods = False

@dataclass
class Bell_Pepper_Shop: #4 different pepper colours
    counter_goods : list = ('player_head{SkullOwner:{Id:[I;1344612946,1873821837,-1292649600,1454823410],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNjVmNzgxMDQxNGEyY2VlMmJjMWRlMTJlY2VmN2E0Yzg5ZmM5YjM4ZTlkMDQxNGE5MDk5MTI0MWE1ODYzNzA1ZiJ9fX0="}]}}}', 
        'player_head{SkullOwner:{Id:[I;1539987331,313803853,-2027297740,798004782],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvODgzZjI4MDg4ZjQ3ZGYzMDIyNDZjZGUwNTk0OWFmNjVjNDVmNGU3MmE0MjMxZjg4NmNjMzJmZDMxZmI3YjEyYyJ9fX0="}]}}}',
        'player_head{SkullOwner:{Id:[I;98082288,192692695,-1184096860,60587389],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvN2U1ZTgyOTNjMTU4ZWIyMzg4NWE0NzRmM2E3OWM3MDQ5MTM5MGI3NmZkZGM0NmIyNTFjOGRiYWQ2MDAxNTVmNCJ9fX0="}]}}}',
        'player_head{SkullOwner:{Id:[I;393662941,717112880,-1133876717,1517023709],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZWEzYWJkMzNkMWUyMzNmMzViNTAzYmZlM2Y2YjQwOGI5YTE4YWJiM2UyNjUwYmJhYTZjYTM4ZjQ5YjdhZDIyMSJ9fX0="}]}}}')

    floor_goods = False

@dataclass
class Japanese_Shop:
    counter_goods : list = ('player_head{SkullOwner:{Id:[I;-383345864,-2114305331,-1190798659,1984883991],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNTBlMzBlODhiMmQyMGFkMDZlMjc5MWM4M2Q1YTQxZGE3YmYyZDJlMzBmZWVjZGNiOGU0ZTFmMWFiNzE4OTA1In19fQ=="}]}}}', #takoyaki
        'player_head{SkullOwner:{Id:[I;1421633831,-1315615434,-1331915359,-265425474],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZTUzNDdkYWRmNjgxOTlmYTdhMWI2NmYwNDgxYWQ4ZTlkYWVlMTUxMDg2NWFkZDZmMzNkMTVmYjM3OGQxM2U5MSJ9fX0="}]}}}', #sushi
        'player_head{SkullOwner:{Id:[I;1938737086,1257783728,-1693272672,-895600016],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMjNjYTNmOTI2ZTdhOWFiOTU1NWZlY2I2OWE4MDI3NDNjMTIyZDllZmM1NjVhMmZlNTU0NTExOGZhOTFkMSJ9fX0="}]}}}', #sushi
        'player_head{SkullOwner:{Id:[I;-26572071,311050408,-1779130003,1709813103],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNGMwOTU5NmE4Yzk4YTNlNjlhNjYwNzliY2MwN2I4MWIwMzZjOTIwNGI3YWJjODdjMTgyMDRlZDg0ZDc4OTM0MCJ9fX0="}]}}}') #sushi

    floor_goods = False

@dataclass
class Honey_Shop:
    counter_goods : list = ('honeycomb_block', 'beehive', 'bee_nest', 
        'player_head{SkullOwner:{Id:[I;-215579961,-905753219,-1517363442,1147482927],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYmI5OTYwZWFkZTJkY2I2ZTc0NGM3ZDA4NGRlZjAwNTk5ZmU3MzI3ZTM5NzNjZDJjYTBhZjRhMmExZTZlYWMwOCJ9fX0="}]}}}', #honey bottle
        'player_head{SkullOwner:{Id:[I;375660980,-893171393,-1622961162,-1836959800],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYjlkY2U1OWJhNzJmODQ3MzZlMWVhOWMzYjQzZWIxYWFkYzQ5N2IyOTA0YTFjZGEwODk3MjY5MmRjMWI0Y2E3NSJ9fX0="}]}}}', #beehive
        'player_head{SkullOwner:{Id:[I;-1945090372,-1701363517,-1482003043,-720073087],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvODhkMDZjNzM0NjYwMjk0YTE1Zjc2ZjNjYmFmMzc4NWFlNmMwOTMyOWIwMTZjZGRlYzU2ZjgyMmZmYzY2MGY0YSJ9fX0="}]}}}', #beehive
        'player_head{SkullOwner:{Id:[I;371347668,-352956824,-1469947658,102849469],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOGI4OTQyYjIyZGRkMjQ0MWYyY2U2YWQ2NTY3Zjg3NzRhOTdjYTZiMmE4MzJhM2FhZjVlNWNjNmJhY2JmIn19fQ=="}]}}}', #honeypot
        'player_head{SkullOwner:{Id:[I;2061359882,1553943730,-2026977421,1376425424],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYjkwNmJmZDgxN2NjNTgxOGM3NjIwZTI4OGY0ZTQxMzAxNDMxOGMwYmNiYjVlY2Q2ZGE4YTU5MjNkNTFjNTJmMiJ9fX0="}]}}}') #honeyjar

    floor_goods = False

@dataclass
class Donut_Shop: #all blocks are donuts
    counter_goods : list = ('player_head{SkullOwner:{Id:[I;532742587,-1304212876,-1697788453,1676318830],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZGY1OTI1ZWQ1MDM2MWY5Yjc5MWRkMDgyODkxMTE4ZTYwYjljM2ZhZWQ2Nzc1MDQ5ZmYyOTM4YmU4MTMxMDQ1MSJ9fX0="}]}}}', 
        'player_head{SkullOwner:{Id:[I;467471868,1648772588,-1091889403,1557911283],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvODYwYWMyZTVhNTFiZjE4MTQ2M2M4YWM2YzliYWE4MDkyZDI2NDRkMTNiMjkxMDkxMGVmNzk5YTNjNTI2OWUxZSJ9fX0="}]}}}',
        'player_head{SkullOwner:{Id:[I;-644891548,-1546434986,-1360309712,1823352225],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZWQyNWRjYzAzZDgxNDU2Mjg4MTQ4MDkxMTNmMDllNDEzODU4ODNiNzM5YWVlNTE5MWViZjMwMjFmYTAyZmJkNyJ9fX0="}]}}}',
        'player_head{SkullOwner:{Id:[I;-1736400799,1295338254,-1494844268,-578878738],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNGViNzRmYjdiYWFkMGY0OTRjMGFmOTA3M2Q4NjczODg5YjgzMWEzNGYxYjgxOTNlNmE2Njg3NjYzNGFiZjc0YyJ9fX0="}]}}}',
        'player_head{SkullOwner:{Id:[I;-2013432875,1296056915,-1442315914,-2084278540],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMjBhZGQ0NDc1MjMyODBjMGJkN2Q4ODQyZjVkNzg3Mzg5NTYxNTBiNjg1ODU1Mzg1NmRjOWQwYjdjM2Y3MDlkMCJ9fX0="}]}}}',
        'player_head{SkullOwner:{Id:[I;-1961563422,548556076,-1304724307,459871975],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNDExYWVkYTc2OWM5MDkyY2Q0MjVhYWZiNGE0MzNjYjFlNTBiZGYzNDEwMmZkZTYwNWRhNmJhYTY1M2E3YTM4NSJ9fX0="}]}}}',
        'player_head{SkullOwner:{Id:[I;626180132,-575650928,-1942147131,-1443737357],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZmExODYyYTIzOTliNzRmOWIwZDFjYWJlYzMxNmNmNDNjMTNhMTFmMmM4Y2U5OWQwODQ5NmQ2NjBmM2ZkNjgyNyJ9fX0="}]}}}',
        'player_head{SkullOwner:{Id:[I;-1785464174,-1679997546,-1287987767,-1938766415],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOTc5ZTcwNzBhZmY5MzRkNjExMDI4MzgwZGNkOTllNjFhYWViOTY4OTUzMDhhMzAwZjJjYjgxNjEyZDU5Mjk0YSJ9fX0="}]}}}',
        'player_head{SkullOwner:{Id:[I;1631315097,1953057693,-1337120994,309194269],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZDA4MjM2YjQ0ZjNmYzExYjAwMjgwNTQ4NDg3MmMyNTFlOTk0YWJjMzdhMWQ1ZjFkYmI3NmM4MTFlNzY3ZDFjNyJ9fX0="}]}}}',
        'player_head{SkullOwner:{Id:[I;-730858374,1301104811,-1110669929,-2078416039],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNTM1NzJhMWJhMDY2MzI0NWQ1N2JjMTQ2Yjk3OWU5MWMwN2EwMmExYzg5YWQzZjg3NTFiYWZlMmFiMTg4NjQ0In19fQ=="}]}}}')

    floor_goods = False

@dataclass
class Butcher_Shop:
    counter_goods : list = ('player_head{SkullOwner:{Id:[I;-1697893344,482626784,-1900324603,-1837649629],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMTg0ZGZhN2YxMTBhMjliNzZkNDUwMjE2NjRhYWQzNDRlOWE5OGVmODdkOWRlMWQyMzViMzEwNzFmYTVkMTAxOCJ9fX0="}]}}}', #turkey
        'player_head{SkullOwner:{Id:[I;924420102,-1020899782,-2135386945,-119827233],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNjY3ZjkxYTAyN2I2ZGMwNjQ5ZTc4YTE2YWQ2ZWRiMzVjNTg0ZWVlYzE5M2QwNzRiMmU5NzcwOWFhOWU3ZmNkNiJ9fX0="}]}}}', #meat
        'player_head{SkullOwner:{Id:[I;924420102,-1020899782,-2135386945,-119827233],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNjY3ZjkxYTAyN2I2ZGMwNjQ5ZTc4YTE2YWQ2ZWRiMzVjNTg0ZWVlYzE5M2QwNzRiMmU5NzcwOWFhOWU3ZmNkNiJ9fX0="}]}}}', #cooked fish
        'player_head{SkullOwner:{Id:[I;893203725,-1998110178,-1981459574,913017758],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMTBlZGI0N2Y5MWJkYjVhZjBmZGYzMjkwYzdkMTgxMTYzZjVkZjcyYTNiMWM3YmVkYTFkMDY5MmUzNmMxNThkYSJ9fX0="}]}}}', #pepperoni
        'player_head{SkullOwner:{Id:[I;1150127731,-977647945,-1233667027,-1603611890],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZDNlMjBhMjZjYmI1NzQwYTE1OGRhOTkxZWY5NGRjZDMyZDQ0N2U5YWMwM2FhMGU4ZjgyOWE0OTgzMDYxOWExMCJ9fX0="}]}}}', #cooked chicken
        'player_head{SkullOwner:{Id:[I;-987506310,1707690889,-1924457192,-1478082841],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZDgwN2YyMDk0MmQ4NGEzYjczM2ExYTJkNjZkZTQ3NWJmNDE2YzJlNmM1NTQyMTM2Nzc0MmIxNzcwNmJhMjE1OSJ9fX0="}]}}}') #ham

    floor_goods = False

@dataclass
class Alcohol_Shop:
    counter_goods : list = ('player_head{SkullOwner:{Id:[I;-733558164,2016231772,-1917138577,-484030463],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYmQyYjY1Yjc5YjQ5MDQ1MTRhMGZjNzIzMmVhODlhOWU4YzZhYzYwZWUzZGJhMWI1OTc1Yjc3NTUxMjczMzhhNCJ9fX0="}]}}}', #wine
        'player_head{SkullOwner:{Id:[I;426302625,58016472,-1672328477,977653860],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZGU5OWE0MDYxNTAwNDhmYTI2NzMxNjA0MDljYTY4NjY2MmNlMGYxYzdhNGVlNTRjMjBlY2M5MDFjOWQwYmQ2ZiJ9fX0="}]}}}', #mug of beer
        'player_head{SkullOwner:{Id:[I;-157457202,-1512816604,-2054521656,1233347456],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNTMxNDQ0YjdmMTYwYjA3Zjg5ZTFhOThlNzljYTFjMTc5ZTAzNzE2ZTY3ODUwMmVkNzU5NzU0NWNhZjE5MzgyOCJ9fX0="}]}}}', #beer 
        'player_head{SkullOwner:{Id:[I;679691285,-1353823811,-2083581681,1045079152],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNDg0MzdmZWU3NDljYmQ2OGYzNDQzYmIwNmU0NTA1OGE2ODdjMGZjYTk2NDM2Y2FkYjUzOGNhZDU5YjUyMTZjNiJ9fX0="}]}}}', #beer barrel
        'player_head{SkullOwner:{Id:[I;-1435884538,271795998,-1808037575,-292356502],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZDg0M2UwNmZkNGU2ZTU2ZDI1NTRlYTJkZGU4Mzc4M2I4MTY3NWZlYjI0YjE2N2ZlOThiMzgyN2U0ZjYyNTQ0NiJ9fX0="}]}}}', #beer medieval
        'player_head{SkullOwner:{Id:[I;-1513351130,1351370996,-1551837317,-2013369534],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOGY3ZGM4YzkxZjdhMjRlY2Q5YzVlOWQ0ZDhjMzlmMGFjODMzM2FlNDg1MzU1OWFjYjhiMDM4NjZmOWQifX19"}]}}}') #beer medieval

    floor_goods = False

# for ease of making new dataclasses copy below
# @dataclass
# class _Shop:
#     counter_goods : list[] = ('player_head', 
#         'player_head',
#         'player_head',
#         'player_head')

#     floor_goods = False
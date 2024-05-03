import sys

sys.path[0] = sys.path[0].removesuffix("\\industries")

ROUGHNESS_LOW = "roughness_low"
ROUGHNESS_MID = "roughness_mid"
ROUGHNESS_HIGH = "roughness_high"
ROUGHNESS = (ROUGHNESS_LOW, ROUGHNESS_MID, ROUGHNESS_HIGH)

TEMPERATURE_LOW = "temperature_low"
TEMPERATURE_MID = "temperature_mid"
TEMPERATURE_HIGH = "temperature_high"
TEMPERATURE = (
    TEMPERATURE_LOW,
    TEMPERATURE_MID,
    TEMPERATURE_HIGH,
)

ACQUATIC_NONE = "acquatic_none"
ACQUATIC_COASTAL = "acquatic_coastal"
ACQUATIC_SMALL_BODY = "acquatic_small_body"
ACQUATIC_LARGE_BODY = "acquatic_large_body"

ACQUATIC = (
    ACQUATIC_NONE,
    ACQUATIC_COASTAL,
    ACQUATIC_SMALL_BODY,
    ACQUATIC_LARGE_BODY,
)

BARREN = "barren"
WOODED = "wooded"

WOOD = (BARREN, WOODED)

all_biomes = {
    "plains": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_NONE),
    "sunflower_plains": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_NONE),
    "tundra": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_NONE),
    "snowy_plains": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_NONE),
    "ice_spikes": (ROUGHNESS_HIGH, TEMPERATURE_LOW, ACQUATIC_NONE),
    "mangrove_swamp": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_SMALL_BODY),
    "badlands": (ROUGHNESS_MID, TEMPERATURE_HIGH, ACQUATIC_NONE),
    "eroded_badlands": (ROUGHNESS_HIGH, TEMPERATURE_HIGH, ACQUATIC_NONE),
    "warm_ocean": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_LARGE_BODY),
    "deep_lukewarm_ocean": (
        ROUGHNESS_LOW,
        TEMPERATURE_MID,
        ACQUATIC_LARGE_BODY,
    ),
    "ocean": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_LARGE_BODY),
    "deep_ocean": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_LARGE_BODY),
    "cold_ocean": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_LARGE_BODY),
    "deep_cold_ocean": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_LARGE_BODY),
    "frozen_ocean": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_LARGE_BODY),
    "deep_frozen_ocean": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_LARGE_BODY),
    "frozen_river": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_SMALL_BODY),
    "snowy_beach": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_COASTAL),
    "dark_forest": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_NONE),
    "snowy_taiga": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_NONE),
    "wooded_badlands": (ROUGHNESS_MID, TEMPERATURE_HIGH, ACQUATIC_NONE),
    "grove": (ROUGHNESS_HIGH, TEMPERATURE_LOW, ACQUATIC_NONE),
    "snowy_slopes": (ROUGHNESS_HIGH, TEMPERATURE_LOW, ACQUATIC_NONE),
    "frozen_peaks": (ROUGHNESS_HIGH, TEMPERATURE_LOW, ACQUATIC_NONE),
    "jagged_peaks": (ROUGHNESS_HIGH, TEMPERATURE_LOW, ACQUATIC_NONE),
    "stony_peaks": (ROUGHNESS_HIGH, TEMPERATURE_MID, ACQUATIC_NONE),
    "stony_shore": (ROUGHNESS_HIGH, TEMPERATURE_LOW, ACQUATIC_COASTAL),
    "jungle": (ROUGHNESS_MID, TEMPERATURE_HIGH, ACQUATIC_NONE),
    "sparse_jungle": (ROUGHNESS_LOW, TEMPERATURE_HIGH, ACQUATIC_NONE),
    "bamboo_jungle": (ROUGHNESS_MID, TEMPERATURE_HIGH, ACQUATIC_NONE),
    "savanna": (ROUGHNESS_MID, TEMPERATURE_HIGH, ACQUATIC_SMALL_BODY),
    "savanna_plateau": (ROUGHNESS_MID, TEMPERATURE_HIGH, ACQUATIC_SMALL_BODY),
    "windswept_savanna": (
        ROUGHNESS_HIGH,
        TEMPERATURE_HIGH,
        ACQUATIC_SMALL_BODY,
    ),
    "old_growth_pine_taiga": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_NONE),
    "old_growth_spruce_taiga": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_NONE),
    "taiga": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_NONE),
    "windswept_hills": (ROUGHNESS_MID, TEMPERATURE_LOW, ACQUATIC_NONE),
    "windswept_gravelly_hills": (
        ROUGHNESS_MID,
        TEMPERATURE_LOW,
        ACQUATIC_NONE,
    ),
    "windswept_forest": (ROUGHNESS_MID, TEMPERATURE_LOW, ACQUATIC_NONE),
    "birch_forest": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_NONE),
    "old_growth_birch_forest": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_NONE),
    "desert": (ROUGHNESS_LOW, TEMPERATURE_HIGH, ACQUATIC_NONE),
    "beach": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_COASTAL),
    "forest": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_NONE),
    "flower_forest": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_NONE),
    "swamp": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_SMALL_BODY),
    "meadow": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_NONE),
    "river": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_SMALL_BODY),
    "mushroom_fields": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_COASTAL),
}

plains = {
    "plains": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_NONE),
    "sunflower_plains": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_NONE),
    "snowy_plains": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_NONE),
    "meadow": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_NONE),
    "tundra": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_NONE),
}

snowy = {
    "snowy_plains": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_NONE),
    "ice_spikes": (ROUGHNESS_HIGH, TEMPERATURE_LOW, ACQUATIC_NONE),
    "snowy_taiga": (ROUGHNESS_MID, TEMPERATURE_LOW, ACQUATIC_NONE),
    "grove": (ROUGHNESS_HIGH, TEMPERATURE_LOW, ACQUATIC_NONE),
    "snowy_slopes": (ROUGHNESS_MID, TEMPERATURE_LOW, ACQUATIC_NONE),
    "frozen_peaks": (ROUGHNESS_HIGH, TEMPERATURE_LOW, ACQUATIC_NONE),
    "jagged_peaks": (ROUGHNESS_HIGH, TEMPERATURE_LOW, ACQUATIC_NONE),
    "frozen_river": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_SMALL_BODY),
    "snowy_beach": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_COASTAL),
    "frozen_ocean": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_LARGE_BODY),
}

cold = {
    "old_growth_pine_taiga": (ROUGHNESS_MID, TEMPERATURE_LOW, ACQUATIC_NONE),
    "old_growth_spruce_taiga": (ROUGHNESS_MID, TEMPERATURE_LOW, ACQUATIC_NONE),
    "taiga": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_NONE),
    "windswept_hills": (ROUGHNESS_MID, TEMPERATURE_LOW, ACQUATIC_NONE),
    "windswept_gravelly_hills": (
        ROUGHNESS_MID,
        TEMPERATURE_LOW,
        ACQUATIC_NONE,
    ),
    "windswept_forest": (ROUGHNESS_MID, TEMPERATURE_LOW, ACQUATIC_NONE),
    **snowy,
}

# unique style
desert = {"desert": (ROUGHNESS_LOW, TEMPERATURE_HIGH, ACQUATIC_NONE)}

swamp = {
    "swamp": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_SMALL_BODY),
    "mangrove_swamp": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_SMALL_BODY),
}

badlands = {
    "badlands": (ROUGHNESS_MID, TEMPERATURE_HIGH, ACQUATIC_NONE),
    "eroded_badlands": (ROUGHNESS_HIGH, TEMPERATURE_HIGH, ACQUATIC_NONE),
    "wooded_badlands": (ROUGHNESS_MID, TEMPERATURE_HIGH, ACQUATIC_NONE),
}

ocean = {
    "warm_ocean": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_LARGE_BODY),
    "deep_lukewarm_ocean": (
        ROUGHNESS_LOW,
        TEMPERATURE_MID,
        ACQUATIC_LARGE_BODY,
    ),
    "ocean": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_LARGE_BODY),
    "deep_ocean": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_LARGE_BODY),
    "cold_ocean": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_LARGE_BODY),
    "deep_cold_ocean": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_LARGE_BODY),
    "frozen_ocean": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_LARGE_BODY),
    "deep_frozen_ocean": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_LARGE_BODY),
}

aquatic = {
    "river": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_SMALL_BODY),
    "frozen_river": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_SMALL_BODY),
    **ocean,
}

shore = {
    "beach": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_COASTAL),
    "snowy_beach": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_COASTAL),
    "stony_shore": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_COASTAL),
    **ocean,
}

# should consider foresty things
forest = {
    "forest": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_NONE),
    "flower_forest": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_NONE),
    "birch_forest": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_NONE),
    "dark_forest": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_NONE),
    "old_growth_birch_forest": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_NONE),
    "old_growth_pine_taiga": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_NONE),
    "old_growth_spruce_taiga": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_NONE),
    "taiga": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_NONE),
    "snowy_taiga": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_NONE),
    "windswept_forest": (ROUGHNESS_MID, TEMPERATURE_LOW, ACQUATIC_NONE),
    "wooded_badlands": (ROUGHNESS_MID, TEMPERATURE_HIGH, ACQUATIC_NONE),
    "grove": (ROUGHNESS_HIGH, TEMPERATURE_LOW, ACQUATIC_NONE),
}

# we should add more rocks
rocky = {
    "windswept_hills": (ROUGHNESS_HIGH, TEMPERATURE_MID, ACQUATIC_NONE),
    "windswept_gravelly_hills": (
        ROUGHNESS_HIGH,
        TEMPERATURE_MID,
        ACQUATIC_NONE,
    ),
    "windswept_forest": (ROUGHNESS_HIGH, TEMPERATURE_MID, ACQUATIC_NONE),
    "windswept_savanna": (ROUGHNESS_HIGH, TEMPERATURE_HIGH, ACQUATIC_NONE),
    "snowy_slopes": (ROUGHNESS_HIGH, TEMPERATURE_LOW, ACQUATIC_NONE),
    "frozen_peaks": (ROUGHNESS_HIGH, TEMPERATURE_LOW, ACQUATIC_NONE),
    "jagged_peaks": (ROUGHNESS_HIGH, TEMPERATURE_LOW, ACQUATIC_NONE),
    "stony_peaks": (ROUGHNESS_HIGH, TEMPERATURE_MID, ACQUATIC_NONE),
    "stony_shore": (ROUGHNESS_HIGH, TEMPERATURE_LOW, ACQUATIC_COASTAL),
}

# by wood
oak = {
    "forest": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_NONE),
    "flower_forest": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_NONE),
    "swamp": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_SMALL_BODY),
    "meadow": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_NONE),
    "river": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_SMALL_BODY),
    "mushroom_fields": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_COASTAL),
    **badlands,
}

birch = {
    "flower_forest": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_NONE),
    "birch_forest": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_NONE),
    "old_growth_birch_forest": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_NONE),
    "desert": (ROUGHNESS_LOW, TEMPERATURE_HIGH, ACQUATIC_NONE),
    "beach": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_COASTAL),
}

spruce = {
    "old_growth_pine_taiga": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_NONE),
    "old_growth_spruce_taiga": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_NONE),
    "taiga": (ROUGHNESS_LOW, TEMPERATURE_LOW, ACQUATIC_NONE),
    "windswept_hills": (ROUGHNESS_MID, TEMPERATURE_LOW, ACQUATIC_NONE),
    "windswept_gravelly_hills": (
        ROUGHNESS_MID,
        TEMPERATURE_LOW,
        ACQUATIC_NONE,
    ),
    "windswept_forest": (ROUGHNESS_MID, TEMPERATURE_LOW, ACQUATIC_NONE),
    **snowy,
}

dark_oak = {
    "swamp": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_SMALL_BODY),
    **badlands,
}

acacia = {
    "savanna": (ROUGHNESS_MID, TEMPERATURE_HIGH, ACQUATIC_SMALL_BODY),
    "savanna_plateau": (ROUGHNESS_MID, TEMPERATURE_HIGH, ACQUATIC_SMALL_BODY),
    "windswept_savanna": (
        ROUGHNESS_HIGH,
        TEMPERATURE_HIGH,
        ACQUATIC_SMALL_BODY,
    ),
    **badlands,
}

jungle = {
    "jungle": (ROUGHNESS_MID, TEMPERATURE_HIGH, ACQUATIC_NONE),
    "sparse_jungle": (ROUGHNESS_LOW, TEMPERATURE_HIGH, ACQUATIC_NONE),
    "bamboo_jungle": (ROUGHNESS_MID, TEMPERATURE_HIGH, ACQUATIC_NONE),
}

common_animal_spawners = {}
for biome in all_biomes:
    if (
        biome in desert
        or biome in badlands
        or biome in shore
        or biome in snowy
        or biome in aquatic
        or biome == "mushroom_fields"
    ):
        continue
    common_animal_spawners[biome] = all_biomes[biome]

horse_spawners = {
    "plains": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_NONE),
    "sunflower_plains": (ROUGHNESS_LOW, TEMPERATURE_MID, ACQUATIC_NONE),
    "savanna": (ROUGHNESS_MID, TEMPERATURE_HIGH, ACQUATIC_SMALL_BODY),
    "savanna_plateau": (ROUGHNESS_MID, TEMPERATURE_HIGH, ACQUATIC_SMALL_BODY),
    "windswept_savanna": (
        ROUGHNESS_HIGH,
        TEMPERATURE_HIGH,
        ACQUATIC_SMALL_BODY,
    ),
}

tag_map = {
    "all_biomes": all_biomes,
    "plains": plains,
    "snowy": snowy,
    "cold": cold,
    "desert": desert,
    "swamp": swamp,
    "badlands": badlands,
    "ocean": ocean,
    "aquatic": aquatic,
    "shore": shore,
    "forest": forest,
    "rocky": rocky,
    "oak": oak,
    "birch": birch,
    "spruce": spruce,
    "dark_oak": dark_oak,
    "acacia": acacia,
    "jungle": jungle,
    "horse_spawners": horse_spawners,
    "common_animal_spawners": common_animal_spawners,
}

if __name__ == "__main__":
    print(all_biomes)

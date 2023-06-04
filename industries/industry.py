import sys
sys.path[0] = sys.path[0].removesuffix('\\industries')

import random
from data.asset import Asset, asset_defaults
from gdpc.editor import Editor
from districts.district import District
from industries import biomes

class Industry(Asset):
    pass

@asset_defaults(
    parent_industries = None
)
class PrimaryIndustry(Industry):
    required_tags : list[str]

@asset_defaults(
    required_tags = None
)
class SecondaryIndustry(Industry):
    parent_industries : list[str]

def get_district_biomes(editor, district, num_points = 3):
    biomes_in_district = []
    for point in random.sample(list(district.points), num_points):
        biomes_in_district.append(editor.getBiome(point)[10:])
    return list(set(biomes_in_district))

def get_primary_industries(district_biomes : list[str]):
    eligibile_primary_industries = []
    for industry in PrimaryIndustry.all():
        industry : PrimaryIndustry
                
        if any((biome in district_biomes for biome in biomes.tag_map[industry.required_tags[0]])):
            eligibile_primary_industries.append(industry)
    return eligibile_primary_industries

def find_secondary_industries(district_primary_industries : list[str]):
    eligible_secondary_industries = []
    for industry in SecondaryIndustry.all():
        industry : SecondaryIndustry

        if any((primary not in district_primary_industries for primary in industry.parent_industries)):
            continue
        eligible_secondary_industries.append(industry)
    return eligible_secondary_industries
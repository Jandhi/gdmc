import sys

from nbtlib import nbt, serialize_tag
from ..structure import Structure
from gdpc.block import Block
from gdpc.vector_tools import ivec3


# Converts an nbt file into a more legible Structure object
def convert_nbt(filename: str) -> Structure:
    file = nbt.load(sys.path[0] + "/" + filename)
    blocks, dimensions = __read_blocks_and_dimensions(file["blocks"])
    entities = __read_entities(file["entities"])
    palette = []

    for tag in file["palette"]:
        name = ""
        properties = {}

        if "Name" in tag:
            name = str(tag["Name"])

        if "Properties" in tag:
            properties = __read_properties(tag)

        palette.append(Block(id=name, states=properties))
    return Structure(blocks, entities, palette, dimensions)


def __read_entities(tag):
    entities = {}
    for entity in tag:
        id = entity["nbt"]["id"]
        x, y, z = (int(i) for i in entity["blockPos"])
        try:
            # removing uuid so minecraft can populate this itself when summoning entity, error occurs when summoning two entities with same uuid
            entity["nbt"].pop("UUID")
            nbt = serialize_tag(entity["nbt"])
        except:
            nbt = None
        entities[ivec3(x, y, z)] = [id, nbt]
    return entities


def __read_blocks_and_dimensions(tag) -> dict:
    blocks = {}
    minimums = [0, 0, 0]
    maximums = [0, 0, 0]

    for block in tag:
        x, y, z = (int(i) for i in block["pos"])
        state = block["state"]
        try:
            nbt = serialize_tag(block["nbt"])
        except:
            nbt = None

        blocks[ivec3(x, y, z)] = [int(state), nbt]

        for val, index in ((x, 0), (y, 1), (z, 2)):
            if val < minimums[index]:
                minimums[index] = val
            if val > maximums[index]:
                maximums[index] = val

    dimensions = ivec3(*(maximums[i] - minimums[i] for i in range(3)))

    return blocks, dimensions


def __read_properties(tag) -> dict:
    properties = {}

    for property in tag["Properties"]:
        pname = str(property)
        properties[pname] = str(tag["Properties"][pname])

    return properties

import os
import json
from glob import glob

def load_jsons(directory_path : str) -> list[dict]:
    names = glob(directory_path + '/**/*.json', recursive=True) # glob allows us to get the subfolders too

    jsons = []

    for name in names:
        with open(name, 'r') as file:
            data = json.load(file)
            jsons.append(data)

    return jsons

def load_objects(directory_path : str, cls : type) -> list[any]:
    objects = []

    for json in load_jsons(directory_path):
        obj = cls.construct(**json)

        if obj is not None:
            objects.append(obj)
    
    return objects
import json
from glob import glob
from typing import Any


def load_jsons(directory_path: str) -> list[dict]:
    names = glob(f"{directory_path}/**/*.json", recursive=True)

    jsons = []

    for name in names:
        with open(name, "r") as file:
            data = json.load(file)
            jsons.append(data)

    return jsons
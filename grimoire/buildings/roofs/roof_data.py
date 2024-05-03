from dataclasses import dataclass


@dataclass
class RoofData:
    top_right_component: str
    top_left_component: str
    bottom_right_component: str
    bottom_left_component: str

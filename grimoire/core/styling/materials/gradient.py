import abc
import dataclasses

from gdpc.vector_tools import DIRECTIONS_3D
from glm import ivec3, vec3

from perlin_noise import PerlinNoise
from grimoire.core.structures.axis import Axis, Axes
from grimoire.core.utils.bounds import clamp
from grimoire.core.utils.misc import average, lerp


@dataclasses.dataclass
class PerlinSettings:
    base_octaves: float
    noise_layers: int
    # The ratio of how fast the higher perlin octaves fall off
    add_ratio: float
    # The amount that the perlin is reflected with in the final result
    strength: float


@dataclasses.dataclass
class GradientAxis:
    axis: Axis
    min_val: int
    max_val: int

    def find_gradient_value(self, pos: ivec3) -> float:
        base_val = self.axis.get(pos)
        grad_val = (base_val - self.min_val) / (self.max_val - self.min_val)
        return clamp(grad_val, 0.0, 1.0)

    @staticmethod
    def x(min_val, max_val) -> "GradientAxis":
        return GradientAxis(Axes.X, min_val, max_val)

    @staticmethod
    def y(min_val, max_val) -> "GradientAxis":
        return GradientAxis(Axes.Y, min_val, max_val)

    @staticmethod
    def z(min_val, max_val) -> "GradientAxis":
        return GradientAxis(Axes.Z, min_val, max_val)


class Gradient:
    default_perlin_settings = PerlinSettings(
        base_octaves=27, noise_layers=6, add_ratio=1.7, strength=0.3
    )

    def __init__(
        self,
        seed,
        perlin_settings: PerlinSettings = None,
    ):
        self.axes = []

        if perlin_settings is None:
            perlin_settings = Gradient.default_perlin_settings

        self.perlin_settings = perlin_settings

        self.noises = [
            PerlinNoise(octaves=self.perlin_settings.base_octaves * 2**i, seed=seed)
            for i in range(self.perlin_settings.noise_layers)
        ]

    # Builder pattern to add axes to the gradient
    def with_axis(self, axis: GradientAxis) -> "Gradient":
        self.axes.append(axis)
        return self

    # Calculates the gradient value without perlin noise
    def calculate_gradient_value(self, pos: ivec3) -> float:
        if len(self.axes) == 0:
            return 0.5

        return average([axis.find_gradient_value(pos) for axis in self.axes])

    # We average the value across its orthogonal neighbours
    def calculate_value(self, pos: ivec3, grad_val: float = None):
        return average(
            [
                self.calculate_point_value(pos + d, grad_val)
                for d in {ivec3(0, 0, 0)} | DIRECTIONS_3D
            ]
        )

    # Make a vec appear between 0 and 1
    def normalize_vec(self, vec: ivec3) -> vec3:
        return vec3(
            float(vec.x) / 256.0,
            float(vec.y) / 256.0,
            float(vec.z) / 256.0,
        )

    def calculate_point_value(self, pos: ivec3, grad_val: float = None):
        perlin_val = 0.5 + sum(
            self.noises[i](list(self.normalize_vec(pos)))
            / (self.perlin_settings.add_ratio**i)
            for i in range(self.perlin_settings.noise_layers)
        )

        grad_val = (
            grad_val if grad_val is not None else self.calculate_gradient_value(pos)
        )

        return clamp(
            lerp(grad_val, perlin_val, self.perlin_settings.strength),
            0.0,
            1.0,
        )

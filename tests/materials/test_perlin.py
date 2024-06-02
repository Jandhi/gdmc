# Allows code to be run in root directory
import sys

sys.path[0] = sys.path[0].removesuffix("tests\\materials")

from perlin_noise import PerlinNoise

noise = PerlinNoise(octaves=3.5, seed=13)

while True:
    value = input()
    print(noise(float(value)))

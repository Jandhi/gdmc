import random

from glm import ivec2
from matplotlib import pyplot as plt
from numpy import zeros, uint8

from core.noise.gradient_noise import get_gradient_noise

# tests if the gradient noise function ever outputs outside 0 to 1
def min_max_test():
    min = .5
    max = .5
    rand = random.Random(1234)
    for x in range(1000):
        for z in range(1000):
            n = get_gradient_noise(ivec2(rand.randint(-6576381, 13779), rand.randint(-1237123,437327)), 4.0)
            if n < min:
                min = n
            if n > max:
                max = n

    print (min, max)

# visualizes using pyplot
def visualize():
    SIZE = 100
    nmap = zeros((SIZE, SIZE))

    for x in range(0, SIZE):
        for z in range(0, SIZE):
            val = get_gradient_noise(ivec2(x, z), 4.0)
            nmap[x, z] = val

    print(nmap.min(), nmap.max(), nmap.mean())

    # normalize the nmap to the range [0, 255]
    nmap = (nmap - nmap.min()) * 255 / (nmap.max() - nmap.min())
    nmap = nmap.clip(0, 255).astype(uint8)

    plt.imshow(nmap, cmap='gray')
    plt.show()

visualize()
# from https://gist.github.com/robweychert/7efa6a5f762207245646b16f29dd6671

import math


def ease_in(t: float, exponential: float = 1) -> float:
    return t**exponential


def ease_out(t: float, exponential: float) -> float:
    return 1 - (1 - t) ** exponential


def ease_in_out(t: float, exponential: float) -> float:
    return ease_in(t, exponential) if t < 0.5 else ease_out(t, exponential)


def ease_in_sine(t: float) -> float:
    return -math.cos(t * math.pi / 2) + 1


def ease_out_sine(t: float) -> float:
    return math.sin(t * math.pi / 2)


def ease_in_out_sine(t: float) -> float:
    return -(math.cos(math.pi * t) - 1) / 2


def ease_in_expo(t: float) -> float:
    return math.pow(2, 10 * (t - 1))


def ease_out_expo(t: float) -> float:
    return -math.pow(2, -10 * t) + 1


def ease_in_out_expo(t: float) -> float:
    t *= 2
    if t < 1:
        return math.pow(2, 10 * (t - 1)) / 2
    else:
        t -= 1
        return -math.pow(2, -10 * t) - 1


def ease_in_circ(t: float) -> float:
    return 1 - math.sqrt(1 - t * t)


def ease_out_circ(t: float) -> float:
    t -= 1
    return math.sqrt(1 - t * t)


def ease_in_out_circ(t: float) -> float:
    t *= 2
    if t < 1:
        return -(math.sqrt(1 - t * t) - 1) / 2
    else:
        t -= 2
        return (math.sqrt(1 - t * t) + 1) / 2

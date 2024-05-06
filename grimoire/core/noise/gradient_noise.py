from glm import floor, vec2
from gdpc import vector_tools as vt

from .hash import hash22


def dot(v1: vt.vec2, v2: vt.vec2):
    return v1.x * v2.x + v1.y * v2.y

# returns a value between 0 and 1
def get_gradient_noise(pos: vec2, grid_size: float) -> float:
    p = vt.vec2(pos.x, pos.y) / (grid_size + 0.001)

    i = vt.vec2(floor(p.x), floor(p.y))
    f = p - i

    c00 = hash22(i)
    c10 = hash22(i + vt.vec2(1, 0))
    c01 = hash22(i + vt.vec2(0, 1))
    c11 = hash22(i + vt.vec2(1, 1))

    u = f * f * f * (f * (f * 6 - 15) + 10)

    d00 = dot(c00, f)
    d10 = dot(c10, f - vt.vec2(1, 0))
    d01 = dot(c01, f - vt.vec2(0, 1))
    d11 = dot(c11, f - vt.vec2(1, 1))

    return .5 + .5*(d00 + u.x * (d10 - d00) + u.y * (d01 - d00) + u.x * u.y * (d00 - d10 - d01 + d11))
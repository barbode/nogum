import math


def get_distance(pos, center, scale):
    return math.sqrt(((pos[0]-center[0]) / scale[0])**2 + ((pos[1]-center[1]) / scale[1])**2)

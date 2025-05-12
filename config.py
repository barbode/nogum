import pygame
from colors import *

screen_size = (1310, 690)
speed = 0.25
xy_scale = (2, 1)
scale_factor = 32
rotation = 30

# assets
font_path = './assets/Vazirmatn-VariableFont_wght.ttf'


def load_image(name: str, scale: tuple[float]):
    img = pygame.image.load(f"assets/{name}.png")
    img = pygame.transform.scale(img, scale)
    return img


bg_image = load_image("background", screen_size)

planets = [
    # 0
    {"name": "sun",
     "surface": load_image("eps-sun", (100, 90)),
     "distance": 0, "speed": 0.0, "angle": 0},
    # 1
    {"name": "mercury",
     "surface": load_image("eps-mercury", (25, 25)),
     "distance": 2, "speed": 2.83, "angle": 43.72},
    # 2
    {"name": "venus",
     "surface": load_image("eps-venus", (30, 30)),
     "distance": 3, "speed": 1.54, "angle": 120.02},
    # 3 - reference speed
    {"name": "earth",
     "surface": load_image("eps-earth", (45, 35)),
     "distance": 4, "speed": 1.00, "angle": 222.18},
    # 4
    {"name": "mars",
     "surface": load_image("eps-mars", (35, 35)),
     "distance": 5, "speed": 0.72, "angle": 251.46},
    # 5
    {"name": "jupiter",
     "surface": load_image("eps-jupiter", (50, 50)),
     "distance": 6, "speed": 0.54, "angle": 293.78},
    # 6
    {"name": "saturn",
     "surface": load_image("eps-saturn", (60, 40)),
     "distance": 7, "speed": 0.43, "angle": 358.00},
    # 7
    {"name": "uranus",
     "surface": load_image("eps-uranus", (30, 30)),
     "distance": 8, "speed": 0.35, "angle": 356.99},
    # 8
    {"name": "neptune",
     "surface": load_image("eps-neptune", (25, 25)),
     "distance": 9, "speed": 0.30, "angle": 31.43}
]

# details box
details_box = pygame.Surface((320, screen_size[1]), pygame.SRCALPHA)
details_box.fill(darker)

import pygame

screen_size = (1310, 690)
speed = 0.25
xy_scale = (2, 1)
scale_factor = 30
rotation = 30


def load_image(name: str, scale: tuple[float]):
    img = pygame.image.load(f"assets/{name}.png")
    img = pygame.transform.scale(img, scale)
    return img


bg_image = load_image("background", screen_size)

planets = [
    # 0
    {"surface": load_image("eps-sun", (100, 90)),
     "distance": 0, "angle": 0},
    # 1
    {"surface": load_image("eps-mercury", (25, 25)),
     "distance": 2, "angle": 0},
    # 2
    {"surface": load_image("eps-venus", (30, 30)),
     "distance": 3, "angle": 0},
    # 3
    {"surface": load_image("eps-earth", (45, 35)),
     "distance": 4, "angle": 0},
    # 4
    {"surface": load_image("eps-mars", (35, 35)),
     "distance": 5, "angle": 0},
    # 5
    {"surface": load_image("eps-jupiter", (50, 50)),
     "distance": 6, "angle": 0},
    # 6
    {"surface": load_image("eps-saturn", (60, 40)),
     "distance": 7, "angle": 0},
    # 7
    {"surface": load_image("eps-uranus", (30, 30)),
     "distance": 8, "angle": 0},
    # 8
    {"surface": load_image("eps-neptune", (25, 25)),
     "distance": 9, "angle": 0}
]

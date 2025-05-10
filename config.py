import pygame

screen_size = (1310, 690)


def load_image(name: str, scale: tuple[float]):
    img = pygame.image.load(f"assets/{name}.png")
    img = pygame.transform.scale(img, scale)
    return img


bg_image = {"surface": load_image("background", screen_size),
            "position": (0, 0), "angle": 0}

planets = [
    # 0
    {"surface": load_image("eps-sun", (100, 90)),
     "position": (612, 266), "angle": 0},
    # 1
    {"surface": load_image("eps-mercury", (25, 25)),
     "position": (750, 274), "angle": 0},
    # 2
    {"surface": load_image("eps-venus", (30, 30)),
     "position": (830, 294), "angle": 0},
    # 3
    {"surface": load_image("eps-earth", (45, 35)),
     "position": (900, 320), "angle": 0},
    # 4
    {"surface": load_image("eps-mars", (35, 35)),
     "position": (970, 350), "angle": 0},
    # 5
    {"surface": load_image("eps-jupiter", (50, 50)),
     "position": (1000, 400), "angle": 0},
    # 6
    {"surface": load_image("eps-saturn", (60, 40)),
     "position": (1000, 490), "angle": 0},
    # 7
    {"surface": load_image("eps-uranus", (30, 30)),
     "position": (1010, 560), "angle": 0},
    # 8
    {"surface": load_image("eps-neptune", (25, 25)),
     "position": (1000, 640), "angle": 0}
]

arc_lines = [
    (540, 250, 240, 120),
    (470, 210, 380, 200),
    (400, 170, 530, 290),
    (330, 125, 670, 390),
    (280, 80, 780, 490),
    (220, 40, 900, 580),
    (170, 0, 1010, 670),
    (100, -40, 1150, 760)
]

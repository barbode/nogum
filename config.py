import pygame

screen_size = (1200, 680)


def load_image(name: str, scale: tuple[float]):
    img = pygame.image.load(f"assets/{name}.png")
    img = pygame.transform.scale(img, scale)
    return img


images = [
    # 0
    {"surface": load_image("background", screen_size),
     "position": (0, 0), "angle": 0},
    # 1
    {"surface": load_image("eps-sun", (120, 110)),
     "position": (600, 264), "angle": 0},
    # 2
    {"surface": load_image("eps-mercury", (40, 40)),
     "position": (750, 274), "angle": 0},
    # 3
    {"surface": load_image("eps-venus", (45, 45)),
     "position": (830, 294), "angle": 0},
    # 4
    {"surface": load_image("eps-earth", (60, 50)),
     "position": (920, 340), "angle": 0},
    # 5
    {"surface": load_image("eps-mars", (50, 50)),
     "position": (1020, 410), "angle": 0},
    # 6
    {"surface": load_image("eps-jupiter", (65, 65)),
     "position": (1060, 490), "angle": 0},
    # 7
    {"surface": load_image("eps-saturn", (75, 55)),
     "position": (940, 570), "angle": 0},
    # 8
    {"surface": load_image("eps-uranus", (45, 45)),
     "position": (800, 580), "angle": 0},
    # 9
    {"surface": load_image("eps-neptune", (40, 40)),
     "position": (630, 560), "angle": 0}
]

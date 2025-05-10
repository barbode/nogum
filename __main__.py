import pygame
import sys
from colors import *
from calculations import *
from config import *
import math


# مقداردهی اولیه Pygame
pygame.init()

# تنظیمات پنجره
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Solar System")

clock = pygame.time.Clock()
dt = 0

# Game loop

while True:
    dt += clock.get_time() * 0.001 * speed

    # exit game on quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # clear screen - white
    screen.fill(white)

    surfaces = move_everything()

    # draw background image
    screen.blit(bg_image, (0, 0))

    mid_screen = (screen_size[0]/2, screen_size[1]/2)

    # draw planets
    for planet in planets:
        surface: pygame.Surface = planet["surface"]
        distance: float = planet["distance"] * scale_factor

        # draw arc line
        arc_size = (distance * xy_scale[0] * 2,
                    distance * xy_scale[1] * 2)
        arc_left_top = (mid_screen[0] - arc_size[0]/2,
                        mid_screen[1] - arc_size[1]/2)
        arc_line = (arc_left_top, arc_size)
        pygame.draw.arc(screen, white_faded, arc_line, 0, 180, 1)

        # draw planet
        mid_planet = (surface.get_width()/2, surface.get_height()/2)
        mid = (mid_screen[0] - mid_planet[0],  mid_screen[1] - mid_planet[1])
        planet_xy = (distance * xy_scale[0] * math.sin(dt),
                     distance * xy_scale[1] * math.cos(dt))
        position = (mid[0] + planet_xy[0], mid[1] + planet_xy[1])
        screen.blit(surface, position)

    # به‌روزرسانی نمایش
    pygame.display.flip()

    # تنظیم فریم‌ریت
    clock.tick(60)

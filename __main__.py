import pygame
import sys
from colors import *
from config import *
from calc import *
import math


# مقداردهی اولیه Pygame
pygame.init()

font_title = pygame.font.Font(font_path, 36)
font_title.set_script("Arab")


# تنظیمات پنجره
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Solar System")

# variables
selected_planet = -1
clock = pygame.time.Clock()
dt = 0  # initial time


mid_screen = (screen_size[0]/2, screen_size[1]/2)

# Game loop

while True:
    dt += clock.get_time() * 0.001 * speed

    # exit game on quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            selected_planet = -1
            for planet in planets:
                click_distance = (planet["distance"]
                                  * scale_factor) + scale_factor/2
                if get_distance(event.pos, mid_screen, xy_scale) < click_distance:
                    print(f"Surface clicked! {planet["name"]}")
                    selected_planet = planets.index(planet)
                    break

    # clear screen - white
    screen.fill(white)

    # draw background image
    screen.blit(bg_image, (0, 0))

    # title
    text = font_title.render('منظومه شمسی'[::-1], True, white)
    screen.blit(text, (screen_size[0] - 270, 12))

    # subtitle
    # TODO ...

    # draw planets
    for planet in planets:
        index = planets.index(planet)
        angle: float = planet["angle"]
        speed: float = planet["speed"]
        surface: pygame.Surface = planet["surface"]
        distance: float = planet["distance"] * scale_factor

        # draw arc line
        arc_size = (distance * xy_scale[0] * 2,
                    distance * xy_scale[1] * 2)
        arc_left_top = (mid_screen[0] - arc_size[0]/2,
                        mid_screen[1] - arc_size[1]/2)
        arc_line = (arc_left_top, arc_size)
        pygame.draw.arc(screen, grey, arc_line, 0, 180, 1)

        # draw planet
        mid_planet = (surface.get_width()/2, surface.get_height()/2)
        mid = (mid_screen[0] - mid_planet[0],  mid_screen[1] - mid_planet[1])
        theta = speed * (dt + angle)
        planet_xy = (distance * xy_scale[0] * math.sin(theta),
                     distance * xy_scale[1] * math.cos(theta))
        position = (mid[0] + planet_xy[0], mid[1] + planet_xy[1])
        screen.blit(surface, position)

    # draw details
    if selected_planet > -1:
        screen.blit(details_box, (0, 0))  # draw the faded rectangle

    # به‌روزرسانی نمایش
    pygame.display.flip()

    # تنظیم فریم‌ریت
    clock.tick(60)

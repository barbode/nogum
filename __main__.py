import pygame
import sys
from colors import *
from calculations import *
from config import *


# مقداردهی اولیه Pygame
pygame.init()

# تنظیمات پنجره
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Solar System")

clock = pygame.time.Clock()


# Game loop

while True:
    # exit game on quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # clear screen - white
    screen.fill(white)

    surfaces = move_everything()

    # draw bg image
    screen.blit(bg_image["surface"], bg_image["position"])

    # draw arc lines
    for arc_line in arc_lines:
        pygame.draw.arc(screen, white_faded, arc_line, 0, 180, 1)

    # draw planets
    for planet in planets:
        surface: pygame.Surface = planet["surface"]
        position: tuple[float] = planet["position"]
        screen.blit(surface, position)

    # به‌روزرسانی نمایش
    pygame.display.flip()

    # تنظیم فریم‌ریت
    clock.tick(60)

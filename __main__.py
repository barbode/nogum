import pygame
import sys
from colors import white
from calculations import *
from config import *


# مقداردهی اولیه Pygame
pygame.init()

# تنظیمات پنجره
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Solar System")

clock = pygame.time.Clock()


# حلقه اصلی بازی
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # پاک کردن صفحه
    screen.fill(white)  # رنگ سفید

    # ellipsis
    pygame.draw.ellipse(
        screen, white, (0, 0, 200, 100))

    surfaces = move_everything()

    # رسم تصویر در موقعیت (x, y)
    for image in images:
        surface: Surface = image["surface"]
        position: tuple[float] = image["position"]
        screen.blit(surface, position)

    # به‌روزرسانی نمایش
    pygame.display.flip()

    # تنظیم فریم‌ریت
    clock.tick(60)

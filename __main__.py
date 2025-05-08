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


# حلقه اصلی بازی
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # پاک کردن صفحه
    screen.fill(white)  # رنگ سفید

    
    
    surfaces = move_everything()

    # رسم تصویر در موقعیت (x, y)
    for image in images:
        surface: Surface = image["surface"]
        position: tuple[float] = image["position"]
        screen.blit(surface, position)

    pygame.draw.arc(screen, white, (540, 250, 240, 120), 0, 180, 1)
    pygame.draw.arc(screen, white, (470, 210, 380, 200), 0, 180, 1)
    pygame.draw.arc(screen, white, (400, 170, 530, 290), 0, 180, 1)
    pygame.draw.arc(screen, white, (330, 125, 670, 390), 0, 180, 1)
    pygame.draw.arc(screen, white, (280, 80, 780, 490), 0, 180, 1)
    pygame.draw.arc(screen, white, (220, 40, 900, 580), 0, 180, 1)
    pygame.draw.arc(screen, white, (170, 0, 1010, 670), 0, 180, 1)
    pygame.draw.arc(screen, white, (100, -40, 1150, 760), 0, 180, 1)
    
    # به‌روزرسانی نمایش
    pygame.display.flip()

    # تنظیم فریم‌ریت
    clock.tick(60)

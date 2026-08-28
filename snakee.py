import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Меню игры")

font = pygame.font.SysFont("bahnschrift", 30)

btn_play = pygame.Rect(300, 200, 200, 50)
btn_settings = pygame.Rect(300, 280, 200, 50)
btn_exit = pygame.Rect(300, 360, 200, 50)

COLOR_BTN = (50, 153, 213)
COLOR_TEXT = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if btn_exit.collidepoint(event.pos):
                    running = False

    screen.fill((30, 30, 30))

    pygame.draw.rect(screen, COLOR_BTN, btn_play)
    text_play = font.render("ИГРАТЬ", True, COLOR_TEXT)
    screen.blit(text_play, text_play.get_rect(center=btn_play.center))

    pygame.draw.rect(screen, COLOR_BTN, btn_settings)
    text_settings = font.render("НАСТРОЙКИ", True, COLOR_TEXT)
    screen.blit(text_settings, text_settings.get_rect(center=btn_settings.center))

    pygame.draw.rect(screen, COLOR_BTN, btn_exit)
    text_exit = font.render("ВЫЙТИ", True, COLOR_TEXT)
    screen.blit(text_exit, text_exit.get_rect(center=btn_exit.center))

    pygame.display.update()

pygame.quit()
sys.exit()

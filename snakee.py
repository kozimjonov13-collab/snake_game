import pygame
import sys
import os

pygame.init()
pygame.mixer.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Funny snake game")

def play_music(music_filename):
    if not os.path.exists(music_filename):
        print(f"Предупреждение: Файл '{music_filename}' не найден.")
        return
    try:
        pygame.mixer.music.load(music_filename)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    except pygame.error as e:
        print(f"Ошибка при загрузке музыки: {e}")

play_music("Caketown 1.mp3")

font_title = pygame.font.SysFont("bahnschrift", 50, bold=True)
font_btn = pygame.font.SysFont("bahnschrift", 30)

btn_play = pygame.Rect(300, 250, 200, 50)
btn_settings = pygame.Rect(300, 330, 200, 50)
btn_exit = pygame.Rect(300, 410, 200, 50)

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

    title_text = font_title.render("FUNNY SNAKE GAME", True, (46, 204, 113))
    title_rect = title_text.get_rect(center=(WIDTH // 2, 120))
    screen.blit(title_text, title_rect)

    pygame.draw.rect(screen, COLOR_BTN, btn_play)
    text_play = font_btn.render("ИГРАТЬ", True, COLOR_TEXT)
    screen.blit(text_play, text_play.get_rect(center=btn_play.center))

    pygame.draw.rect(screen, COLOR_BTN, btn_settings)
    text_settings = font_btn.render("НАСТРОЙКИ", True, COLOR_TEXT)
    screen.blit(text_settings, text_settings.get_rect(center=btn_settings.center))

    pygame.draw.rect(screen, COLOR_BTN, btn_exit)
    text_exit = font_btn.render("ВЫЙТИ", True, COLOR_TEXT)
    screen.blit(text_exit, text_exit.get_rect(center=btn_exit.center))

    pygame.display.update()

pygame.quit()
sys.exit()

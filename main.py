# Setup Python ----------------------------------------------- #
from game_screen import game
import pygame
import pygame_widgets
from pygame_widgets.button import Button
import sys
import os
from game_won_screen import game_won

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Circle Clicker')
screen = pygame.display.set_mode((1280, 720))

# Game colours ---------------------------------------- #
GAME_BACKGROUND_CLR = (17, 24, 39)

# Buttons
GAME_BUTTON_CLR = (55, 65, 81)
GAME_BUTTON_HOVER_CLR = (75, 85, 99)
GAME_BUTTON_FONT_CLR = (229, 231, 235)
GAME_FONT_CLR = (243, 244, 246)

font = pygame.font.SysFont(os.path.join("assets", 'gamefont.ttf'), 70)
subtitle = pygame.font.SysFont(os.path.join("assets", 'gamefont.ttf'), 30)


def draw_text(text, fontToRender, color, surface, x, y):
    textobj = fontToRender.render(text, 1, color)
    text_rect = textobj.get_rect(center=(1280//2, y))
    surface.blit(textobj, text_rect)


click = False


def main_menu():
    while True:
        screen.fill(GAME_BACKGROUND_CLR)

        draw_text('Circle Clicker', font, (255, 255, 255), screen, 10, 240)
        Button(
            screen, 520, 300, 250, 50,
            text="Start Game",
            textColour=GAME_BUTTON_FONT_CLR,
            fontSize=35, margin=5,
            inactiveColour=GAME_BUTTON_CLR,
            hoverColour=GAME_BUTTON_HOVER_CLR,
            pressedColour=GAME_BUTTON_CLR,
            radius=8,
            onClick=lambda: game(screen)
        )
        draw_text('Created by Nicola', subtitle,
                  (255, 255, 255), screen, 10, 680)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame_widgets.update(event)
        pygame.display.update()
        mainClock.tick(60)


def options():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('options', font, (255, 255, 255), screen, 20, 10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


main_menu()

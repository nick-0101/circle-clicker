# Setup Python ----------------------------------------------- #
import os
import sys

import pygame

# from main import main_menu

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Circle Clicker - Game Over')
screen = pygame.display.set_mode((1280, 720))

# Game colours ---------------------------------------- #
GAME_BACKGROUND_CLR = (17, 24, 39)

# Buttons
GAME_BUTTON_CLR = (55, 65, 81)
GAME_BUTTON_HOVER_CLR = (75, 85, 99)
GAME_BUTTON_FONT_CLR = (229, 231, 235)
GAME_FONT_CLR = (243, 244, 246)

font = pygame.font.SysFont(os.path.join("assets", 'gamefont.ttf'), 70)
subtitle = pygame.font.SysFont(os.path.join("assets", 'gamefont.ttf'), 50)
button = pygame.font.SysFont(os.path.join("assets", 'gamefont.ttf'), 35)


def draw_text(text, fontToRender, color, surface, x, y):
    textobj = fontToRender.render(text, 1, color)
    text_rect = textobj.get_rect(center=(1280//2, y))
    surface.blit(textobj, text_rect)


def game_over(player_level, player_highscore, player_timeInGame):
    # Resolves circular import
    from game_screen import game

    while True:
        screen.fill(GAME_BACKGROUND_CLR)
        draw_text('Game over:', font, (255, 255, 255), screen, 10, 150)
        draw_text('Time: {0} seconds'.format(player_timeInGame),
                  subtitle, (255, 255, 255), screen, 10, 210)
        draw_text('Level: {0}'.format(player_level),
                  subtitle, (255, 255, 255), screen, 10, 250)
        draw_text('Highscore: {0}'.format(player_highscore),
                  subtitle, (255, 255, 255), screen, 10, 290)

        text = button.render('Restart Game', True, GAME_BUTTON_FONT_CLR)

        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()

        # if mouse is hovered on a button it
        # changes to lighter shade
        if 1140/2 <= mouse[0] <= 1140/2+140 and 720/2 <= mouse[1] <= 720/2+40:
            pygame.draw.rect(screen, GAME_BUTTON_HOVER_CLR,
                             [1080/2, 690/2, 210, 50])

        else:
            pygame.draw.rect(screen, GAME_BUTTON_CLR, [
                             1080/2, 690/2, 210, 50])

        # superimposing the text onto our button
        screen.blit(text, (1135/2, 720/2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                game(screen)

        pygame.display.update()
        mainClock.tick(100)

# Setup Python ----------------------------------------------- #
import pygame
import pygame_widgets
from pygame_widgets.button import Button
import sys
import os
import random
from game_over_screen import game_over
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

# Levels
LEVEL_1 = (0, 255, 0)
LEVEL_2 = (191, 255, 0)
LEVEL_3 = (255, 204, 0)
LEVEL_4 = (255, 111, 0)
LEVEL_5 = (255, 47, 0)
LEVEL_6 = (255, 0, 111)
LEVEL_7 = (255, 0, 221)
LEVEL_8 = (166, 0, 255)
LEVEL_9 = (255, 255, 255)
LEVEL_10 = (0, 0, 0)


class Player(object):
    def __init__(self, score, level, ttc, timeInGame):
        self.score = score
        self.level = level
        self.timeToClick = ttc
        self.timeInGame = timeInGame

    def setTimeInGame(self, timeInGame):
        self.timeInGame = timeInGame

    def getTimeInGame(self):
        return self.timeInGame

    def setTTC(self, ttc):
        self.timeToClick = ttc

    def getTTC(self):
        return self.timeToClick

    def setLevel(self, level):
        self.level = level

    def getLevel(self):
        return self.level

    def setScore(self, score):
        self.score = score

    def getScore(self):
        return self.score


class GameObject(object):
    def __init__(self, colour, radius):
        self.pos = [random.randint(0, 1280), random.randint(0, 650)]
        self.colour = colour
        self.radius = radius

        self.circle_rect = 0

    def draw(self):
        circle_rect = pygame.draw.circle(
            screen, self.colour, (self.pos[0], self.pos[1]), self.radius)

        self.circle_rect = circle_rect


# Text
font = pygame.font.SysFont(os.path.join("assets", 'gamefont.ttf'), 25)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    text_rect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, text_rect)


# #
# Player
# #
def updateScore(player):
    player_score = player.getScore()
    player.setScore(player_score + 1)

    # Update score
    player_score = player.getScore()
    draw_text(str(player_score), font, (255, 255, 255), screen, 1250, 20)


def updateLevel(player):
    player_level = player.getLevel()
    player.setLevel(player_level + 1)

    # Update level
    player_level = player.getLevel()
    draw_text(str(player_level), font, (255, 255, 255), screen, 60, 20)

    return player_level


def updateTimer(player):
    player_timeToClick = player.getTTC()

    if player_timeToClick >= 0:
        player.setTTC(player_timeToClick - 1)

        # Update timer
        player_timeToClick = player.getTTC() / 100
        draw_text('Countdown: {0}'.format(player_timeToClick),
                  font, (255, 255, 255), screen, 640, 20)

    else:
        draw_text('Countdown: 0.00',
                  font, (255, 255, 255), screen, 640, 20)

    return player_timeToClick


def updateTimeInGame(player):
    player_timeInGame = player.getTimeInGame()
    player.setTimeInGame(player_timeInGame + 1)

    return player_timeInGame / 100


# #
# Level objects
# #
def generateLevel(circles, amountOfCircles, colour, radius, ttc, player):
    # Generate circles
    for i in range(amountOfCircles):
        circles.append(GameObject(colour, radius))

    # Set timer
    player.setTTC(ttc)

# Main game function


def game(screen):
    running = True

    player = Player(0, 1, 2000, 0000)
    circles = []

    # Create first level
    generateLevel(circles, 10, LEVEL_1, 20, 2000, player)

    while running:
        # Draw high score
        player_score = player.getScore()
        screen.fill(GAME_BACKGROUND_CLR)
        draw_text('High score: {0}'.format(player_score),
                  font, (255, 255, 255), screen, 1210, 20)

        # Draw level
        player_level = player.getLevel()
        draw_text('Level: {0}'.format(player_level),
                  font, (255, 255, 255), screen, 40, 20)

        # #
        # Timer logic
        # #
        player_timeToClick = updateTimer(player)
        player_timeInGame = updateTimeInGame(player)

        # Handle timer expiration
        if player_timeToClick <= 0:
            # go to lost screen with game summary
            game_over(player_level, player_score, player_timeInGame)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Holds the circle to remove
                cir_to_remove = []

                for i in range(len(circles)):
                    # If a circle has been clicked on, add it to cir_to_remove
                    if circles[i].circle_rect.collidepoint(event.pos):
                        cir_to_remove.append(circles[i])
                        updateScore(player)

                # Removes all circles in cir_to_remove
                for circle in cir_to_remove:
                    circles.remove(circle)

                # Go to new level
                if not circles:
                    # Go up until level 10
                    if player_level < 10:
                        player_level = updateLevel(player)

                    if player_level == 2:
                        generateLevel(circles, 11, LEVEL_2, 20, 1900, player)
                    elif player_level == 3:
                        generateLevel(11, LEVEL_3, 18, 1800, player)
                    elif player_level == 4:
                        generateLevel(12, LEVEL_4, 16, 1700, player)
                    elif player_level == 5:
                        generateLevel(12, LEVEL_5, 14, 1600, player)
                    elif player_level == 6:
                        generateLevel(13, LEVEL_6, 12, 1500, player)
                    elif player_level == 7:
                        generateLevel(13, LEVEL_7, 10, 1400, player)
                    elif player_level == 8:
                        generateLevel(14, LEVEL_8, 8, 1300, player)
                    elif player_level == 9:
                        generateLevel(14, LEVEL_9, 7, 1200, player)
                    elif player_level == 10:
                        generateLevel(20, LEVEL_10, 6, 1200, player)
                    else:
                        # go to win screen with game summary
                        game_won(player_level, player_score, player_timeInGame)

        # draw circles
        for circle in circles:
            circle.draw()

        pygame.display.update()
        mainClock.tick(100)

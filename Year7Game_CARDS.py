'''Flipping Cards Game - Not with menu'''

# Importing needed libraries
import pygame
import random
import sys

# Initialising pygame
pygame.init()

# Window dimensions
screen_width = 800
screen_height = 600
window = pygame.display.set_mode((screen_width, screen_height))

# Game title
pygame.display.set_caption("Matching Cards - Chinese Numbers")

# Fonts
font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

# Chinese numbers list
chinese_numbers = {1: "yī", 2: "èr", 3: "sān", 4: "sì", 5: "wǔ",
    6: "liù", 7: "qī", 8: "bā", 9: "jiǔ", 10: "shí",
    11: "shí yī", 12: "shí èr", 13: "shí sān", 14: "shí sì", 15: "shí wǔ",
    16: "shí liù", 17: "shí qī", 18: "shí bā", 19: "shí jiǔ", 20: "èr shí"
}


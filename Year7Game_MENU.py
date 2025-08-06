'''Game menu - Leads to Quiz, Card game, and exiting the programe'''

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
pygame.display.set_caption("Learning Chinese Numbers - Game")

# Fonts 
font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()


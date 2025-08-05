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

# Using subset - 6 pairs 
pairs = random.sample(list(chinese_numbers.items()), 6)
cards = []
for num, ch in pairs:
    cards.append((str(num), num))      # English number card
    cards.append((chinese_numbers[num], num))  # Chinese character card
random.shuffle(cards)

# Set up card layout
CARD_WIDTH, CARD_HEIGHT = 120, 80
GRID_ROWS, GRID_COLS = 3, 4
card_rects = []
revealed = [False] * len(cards)
matched = [False] * len(cards)
first_selection = None
pause_time = 0

for i in range(len(cards)):
    row = i // GRID_COLS
    col = i % GRID_COLS
    rect = pygame.Rect(100 + col * (CARD_WIDTH + 20), 100 + row * (CARD_HEIGHT + 20), CARD_WIDTH, CARD_HEIGHT)
    card_rects.append(rect)

def draw_board():
    window.fill((200, 200, 250))
    for i, rect in enumerate(card_rects):
        if matched[i]:
            pygame.draw.rect(window, (200, 255, 200), rect)
        elif revealed[i]:
            pygame.draw.rect(window, (255, 255, 200), rect)
        else:
            pygame.draw.rect(window, (255, 255, 255), rect)

        pygame.draw.rect(window, (0, 0, 0), rect, 2)
        if revealed[i] or matched[i]:
            text = small_font.render(str(cards[i][0]), True, (0, 0, 0))
            text_rect = text.get_rect(center=rect.center)
            window.blit(text, text_rect)

    pygame.display.flip()

running = True
while running:
    draw_board()

    if pause_time > 0 and pygame.time.get_ticks() - pause_time > 1000:
        # Hide cards again if not a match
        if cards[first_selection][1] != cards[second_selection][1]:
            revealed[first_selection] = False
            revealed[second_selection] = False
        else:
            matched[first_selection] = True
            matched[second_selection] = True
        pause_time = 0
        first_selection = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and pause_time == 0:
            for i, rect in enumerate(card_rects):
                if rect.collidepoint(event.pos) and not revealed[i] and not matched[i]:
                    revealed[i] = True
                    if first_selection is None:
                        first_selection = i
                    else:
                        second_selection = i
                        pause_time = pygame.time.get_ticks()
    clock.tick(30)

pygame.quit()
sys.exit()


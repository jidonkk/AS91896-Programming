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

# Common list of Chinese Numbers
chinese_numbers = {1: "yī", 2: "èr", 3: "sān", 4: "sì", 5: "wǔ",
    6: "liù", 7: "qī", 8: "bā", 9: "jiǔ", 10: "shí",
    11: "shí yī", 12: "shí èr", 13: "shí sān", 14: "shí sì", 15: "shí wǔ",
    16: "shí liù", 17: "shí qī", 18: "shí bā", 19: "shí jiǔ", 20: "èr shí"
}

# Menu
def menu():
    while True:
        window.fill((150, 200, 250))  # Light blue background
        title = font.render("Chinese Numbers Games", True, (0, 0, 0))
        window.blit(title, (160, 100))

        mouse_pos = pygame.mouse.get_pos()
        buttons = [
            {"label": "Quiz", "pos": (220, 200), "action": run_quiz},
            {"label": "Matching Game", "pos": (220, 300), "action": run_cards},
            {"label": "Exit", "pos": (220, 400), "action": quit_game},
        ]

        for button in buttons:
            rect = pygame.Rect(button["pos"][0], button["pos"][1], 300, 70)
            colour = (100, 150, 255) if rect.collidepoint(mouse_pos) else (255, 255, 255)
            pygame.draw.rect(window, colour, rect)
            pygame.draw.rect(window, (0, 0, 0), rect, 3)
            text = small_font.render(button["label"], True, (0, 0, 0))
            text_rect = text.get_rect(center=rect.center)
            window.blit(text, text_rect)
            button["rect"] = rect  # Store the rect for later use

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button["rect"].collidepoint(event.pos):
                        button["action"]()  # Call the action associated with the button

        pygame.display.flip()
        clock.tick(60)

# Quit function
def quit_game():
    pygame.quit()
    sys.exit()

# Quiz Game
def run_quiz():
    questions = random.sample(list(chinese_numbers.items()), 10)
    current_index = 0
    score = 0
    input_text = ""
    feedback = ""

    while True:
        window.fill((200, 220, 255))
        if current_index < len(questions):
            num, ch = questions[current_index]
            window.blit(small_font.render("Type in numbers to answer, then press Enter", True, (0, 0, 0)), (100, 180))
            window.blit(font.render(f"What is '{ch}' in English?", True, (0, 0, 0)), (200, 230))
            pygame.draw.rect(window, (255, 255, 255), (300, 290, 200, 70))
            window.blit(font.render(input_text, True, (0, 0, 0)), (310, 300))

            if feedback:
                color = (0, 128, 0) if feedback == "Correct!" else (255, 0, 0)
                window.blit(small_font.render(feedback, True, color), (300, 370))
        else:
            window.blit(font.render(f"Quiz Finished! Score: {score}/10", True, (0, 0, 0)), (200, 250))
            window.blit(small_font.render("Click anywhere to return to menu", True, (0, 0, 0)), (200, 320))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN and current_index >= len(questions):
                return
            elif event.type == pygame.KEYDOWN and current_index < len(questions):
                if event.key == pygame.K_RETURN:
                    if input_text.strip().isdigit() and int(input_text.strip()) == num:
                        feedback = "Correct!"
                        score += 1
                    else:
                        feedback = f"Wrong! It was {num}."
                    input_text = ""
                    current_index += 1
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key >= pygame.K_0 and event.key <= pygame.K_9:
                    input_text += chr(event.key)

        clock.tick(30)

# Matching Cards Game
def run_cards():
    pairs = random.sample(list(chinese_numbers.items()), 6)
    cards = []
    for num, ch in pairs:
        cards.append((str(num), num))
        cards.append((ch, num))
    random.shuffle(cards)

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

    while True:
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

        if all(matched):
            window.blit(font.render("You matched all pairs!", True, (0, 100, 0)), (200, 420))
            window.blit(small_font.render("Click anywhere to return to menu", True, (0, 0, 0)), (200, 480))

        pygame.display.flip()

        if pause_time > 0 and pygame.time.get_ticks() - pause_time > 1000:
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
                quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if all(matched):
                    return
                for i, rect in enumerate(card_rects):
                    if rect.collidepoint(event.pos) and not revealed[i] and not matched[i] and pause_time == 0:
                        revealed[i] = True
                        if first_selection is None:
                            first_selection = i
                        else:
                            second_selection = i
                            pause_time = pygame.time.get_ticks()

        clock.tick(30)

# Starting the game menu
menu()



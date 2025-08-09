'''
Chinese Numbers Learning Games, Year 7 Game Project
Includes:
- Main Menu
- Quiz Game
- Matching Cards Game
'''

# Importing needed libraries
import pygame
import random
import sys

# Initialising pygame
pygame.init()

# Loading the icon for the game
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Loading the background images
cards_bg = pygame.image.load("cards_background2.webp")
menu_bg = pygame.image.load("menu_background.jpg!sw800")
quiz_bg = pygame.image.load("quiz_background.jpg")

# Loading image for the cards
cardback_image = pygame.image.load("card_back.png")

# Scaling images to fit window size (and card size)
cards_bg = pygame.transform.scale(cards_bg, (800, 600))
menu_bg = pygame.transform.scale(menu_bg, (800, 600))
quiz_bg = pygame.transform.scale(quiz_bg, (800, 600))
cardback_image = pygame.transform.scale(cardback_image, (120, 80))

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

# Common list of Chinese Numbers - This is used across both games
chinese_numbers = {1: "yī", 2: "èr", 3: "sān", 4: "sì", 5: "wǔ",
    6: "liù", 7: "qī", 8: "bā", 9: "jiǔ", 10: "shí",
    11: "shí yī", 12: "shí èr", 13: "shí sān", 14: "shí sì", 15: "shí wǔ",
    16: "shí liù", 17: "shí qī", 18: "shí bā", 19: "shí jiǔ", 20: "èr shí"
}

# Main Menu Function
def menu():
    while True:
        window.blit(menu_bg, (0, 0))  # Background

        # Displaying the title
        title = font.render("Chinese Numbers Games", True, (0, 0, 0))
        window.blit(title, (160, 100))

        # Defines the buttons for each option/action
        mouse_pos = pygame.mouse.get_pos()
        buttons = [
            {"label": "Quiz", "pos": (220, 200), "action": run_quiz},
            {"label": "Matching Game", "pos": (220, 300), "action": run_cards},
            {"label": "Exit", "pos": (220, 400), "action": quit_game},
        ]

        # Drawing the buttons
        for button in buttons:
            rect = pygame.Rect(button["pos"][0], button["pos"][1], 300, 70)

            # Changes button colour when hovered over
            colour = (119, 221, 119) if rect.collidepoint(mouse_pos) else (255, 255, 255)
            pygame.draw.rect(window, colour, rect)
            pygame.draw.rect(window, (0, 0, 0), rect, 3)
            text = small_font.render(button["label"], True, (0, 0, 0))
            text_rect = text.get_rect(center=rect.center)
            window.blit(text, text_rect)
            button["rect"] = rect  # Save the rect to use for click detection

        # Handle events - clicking buttons and quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button["rect"].collidepoint(event.pos):
                        button["action"]()  # Calls the function linked to the button

        pygame.display.flip()
        clock.tick(60)

# Quit function - Quits the game
def quit_game():
    pygame.quit()
    sys.exit()

# Back button function - Draws back button on the screen when called
def draw_back_button(mouse_pos):
    back_rect = pygame.Rect(20, 20, 120, 50)
    colour = (119, 221, 119) if back_rect.collidepoint(mouse_pos) else (255, 255, 255)
    pygame.draw.rect(window, colour, back_rect)
    pygame.draw.rect(window, (0, 0, 0), back_rect, 3)
    back_text = small_font.render("Back", True, (0, 0, 0))
    back_text_rect = back_text.get_rect(center=back_rect.center)
    window.blit(back_text, back_text_rect)
    return back_rect

# Quiz Game - Function that runs the quiz
def run_quiz():
    
    # Selects 10 random chinese numbers for the quiz
    questions = random.sample(list(chinese_numbers.items()), 10)
    current_index = 0
    score = 0
    input_text = ""
    feedback = ""

    while True:
        window.blit(quiz_bg, (0, 0)) # Background
        mouse_pos = pygame.mouse.get_pos() # Finds mouse position

        if current_index < len(questions):
            # Show question and input box
            num, ch = questions[current_index]
            window.blit(small_font.render("Type in numbers to answer, then press Enter", True, (0, 0, 0)), (100, 180))
            window.blit(font.render(f"What is '{ch}' in English?", True, (0, 0, 0)), (200, 230))
            pygame.draw.rect(window, (255, 255, 255), (300, 290, 200, 70))
            window.blit(font.render(input_text, True, (0, 0, 0)), (310, 300))

            # Shows feedback on answer - if its correct or wrong
            if feedback:
                color = (144, 238, 144) if feedback == "Correct!" else (255, 0, 0)
                window.blit(small_font.render(feedback, True, color), (300, 370))

            back_button_rect = draw_back_button(mouse_pos)  # Draws back button

        else:
            # Quiz finished screen - shows the final score then redirects to the menu
            window.blit(font.render(f"Quiz Finished! Score: {score}/10", True, (0, 0, 0)), (200, 250))
            window.blit(small_font.render("Click anywhere to return to menu", True, (0, 0, 0)), (200, 320))
            back_button_rect = None # No back button needed when quiz is finished

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if current_index >= len(questions) or (back_button_rect and back_button_rect.collidepoint(event.pos)):
                    return  # Return to menu if quiz is finished or back button is clicked
            elif event.type == pygame.KEYDOWN and current_index < len(questions):
                if event.key == pygame.K_RETURN:
                    # Check the answer
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

# Matching Cards Game - Function that runs the cards game
def run_cards():

    # Picks 6 random pairs of numbers (12 cards total)
    pairs = random.sample(list(chinese_numbers.items()), 6)
    cards = []
    for num, ch in pairs:
        cards.append((str(num), num))  # English number card
        cards.append((ch, num))  # Chinese pinyin card
    random.shuffle(cards)

    CARD_WIDTH, CARD_HEIGHT = 120, 80
    GRID_ROWS, GRID_COLS = 3, 4
    card_rects = []
    revealed = [False] * len(cards)
    matched = [False] * len(cards)
    first_selection = None
    pause_time = 0

    # Create card positions, each card is a rectangle in a grid layout
    for i in range(len(cards)):
        row = i // GRID_COLS
        col = i % GRID_COLS
        rect = pygame.Rect(100 + col * (CARD_WIDTH + 20), 100 + row * (CARD_HEIGHT + 20), CARD_WIDTH, CARD_HEIGHT)
        card_rects.append(rect)

    while True:
        window.blit(cards_bg, (0, 0))  # Background
        mouse_pos = pygame.mouse.get_pos()  # Finds mouse position

        # Drawing the cards 
        for i, rect in enumerate(card_rects):
            if matched[i]:
                pygame.draw.rect(window, (200, 255, 200), rect)  # Card turns green if matched
            elif revealed[i]:
                pygame.draw.rect(window, (255, 255, 200), rect)  # Card turns yellow if revealed
            else:
                window.blit(cardback_image, rect.topleft)  # Card is white if facing down
            pygame.draw.rect(window, (0, 0, 0), rect, 2)

            # Displays the card text if revealed or matched
            if revealed[i] or matched[i]:
                text = small_font.render(str(cards[i][0]), True, (0, 0, 0))
                text_rect = text.get_rect(center=rect.center)
                window.blit(text, text_rect)

        if not all(matched):
            back_button_rect = draw_back_button(mouse_pos)  # Draws back button while all cards aren't matched

        # Shows message when all pairs are matched
        if all(matched):
            back_button_rect = None  # No back button needed when all pairs are matched
            window.blit(font.render("You matched all pairs!", True, (255, 255, 255)), (200, 420))
            window.blit(small_font.render("Click anywhere to return to menu", True, (0, 0, 0)), (200, 480))

        pygame.display.flip()

        # Pause after two cards are selected
        if pause_time > 0 and pygame.time.get_ticks() - pause_time > 1000:
            if cards[first_selection][1] != cards[second_selection][1]:
                # If not a match, hide the cards
                revealed[first_selection] = False
                revealed[second_selection] = False
            else:
                # Match found, mark as matched
                matched[first_selection] = True
                matched[second_selection] = True
            pause_time = 0
            first_selection = None

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if all(matched):
                    return  # Return to menu when finished 
                if back_button_rect and back_button_rect.collidepoint(event.pos):
                    return  # Return to menu if back button is clicked
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
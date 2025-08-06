'''Quiz - Not with menu'''

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
pygame.display.set_caption("Chinese Quiz")

# Fonts
font = pygame.font.SysFont("Arial", 48)
small_font = pygame.font.SysFont("Arial", 36)

clock = pygame.time.Clock()

# Chinese numbers list
chinese_numbers = {1: "yī", 2: "èr", 3: "sān", 4: "sì", 5: "wǔ",
    6: "liù", 7: "qī", 8: "bā", 9: "jiǔ", 10: "shí",
    11: "shí yī", 12: "shí èr", 13: "shí sān", 14: "shí sì", 15: "shí wǔ",
    16: "shí liù", 17: "shí qī", 18: "shí bā", 19: "shí jiǔ", 20: "èr shí"
}

questions = random.sample(list(chinese_numbers.items()), 10)
current_index, score = 0, 0
input_text, feedback = "", ""

running = True
while running:
    window.fill((200, 220, 255))  # Light blue background

    if current_index < len(questions):
        num, ch = questions[current_index]

        # Displaying the instructions
        instruction_text = small_font.render("Type in numbers to answer, then press Enter", True, (0, 0, 0))
        window.blit(instruction_text, (100, 180))

        # Displaying the question
        window.blit(font.render(f"What is '{ch}' in English?", True, (0, 0, 0)), (200, 230))

        # Input box for the answer
        pygame.draw.rect(window, (255, 255, 255), (300, 290, 200, 70))
        window.blit(font.render(input_text, True, (0, 0, 0)), (310, 300))

        if feedback:
            colour = (0, 128, 0) if feedback == "Correct!" else (255, 0, 0)
            window.blit(small_font.render(feedback, True, colour), (300, 370))

    else:
        window.blit(font.render(f"Quiz Finished! Score: {score}/10", True, (0, 0, 0)), (200, 250))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

pygame.quit()
sys.exit()
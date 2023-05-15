import pygame
import random
import time

pygame.init()

# Set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Typing Game')
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the game variables
word_list = ['apple', 'banana', 'cherry', 'orange', 'pear', 'kiwi', 'grape', 'watermelon']
current_word = random.choice(word_list)
user_input = ''
start_time = None
time_limit = 10 # in seconds
score = 0

# Define a function to draw the current word and user input
def draw_text():
    # Draw the current word
    word_text = font.render(current_word, True, BLACK)
    word_width = word_text.get_width()
    word_height = word_text.get_height()
    screen.blit(word_text, (WINDOW_WIDTH/2 - word_width/2, WINDOW_HEIGHT/2 - word_height/2))
    
    # Draw the user input
    input_text = font.render(user_input, True, BLACK)
    input_width = input_text.get_width()
    input_height = input_text.get_height()
    screen.blit(input_text, (WINDOW_WIDTH/2 - input_width/2, WINDOW_HEIGHT/2 + word_height/2))
    
    # Change the color of the letters that are typed correctly
    for i, char in enumerate(user_input):
        if i >= len(current_word):
            break
        if char == current_word[i]:
            char_text = font.render(char, True, GREEN)
        else:
            char_text = font.render(char, True, RED)
        char_width = char_text.get_width()
        char_height = char_text.get_height()
        screen.blit(char_text, (WINDOW_WIDTH/2 - input_width/2 + i*char_width, WINDOW_HEIGHT/2 + word_height/2))

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                user_input += event.unicode
            elif event.key == pygame.K_RETURN:
                if user_input == current_word:
                    score += 1
                user_input = ''
                current_word = random.choice(word_list)
                start_time = time.time()
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
    
    # Clear the screen
    screen.fill(WHITE)
    
    # Draw the text
    draw_text()
    
    # Draw the score and time remaining
    score_text = font.render(f'Score: {score}', True, BLACK)
    score_width = score_text.get_width()
    screen.blit(score_text, (10, 10))
    if start_time is not None:
        time_remaining = time_limit - int(time.time() - start_time)
        if time_remaining <= 0:
            running = False
        time_text = font.render(f'Time remaining: {time_remaining}', True, BLACK)
        time_width = time_text.get_width()
        screen.blit(time_text, (WINDOW_WIDTH - time_width - 10, 10))
    
   
    pygame.display.update()
    clock.tick(60)
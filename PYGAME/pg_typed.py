import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Typing Game")
font = pygame.font.Font(None, 36)

word_list = ["apple", "banana", "cherry", "orange", "pear"]

class Word:
    def __init__(self, text):
        self.text = text
        self.x = random.randint(100, 700)
        self.y = -50
        self.speed = random.randint(1, 5)

    def move(self):
        self.y += self.speed

    def draw(self):
        text_surface = font.render(self.text, True, (255, 255, 255))
        screen.blit(text_surface, (self.x, self.y))

def word_hit_ground(word):
    return word.y > 550

def new_word():
    word_text = random.choice(word_list)
    return Word(word_text)

clock = pygame.time.Clock()
score = 0
game_over = False
current_word = new_word()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.unicode == current_word.text[0]:
                current_word.text = current_word.text[1:]
                if not current_word.text:
                    score += 1
                    current_word = new_word()

    screen.fill((0, 0, 0))
    current_word.move()
    current_word.draw()

    if word_hit_ground(current_word):
        game_over = True

    score_text = font.render("Score: {}".format(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

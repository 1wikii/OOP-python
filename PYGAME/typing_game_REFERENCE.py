# WATERFALL TEXT

import pygame
import string
import random
from random import randrange
import sys


def WATERFALL_TEXT():
    width = 800
    height = 600
    white = (255,255,255)
    black = (0,0,0)

    pygame.init()
    window = pygame.display.set_mode((width,height))
    pygame.display.set_caption('TYPING GAME')


    font = pygame.font.SysFont('comicsansms', 40)
    word = ['budi','andi','reni','sulis','muloyo','maman']

    class TEXT:

        def __init__(self):
            self.x = random.randint(0, width - 100)
            self.y = -50
            self.text = ''.join(random.choices(word))
            self.speed = 1

        def move (self):
            self.y += self.speed

        def draw(self):
            text_surface = font.render(self.text, True, black)
            window.blit(text_surface, (self.x,self.y))


    clock = pygame.time.Clock()
    score = 0
    text_list = []
    mmax = 40

    while True:
        # Handle Event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Generate New Text
        #if len(text_list) < 4 :
        if randrange(mmax) == 17:
            text_list.append(TEXT())

            
        # Move and draw text
        window.fill("purple")
        for text in text_list:
            text.move()
            text.draw()

            # Checking if they reach the bottom of the screen
            if text.y > height:
                text_list.remove(text)

            # Checkif when player type correctly
            # keys = pygame.key.get_pressed()
            # if all(key in keys for key in text.text):
            #     text_list.remove(text)
            #     score += 1

        # display score
        score_surface = font.render("Score : " + str(score), True, black)
        window.blit(score_surface, (5,10))

        pygame.display.update()
        clock.tick(60)


# DISAPPEAR TEXT
def DISSAPPEAR_TEXT():

    def select_word():
        word_list = [
            'apple',
            'banana',
            'cherry',
            'melon',
            'orange'
        ]

        num_of_elements = len(word_list)
        i = random.randint(0, num_of_elements - 1)
        return word_list[i]


    def cut_head_char(word):
       
        return word[1:]


    def is_empty_word(word):
        return len(word) == 0
        #return not word


    def run_game():
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        font_big = pygame.font.SysFont(None, 78)
        word = select_word()
        cl = pygame.time.Clock()

        score = 0
        temp = 0

        while True:
            temp+=1
            
            screen.fill("purple")
            sf_word = font_big.render(word, True, (0, 0, 0))
            center_x = screen.get_rect().width / 2 - sf_word.get_rect().width / 2
            screen.blit(sf_word, (temp, 200))

            sc = font_big.render(f"Score : {score}", True, (0,0,0))
            screen.blit(sc, (10,10))
          
           #pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.unicode == word[0]:
                        word = cut_head_char(word)
                        if is_empty_word(word):
                            word = select_word()
                            score += 1

            pygame.display.update()
            cl.tick(60)

    run_game()

# MAIN 
#WATERFALL_TEXT()
DISSAPPEAR_TEXT()


import pygame

# color
purple = (189, 52, 235)
white = (255, 255, 255)
orange = (242, 103, 10)

pygame.init()
screen = pygame.display.set_mode((720,500))
cl = pygame.time.Clock()
running = True

pygame.display.set_caption('TYPING GAME by wikii')
screen.fill(purple)
font = pygame.font.SysFont('comicsansms',36)

# Handling each letter color
class each_letter:
	word = []

	def __init__(self, ch):
		self.color = white
		self.ch = ch

	def typed(self):
		self.color = orange

	def draw(self):
		letter_surf = font.render(self.ch, True, white)
		screen.blit(letter_surf, (100,100))

while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		
		if event.type == pygame.KEYDOWN:
			pass
			#if char(event.key) == 

	
	pygame.display.update()
	cl.tick(60)  # 60 fps

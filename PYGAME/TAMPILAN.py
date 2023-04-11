import pygame

pygame.init()

screen = pygame.display.set_mode((720,300))
clock = pygame.time.Clock()
running = True

pygame.display.set_caption("COBA PYGAME")

while running:
    for ivent in pygame.event.get():
        if ivent.type == pygame.QUIT:
            running = False

screen.fill("purple")

my_font = pygame.font.Font(None, 36)
nama = my_font.render("Ahmad Dwiky Zerro Dixxon", True, (255, 255, 255))
screen.blit(nama,(20,20))

clock.tick(60)

pygame.display.update()
pygame.quit()

import pygame

pygame.init()
screen = pygame.display.set_mode((720, 300))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    my_font = pygame.font.SysFont('Comic Sans Ms', 36)
    nama = my_font.render("Ahmad Dwiky Zerro Dixxon", True, (255, 255, 255))
    screen.blit(nama,(20,20))

    nim = my_font.render("121140044", True, (255, 255, 255))
    screen.blit(nim,(20,70))

    ucapan = my_font.render("Selamat menjalankan ibadah puasa!", True, (255, 255, 255))
    screen.blit(ucapan,(20,120))

  
    pygame.display.update()
    clock.tick(60)  

pygame.quit()
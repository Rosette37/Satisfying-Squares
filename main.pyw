import pygame
from critter import Critter

icon = pygame.Surface((32, 32))
icon.fill((255, 0, 0))

pygame.init()
screen_size = (1280, 720)
window_size = (1600, 900)
pygame.display.set_icon(icon)
pygame.display.set_caption("Satisfying squares")
window = pygame.display.set_mode(window_size, pygame.RESIZABLE)
screen = pygame.Surface(screen_size)
clock = pygame.time.Clock()
color = pygame.Color(10, 10, 10)
running = True
clock = pygame.time.Clock()

space_pressed = False

critter_list = []
critter_num = 8000

for i in range(1, critter_num):
    critter_list.append(Critter(screen_size))

while(running):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and space_pressed == False:
        space_pressed = True
        critter_list.append(Critter(screen_size))
    if not keys[pygame.K_SPACE]:
        space_pressed = False
    
    for critter in critter_list:
        critter.update()

    screen.fill(color)

    for critter in critter_list:
        pygame.draw.rect(screen, critter.get_color(), critter.get_rect())
    
    window.blit(pygame.transform.scale(screen, window.size), (0, 0))
    pygame.display.flip()
    clock.tick(60)

    
pygame.quit()

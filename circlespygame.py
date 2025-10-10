import pygame
pygame.init()

screen=pygame.display.set_mode((500,400))
screen.fill((0,209,0))

RED=(255,0,0)

pygame.draw.circle(screen,RED,(100,200),50)
pygame.draw.circle(screen,RED,(300,200),50,3)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

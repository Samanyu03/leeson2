import pygame 

pygame.init()
screen=pygame.display.set_mode((400,500))
while True:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      pygame.quit()
  pygame.draw.rect(screen,(150,90,255), pygame.Rect(60,90,90,90))
  pygame.display.flip()
import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))
screen.fill((255,255,255))
green =(0,255,0)
pygame.draw.circle(screen,green,(300,300),55)
pygame.draw.circle(screen,green,(100,100),55,5)
pygame.display.update()
done = True
while done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           done = False
pygame.quit()

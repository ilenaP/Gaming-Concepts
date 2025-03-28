import pygame
from brick import Paddle
pygame.init()

WIDTH=800
HEIGHT=600

gs=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Brick Smash")

paddle=Paddle()

FPS=20
clock=pygame.time.Clock()

gameloop=True
while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop=False

    paddle.move(event)
    gs.fill("black")
    paddle.draw(gs)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
    
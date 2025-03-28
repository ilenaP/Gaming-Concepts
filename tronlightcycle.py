import pygame
pygame.init()

screen=pygame.display.set_mode((800,800))
pygame.display.set_caption("Troy Light Cycle")

tron_dx=0
tron_dy=0

tronx=740
trony=10

FPS=50
clock=pygame.time.Clock()

tronposition=(tronx, trony, 50, 50)

motor=pygame.draw.rect(screen, "white", tronposition)

body_coords=[]

gameloop=True
while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop=False

    if event.type == pygame.KEYDOWN:
        if event.key==pygame.K_LEFT:
            tron_dx=-10
            tron_dy=0
        elif event.key == pygame.K_RIGHT:
            tron_dx=10
            tron_dy=0
        elif event.key == pygame.K_UP:
            tron_dx=0
            tron_dy=-10
        elif event.key == pygame.K_DOWN:
            tron_dx=0
            tron_dy=10

    body_coords.insert(0,tronposition)
    body_coords.pop()

    tronx=tronx+tron_dx
    trony=trony+tron_dy
    tronposition=(tronx, trony, 50, 50)

    screen.fill("black")

    body_coords.append(tronposition)

    for i in body_coords:
        pygame.draw.rect(screen, "cyan", i)

    motor=pygame.draw.rect(screen, "white", tronposition)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
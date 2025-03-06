import pygame
pygame.init()

midas_dx=0
midas_dy=0

head_x=400
head_y=400

speed=10

FPS=30
clock=pygame.time.Clock()

gs=pygame.display.set_mode((800, 800))
pygame.display.set_caption("Midas Game")

midas=pygame.draw.rect(gs, "yellow", (head_x,head_y,40, 40))

thing1color="red"
thing2color="green"
thing3color="blue"
thing4color="orange"

thing1=pygame.draw.rect(gs,thing1color, (100,100, 50, 50))
thing2=pygame.draw.rect(gs,thing2color, (650,100, 50, 50))
thing3=pygame.draw.rect(gs,thing3color, (100,650, 50, 50))
thing4=pygame.draw.rect(gs,thing4color, (650,650, 50, 50))

gameloop=True
while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop=False

    if event.type == pygame.KEYDOWN:
        if event.key==pygame.K_LEFT:
            midas_dx=-1*speed
            midas_dy=0
        elif event.key == pygame.K_RIGHT:
            midas_dx=1*speed
            midas_dy=0
        elif event.key == pygame.K_UP:
            midas_dx=0
            midas_dy=-1*speed
        elif event.key == pygame.K_DOWN:
            midas_dx=0
            midas_dy=1*speed

    head_x=head_x+midas_dx
    head_y=head_y+midas_dy

    gs.fill("black")

    if midas.colliderect(thing1):
        thing1color="yellow"

    if midas.colliderect(thing2):
        thing2color="yellow"

    if midas.colliderect(thing3):
        thing3color="yellow"

    if midas.colliderect(thing4):
        thing4color="yellow"

    midas=pygame.draw.rect(gs, "yellow", (head_x,head_y,40, 40))
    thing1=pygame.draw.rect(gs,thing1color, (100,100, 50, 50))
    thing2=pygame.draw.rect(gs,thing2color, (650,100, 50, 50))
    thing3=pygame.draw.rect(gs,thing3color, (100,650, 50, 50))
    thing4=pygame.draw.rect(gs,thing4color, (650,650, 50, 50))

    pygame.display.flip()
    clock.tick(FPS)


    

pygame.quit()
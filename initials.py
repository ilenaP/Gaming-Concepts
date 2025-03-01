import pygame

pygame.init()

W_WIDTH=800
W_HEIGHT=800

gs=pygame.display.set_mode((W_WIDTH, W_HEIGHT))
pygame.display.set_caption("Initials")

ilena=pygame.draw.rect(gs, "pink", (100,100, 600, 100))
ilena2=pygame.draw.rect(gs, "pink", (350,200, 100, 400))
ilena3=pygame.draw.rect(gs, "pink", (100, 600, 600, 100 ))

game=True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game=False

    ilena=pygame.draw.rect(gs, "pink", (100,100, 600, 100))
    ilena2=pygame.draw.rect(gs, "pink", (350,200, 100, 400))
    ilena3=pygame.draw.rect(gs, "pink", (100, 600, 600, 100 ))
    pygame.display.flip()


pygame.quit
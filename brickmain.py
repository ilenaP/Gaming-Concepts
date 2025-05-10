import pygame
from brick import Paddle
from brick import Ball
from brick import Bricks

pygame.init()

WIDTH=800
HEIGHT=600

gs=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Brick Smash")

bricks_group=pygame.sprite.Group()
paddle_group=pygame.sprite.Group()
ball_group=pygame.sprite.Group()

num_rows=7
num_cols=7
start_x=80
start_y=20
spacing_x=100
spacing_y=30

for row in range(num_rows):
    for col in range(num_cols):
        x = start_x + col * spacing_x
        y = start_y + row * spacing_y
        brick=Bricks(x,y, bricks_group)
        bricks_group.add(brick)


paddle=Paddle(paddle_group)
ball=Ball(ball_group)

f=pygame.font.Font(None, 36)

FPS=20
clock=pygame.time.Clock()

gameloop=True
while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop=False

    paddle.move(event)
    ball.update()
    gs.fill("black")
    paddle.draw(gs)
    ball.draw(gs)

    bricks_group.update()
    bricks_group.draw(gs)

    scoretext=f.render("Score = " +str(ball.score), True, "white")
    scorerect=scoretext.get_rect(centerx=WIDTH//2, top=15)
    gs.blit(scoretext, scorerect)

    pygame.draw.line(gs,  "white", (0,45), (WIDTH,45), 2)
    pygame.draw.line(gs, "white", (0,525), (WIDTH, 525), 2)

    if pygame.sprite.spritecollide(ball, bricks_group, True):
        ball.speed_y *= -1
        ball.score=ball.score + 10

    if ball.rect.colliderect(paddle.rect):
        ball.speed_y *= -1

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
    
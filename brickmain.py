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
gamewin=False
gamelose=False

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

    hitsound=pygame.mixer.Sound("/Users/durgaparajuli/Desktop/gaming concepts/brickgame/hit.mp3")

    if pygame.sprite.spritecollide(ball, bricks_group, True):
        ball.speed_y *= -1
        ball.score=ball.score + 10
        hitsound.play()

    if ball.rect.colliderect(paddle.rect):
        ball.speed_y *= -1
        hitsound.play()

    if ball.rect.bottom >= HEIGHT:
        go=f.render("You Lost! Game Over!", True, "white")
        gr=go.get_rect(center=(WIDTH//2, HEIGHT//2))
        brick_losesound=pygame.mixer.Sound("/Users/durgaparajuli/Desktop/gaming concepts/brickgame/game_over.mp3")
        brick_losesound.play()
        gamelose=True

    if len (bricks_group) ==0:
        gw=f.render("You hit all the bricks! You win!", True, "white")
        gwt=gw.get_rect(center=(WIDTH//2, HEIGHT//2))
        game_winsound=pygame.mixer.Sound("/Users/durgaparajuli/Desktop/gaming concepts/brickgame/game_win.mp3")
        game_winsound.play()
        gamewin=True   

    if gamelose==True:
        gs.fill("black")
        gs.blit(go, gr)
        pygame.display.update()
        pygame.time.delay(2000)
        gameloop=False

    if gamewin==True:
        gs.fill("black")
        gs.blit(gw, gwt)
        pygame.display.update()
        pygame.time.delay(2000)
        gameloop=False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
    
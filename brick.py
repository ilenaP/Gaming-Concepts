import pygame
import random

class Paddle (pygame.sprite.Sprite):
    def __init__(self, paddle_group):
        self.rect=pygame.Rect(700, 550, 90, 25)
        self.velocity=20
        self.paddle_group=paddle_group
    
    def move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                if self.rect.left > 0:
                    self.rect.x=self.rect.x-self.velocity

            if event.key==pygame.K_RIGHT:
                if self.rect.right < 800:
                    self.rect.x=self.rect.x+self.velocity

    def draw(self,screen):
        pygame.draw.rect(screen, "pink", self.rect)

class Ball (pygame.sprite.Sprite):
    def __init__(self, ball_group):
        self.ball=pygame.image.load("/Users/durgaparajuli/Desktop/gaming concepts/brickgame/ball-removebg-preview.png")
        self.ball=pygame.transform.scale(self.ball, (20,20))
        self.rect=self.ball.get_rect()
        self.rect.centerx=400
        self.rect.centery=300
        self.speed_x=15
        self.speed_y=15
        self.score=0
        self.ball_group=ball_group

    def update(self):
        self.rect.x= self.rect.x + self.speed_x*1
        self.rect.y= self.rect.y + self.speed_y*1
        if self.rect.left <=0 or self.rect.right >= 800:
            self.speed_x *= -1
        if self.rect.top <=0 or self.rect.bottom >= 600:
            self.speed_y*= -1
        
        

    def draw(self, screen):
        pygame.draw.rect(screen, "blue", self.rect)


class Bricks (pygame.sprite.Sprite):
    def __init__(self, x, y, bricks_group):
        super().__init__()
        bricks=["/Users/durgaparajuli/Desktop/gaming concepts/brickgame/pastel-yellow-color-solid-background-1920x1080.png", "/Users/durgaparajuli/Desktop/gaming concepts/brickgame/blue.png", "/Users/durgaparajuli/Desktop/gaming concepts/brickgame/pink.jpg", "/Users/durgaparajuli/Desktop/gaming concepts/brickgame/purple.png" ]
        self.image=pygame.image.load(bricks[random.randint(0,3)])
        self.image=pygame.transform.scale(self.image, (80, 20))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x-25,y+50)
        self.bricks_group=bricks_group

    #def draw (self, screen):
        




    
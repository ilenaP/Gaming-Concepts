import pygame

class Paddle:
    def __init__(self):
        self.rect=pygame.Rect(700, 550, 90, 25)
        self.velocity=10
    
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
    def __init__(self):
        self.ball=pygame.image.load("/Users/durgaparajuli/Desktop/gaming concepts/brickgame/ball-removebg-preview.png")
        self.ball=pygame.transform.scale(self.ball, (20,20))
        self.rect=self.ball.get_rect()
        self.rect.centerx=400
        self.rect.centery=300
        self.speed_x=10
        self.speed_y=10

    def update(self):
        self.rect.x= self.rect.x + self.speed_x*1
        self.rect.y= self.rect.y + self.speed_y*1
        if self.rect.left <=0 or self.rect.right >= 800:
            self.speed_x *= -1
        if self.rect.top <=0 or self.rect.bottom >= 600:
            self.speed_y*= -1

    def draw(self, screen):
        pygame.draw.rect(screen, "blue", self.rect)
        


    
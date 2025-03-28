import pygame

class Paddle:
    def __init__(self):
        self.rect=pygame.Rect(750, 550, 90, 25)
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
from random import randint
from pygame import *
from time import time as timer

window = display.set_mode((740, 600))
display.set_caption("пин-понг")
background = transform.scale(image.load("P.jpg"), (740, 600))
clock = time.Clock()
FPS = 60


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 505:
            self.rect.y += self.speed
    def update_l(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 505:
            self.rect.y += self.speed

hero = Player('D.png',730, 150, 10, 10, 95)
hero2 = Player('D.png',10, 150, 10, 10, 95)


Finish = False


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if Finish != True:
        
        window.blit(background, (0, 0))
        hero.reset()
        hero.update_r()
        hero2.reset()
        hero2.update_l()

    display.update()                    
    clock.tick(FPS)



from pygame import *
from random import *

#classes
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, img_x, img_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (img_x, img_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 505:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 505:
            self.rect.y += self.speed
#class Ball(GameSprite):


ruka1 = Player("ruka1.png", 20, 100, 4, 200, 200)
ruka2 = Player("ruka2.png", 1050, 100, 4, 200, 200)
ball = Player("ball.png", 300, 300, 3, 75, 75)

window = display.set_mode((1280, 720))
display.set_caption('Ping-Pong')
background = transform.scale(image.load("sky.png"), (1280, 720))
window.blit(background, (0, 0))


#cycle-game
clock = time.Clock()
clock.tick(60)

game = True
finish = False
speed_x = 6
speed_y = 6
font.init()
font = font.SysFont('Arial', 60)
lose1 = font.render('1p Lose!', True, (255,0,0))
lose2 = font.render('2p Lose!', True, (255,0,0))
while game:
    display.update()
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        window.blit(background, (0, 0))
        keys_pressed = key.get_pressed()
        ruka1.reset()
        ruka1.update_l()
        ruka2.reset()
        ruka2.update_r()
        ball.reset()
        if ball.rect.y < 0 or ball.rect.y > 650:
            speed_y *= -1
        if sprite.collide_rect(ruka1, ball) or sprite.collide_rect(ruka2, ball):
            speed_x *= -1
        if ball.rect.x < -80:
            finish = True
            window.blit(lose1, (600, 350))
        if ball.rect.x > 1320:
            finish = True
            window.blit(lose2, (600, 350))
        

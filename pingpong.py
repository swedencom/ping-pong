from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 340:
            self.rect.y += self.speed

    def updatet(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 340:
            self.rect.y += self.speed



class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.y = -20
            self.rect.x = randint(80,620)
            self.speed = randint(1,2)
            lost = lost + 1



window = display.set_mode((700,500))
display.set_caption('ping-pong')
background = transform.scale(image.load('fone.png'), (700,500))

player = Player('playeer.png', 10, 50, 20, 150, 5)
playert = Player('playeer.png', 670, 50, 20, 150, 5)

ball = GameSprite('ball.png', 40, 20, 50, 50, 3)

clock = time.Clock()
FPS = 60
game = True
finish = False

speed_y = 3
speed_x = 3

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))




while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background,(0,0))

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        player.update()
        playert.updatet()

        ball.reset()
        player.reset()
        playert.reset()

    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1

    if sprite.collide_rect(player, ball) or sprite.collide_rect(playert, ball):
        speed_x *= -1

    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (250,250))

    if ball.rect.x > 650:
        finish = True
        window.blit(lose2, (250,250))


    display.update()
    clock.tick(FPS)
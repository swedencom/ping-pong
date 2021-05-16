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


clock = time.Clock()
FPS = 60
game = True
finish = False


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background,(0,0))

        player.update()
        playert.updatet()

        player.reset()
        playert.reset()

    display.update()
    clock.tick(FPS)
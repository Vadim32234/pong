from pygame import *
win_wight = 700
win_height = 500
window = display.set_mode((win_wight, win_height))
display.set_caption('PING_PONG')
background = transform.scale(image.load('images.jpg'), (win_wight, win_height))
font.init()
font2 = font.SysFont("Arial", 40)
lose = font2.render("YOU LOSE", True, (247, 5, 5))
img_roket = "pngtree-a-beautiful-tennis-racket-png-image_13293625.png"
FPS = 60
game =  True
finish = False
clock = time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_wight - 80:
            self.rect.x += self.speed
raket1 = Player("img_roket", 350, 400, 5)
finish = False
run = True
while run
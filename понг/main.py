from pygame import *
win_wight = 700
win_height = 500
window = display.set_mode((win_wight, win_height))
display.set_caption('PING_PONG')
background = transform.scale(image.load('images.jpg'), (win_wight, win_height))
font.init()
font2 = font.SysFont("Arial", 40)
lose = font2.render("PLAYER 1 LOSE", True, (247, 5, 5))
lose2 = font2.render("PLAYER 2 LOSE", True, (247, 5, 5))
img_roket = "pngtree-a-beautiful-tennis-racket-png-image_13293625.png"
img_ball = "tennis.png"
FPS = 60
game = True
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
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    
    def update_res(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:  
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:  
            self.rect.y += self.speed

raket1 = Player(img_roket, 605, 200, 10)  
raket2 = Player(img_roket, 25, 200, 10)  
ball = GameSprite(img_ball, 250, 200, 10)
speed_x = 3
speed_y = 3
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    if not finish:
        window.blit(background, (0, 0))
        
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        ball.reset()
        
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        
        
        if sprite.collide_rect(raket1, ball) or sprite.collide_rect(raket2, ball):
            speed_x *= -1
        
        
        if ball.rect.x < 0 or ball.rect.x > win_wight:
            finish = True
            window.blit(lose, (250, 200))

        if ball.rect.x > 700 or ball.rect.x > win_wight:
            finish = True
            window.blit(lose2, (250, 200))
        
        
        raket1.update()
        raket1.reset()
        raket2.update_res()  
        raket2.reset()
    
    display.update()  
    clock.tick(30)   

quit()

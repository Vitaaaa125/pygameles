from pygame import *

window = display.set_mode((900, 600))
clock = time.Clock()
display.set_caption("Доганялки")
FPS = 60
 
bg = image.load("images/background.png")
bg = transform.scale(bg, (900, 600))

class Player(sprite.Sprite):
    def __init__(self, sprite_image, x, y):
        super().__init__()

        self.image = transform.scale(image.load(sprite_image), (75, 75) )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1.5

    def draw(self, window):
        window.blit(self.image, self.rect)

    def update(self, key_r, key_l, key_u, key_d):
        keys = key.get_pressed()
        if keys[key_r]:
            self.rect.x += self.speed
        if keys[key_l]:
            self.rect.x -= self.speed
        if keys[key_d]:
            self.rect.y += self.speed
        if keys[key_u]:
            self.rect.y -= self.speed
    


player1 = Player("images/sprite1.png", 150, 450)
player2 = Player("images/sprite2.png", 450, 450)
player3 = Player("images/20250608155334!Стіч_(персонаж).png", 450, 150)




while True:
    window.blit(bg, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            quit()
    
    player1.update(K_RIGHT, K_LEFT, K_UP, K_DOWN)
    player2.update(K_d, K_a, K_w, K_s)
    player3.update(K_j, K_g,K_y,K_h)

    if sprite.collide_rect(player1, player2):
        quit()
    elif sprite.collide_rect(player3, player2):
        quit()
    elif sprite.collide_rect(player1, player3):
        quit()
    
    player1.draw(window)
    player2.draw(window)
    player3.draw(window)

    display.update()
    clock.tick(FPS)
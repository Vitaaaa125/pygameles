from pygame import *

window = display.set_mode((900, 600))
clock = time.Clock()
display.set_caption("Доганялки")
FPS = 60
 
bg = image.load("images/background.png")
bg = transform.scale(bg, (900, 600))
player1 = transform.scale(image.load("images/sprite1.png"), (75, 75) )

while True:
    window.blit(bg, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            quit()
    window.blit(player1, (150, 150))
    

    display.update()
    clock.tick(FPS)
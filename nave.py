import pygame, random


width=800
height=600
black=(0,0,0)
white=(255,255,255)
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("meteoros")
clock= pygame.time.Clock()

#clase para la nave espacial
class Nave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("imagenes/nave.png").convert()
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
        self.rect.centerx = width//2
        self.rect.bottom=height-10
        self.speed_x=0
        #self.listaDisparo=[]
        #self.Vida=True
    def update(self):
        self.speed_x=0
        self.speed_y=0
        keystate= pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x=-5
        if keystate[pygame.K_RIGHT]:
            self.speed_x=5
        if keystate[pygame.K_UP]:
            self.speed_y=-5
        if keystate[pygame.K_DOWN]:
            self.speed_y=5
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.right>width:
            self.rect.right=width
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.top<0:
            self.rect.top=0
        if self.rect.bottom>height:
            self.rect.bottom=height

    

all_sprites=pygame.sprite.Group()

jugador=Nave()
all_sprites.add(jugador)

runnig=True
while runnig:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runnig=False
    all_sprites.update()
    screen.fill(black)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()

    
    
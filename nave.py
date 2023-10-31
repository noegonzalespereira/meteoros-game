import pygame, random


width=800
height=600
black=(0,0,0)
white=(255,255,255)
blue = (0, 0, 255)
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("meteoros")
clock= pygame.time.Clock()

#clase para la nave espacial
class Nave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("img/nave.png").convert()
        self.image.set_colorkey(blue)
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

    def disparar(self):
        bala=bala()
        all_sprites.add(bala)
        balas.add(bala)
class Meteorito(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("img/asteroids.png").convert()
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(width-self.rect.width)
        self.rect.y=random.randrange(-25,-10)
        self.speedy=random.randrange(1,3)
        self.speedx=random.randrange(-3,3)
        #caida de los meteoros
    def update(self):
        self.rect.y+=self.speedy
        self.rect.x+=self.speedx
        if self.rect.top>height+10 or self.rect.left < -25 or self.rect.right > width+25:
           self.rect.x=random.randrange(width-self.rect.width)
           self.rect.y=random.randrange(-25,-10)
           self.speedy=random.randrange(1,3)


        


all_sprites=pygame.sprite.Group()
meteoro_lista=pygame.sprite.Group()

jugador=Nave()
all_sprites.add(jugador)
for i in range(8):
    meteoro=Meteorito()
    all_sprites.add(meteoro)
    meteoro_lista.add(meteoro)

runnig=True
while runnig:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runnig=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                jugador.disparar()
    all_sprites.update()
    #colisiones
    choque= pygame.sprite.spritecollide(jugador,meteoro_lista,True)
    if choque:
        runnig=False

    screen.fill(black)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()

    
    
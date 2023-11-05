import pygame, random
 


width=800
height=600
black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
blue = (0, 0, 255)
pygame.init()
pygame.mixer.init()

screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("meteoros")
clock= pygame.time.Clock()

#surface=donde dibujar el texto
def dibujarTexto(surface,text,size,x,y):
    font = pygame.font.SysFont("serif",size)
    text_surface= font.render(text,True,white)
    text_rect=text_surface.get_rect()
    text_rect.midtop=(x,y)
    surface.blit(text_surface,text_rect)

def dibujarBarraVida(surface,x,y,porcentaje):
    barra_lenght= 100
    barra_height= 10
    fill_lenght=(porcentaje/100)*barra_lenght
    border= pygame.Rect(x,y,barra_lenght,barra_height)
    fill= pygame.Rect(x,y,fill_lenght,barra_height)
    pygame.draw.rect(surface,green,fill)
    pygame.draw.rect(surface,white,border,1)


#clase para la nave espacial
class Nave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.transform.scale((pygame.image.load("img/nave.png").convert()),(50,50))
        self.image.set_colorkey(blue)
        self.rect=self.image.get_rect()
        self.rect.centerx = width//2
        self.rect.bottom=height-10
        self.speed_x=0
        self.vida=100
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
        bullet = Bala(self.rect.centerx,self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        #laser_sound.play()
        
    


class Meteorito(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #meteoros de distinto tamaño aleatoriamente
        #self.image=random.choice(meteoro_imagenes)
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

    

class Bala(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        #carga la imagen
        self.image=pygame.image.load("img/laser1.png")
        #remover el fondo
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
        self.rect.y=y
        self.rect.centerx=x
        self.speedy=-10
    def update(self):
        #la bala sube automaticamente 
        self.rect.y+=self.speedy
        #elimina las instacias/balas para que no ocupe espacio de memoria
        if self.rect.bottom<0:
            self.kill()
    


#cargar imagen de fondo
#background=pygame.image.load("img/background.png") 

# meteoro_imagenes=[]
# meteoro_lista=["img/asteroids.png","img/asteroidPeque2.png"]
# #almacenando todos los meteoros a la lista de meteoros
# for img in meteoro_lista:
#     meteoro_imagenes.append(pygame.image.load(img).convert())

#cargando sonidos 
laser_sound=pygame.mixer.Sound("sound/laser.ogg")
explosion_sound=pygame.mixer.Sound("sound/explosion.wav")
pygame.mixer.music.load("sound/soundPlayer.ogg")
pygame.mixer.music.set_volume(0.2)

all_sprites=pygame.sprite.Group()
meteoro_lista=pygame.sprite.Group()
bullets=pygame.sprite.Group()

jugador=Nave()
all_sprites.add(jugador)
for i in range(8):
    meteoro=Meteorito()
    all_sprites.add(meteoro)
    meteoro_lista.add(meteoro)
    
score=0
#pygame.mixer.music.play(loops=-1)
running=True
while running:
    clock.tick(60)
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT:
            runnig=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                jugador.disparar()

    all_sprites.update()
    #colisiones-meteoro-laser
    choque=pygame.sprite.groupcollide(meteoro_lista,bullets,True,True)
    #vuelve a caer los meteoros aunque se destruyan
    for choq in choque:
        score+=1
        #explosion_sound.play()
        meteoro=Meteorito()
        all_sprites.add(meteoro)
        meteoro_lista.add(meteoro)
    #colisiones-jugador-meteoro
    choque= pygame.sprite.spritecollide(jugador,meteoro_lista,True)
    if choque:
        #explosion_sound.play() 
        running=True
        jugador.vida-=33.9
        if jugador.vida<0:
            running=False
        
     
    #screen.blit(background,[600,800])
    
    screen.fill(black)
    all_sprites.draw(screen)
    #marcador
    dibujarTexto(screen,str(score),25,width//2,10)
    dibujarBarraVida(screen,5,5,jugador.vida)
    pygame.display.flip()
pygame.quit()

    
    
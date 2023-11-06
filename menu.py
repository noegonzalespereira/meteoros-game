def menu():
    
    pygame.mixer.init()
    #variebles
    pantalla = pygame.display.set_mode(size)
    clock  = pygame.time.Clock()

    #fuentes
    fuente = pygame.font.SysFont("tahoma", 30)

    #texto  para mostrar en pantalla
    TextoPlay  = fuente.render("Play", True, white)
    TextoExit = fuente.render("Exit", True, white)
    TextoAbaut = fuente.render("About", True, white)

    #cargar imagenes
    logomenu = pygame.image.load("img/logomenu.png")
    logomenu = pygame.transform.scale(logomenu, (400,200))
    asteroids = pygame.image.load("img/asteroids.png")
    asteroids.set_colorkey([0,0,0])

    #cargar sonidos
    star = pygame.mixer.Sound("sound/star.mp3")
    fondo = pygame.mixer.Sound("sound/soundfondo.mp3")
    
    #coordenas de aparecion de los asteroides
    coor_list = []
    for i in range(15):
        x  = random.randint(0,800)
        y  = random.randint(0,800)
        coor_list.append([x,y])

    menu = True
    while menu == True : 
        #color de fondo
        pantalla.fill(black)
        fondo.play()
        #cargar a la pantalla los asteroides
        for j in coor_list:
            x  = j[0]
            y  = j[1]
            pantalla.blit(asteroids,(x,y))
            j[1] += 1
            if j[1] > 600:
                j[1] = 0

        #cargar figuras
        rectangulo0 = pygame.draw.rect(pantalla, [0,0,0], (250,350,85,40), 0)
        rectangulo0_1 = pygame.draw.rect(pantalla, [0,0,0], (250,390,85,40), 0)
        rectangulo0_2 = pygame.draw.rect(pantalla, [0,0,0], (250,430,85,40), 0)
        rectangulo1 = pygame.draw.rect(pantalla, [237,128,19], (250,350,85,40), 2)
        rectangulo2 = pygame.draw.rect(pantalla, [70,189,34], (250,390,85,40), 2)
        rectangulo3 = pygame.draw.rect(pantalla, [70,189,34], (250,430,85,40), 2)

        #cambio de colores de las figuras y letras
        if rectangulo1.collidepoint(pygame.mouse.get_pos()):
            rectangulo1 = pygame.draw.rect(pantalla, [237,128,19], (250,350,85,40), 2)
            TextoPlay  = fuente.render("Play", True, [237,128,19])
        else:
            rectangulo1 = pygame.draw.rect(pantalla, [70,189,34], (250,350,85,40), 2)
            TextoPlay  = fuente.render("Play", True, white)
        if rectangulo2.collidepoint(pygame.mouse.get_pos()):
            rectangulo2 = pygame.draw.rect(pantalla, [237,128,19], (250,390,85,40), 2)
            TextoAbaut = fuente.render("About", True, [237,128,19])
        else:
            rectangulo2 = pygame.draw.rect(pantalla, [70,189,34], (250,390,85,40), 2)
            TextoAbaut = fuente.render("About", True, white)
        if rectangulo3.collidepoint(pygame.mouse.get_pos()):
            rectangulo3 = pygame.draw.rect(pantalla, [237,128,19], (250,430,85,40), 2)
            TextoExit = fuente.render("Exit", True, [237,128,19])
        else:
            rectangulo3 = pygame.draw.rect(pantalla, [70,189,34], (250,430,85,40), 2)
            TextoExit = fuente.render("Exit", True, white)

        #cargar texto
        pantalla.blit(TextoPlay,[265,350])
        pantalla.blit(TextoAbaut,[252,390])
        pantalla.blit(TextoExit,[265,430])

        #eventos dentro de la pantalla
        for event in pygame.event.get():

            #evento para salir
            if event.type == pygame.QUIT:
                sys.exit()
            
            #eventos para los botones
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if rectangulo1.collidepoint(pygame.mouse.get_pos()):
                    op = 3
                    fondo.stop()
                    star.play()
                    time.sleep(1)
                    menu = False
                if rectangulo2.collidepoint(pygame.mouse.get_pos()):
                    op = 2
                    fondo.stop()
                    star.play()
                    time.sleep(0.7)
                    menu = False
                if rectangulo3.collidepoint(pygame.mouse.get_pos()):
                    fondo.stop()
                    star.play()
                    time.sleep(1)
                    sys.exit()


        pantalla.blit(logomenu, (100,110))
        pygame.display.update()
        clock.tick(60)
    pygame.mixer.quit()
    return op

def abaout():
    pantalla = pygame.display.set_mode(size)
    clock  = pygame.time.Clock()
    
    back = pygame.draw.rect(pantalla, [222,100,0], (250,350,85,40), 0)

    about = True
    while about == True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back.collidepoint(pygame.mouse.get_pos()):
                    op = 1
                    about = False
        pygame.display.update()
        clock.tick(60)
    return  op

def juego ():
    pygame.init()
    pygame.mixer.init()
    width=800
    height=600
    black=(0,0,0)
    white=(255,255,255)
    blue = (0, 0, 255)
    green=(0,255,0)
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
        def update(self):
            self.speed_x=0
            self.speed_y=0
            #movimiento de la nave
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
            #para que se mantenga en el ancho y altura establecido
            if self.rect.right>width:
                self.rect.right=width
            if self.rect.left<0:
                self.rect.left=0
            if self.rect.top<0:
                self.rect.top=0
            if self.rect.bottom>height:
                self.rect.bottom=height
        def disparar(self):
            bullet=Bala(self.rect.centerx,self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
            laser_sound.play()

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
    class ExplosionBala(pygame.sprite.Sprite):
        def __init__(self,center):
            super().__init__()
            self.image = explosion_anim[0]
            self.rect=self.image.get_rect()
            self.rect.center = center
            self.frame=0
            self.last_update=pygame.time.get_ticks() #cuanto tiempo transcurrio cuando se inicio el juego
            self.frame_rate=50 #velocidad de la explosion
        def update(self):
            now=pygame.time.get_ticks()
            if now-self.last_update > self.frame_rate:
                self.last_update=now
                self.frame+=1
                if self.frame == len(explosion_anim):
                    self.kill()
                else:
                    center=self.rect.center
                    self.image=explosion_anim[self.frame]
                    self.rect= self.image.get_rect()
                    self.rect.center=center
    class ExplosionNave(pygame.sprite.Sprite):
        def __init__(self,center):
            super().__init__()
            self.image = explosion_anim2[0]
            self.rect=self.image.get_rect()
            self.rect.center = center
            self.frame=0
            self.last_update=pygame.time.get_ticks() #cuanto tiempo transcurrio cuando se inicio el juego
            self.frame_rate=50 #velocidad de la explosion
        def update(self):
            now=pygame.time.get_ticks()
            if now-self.last_update > self.frame_rate:
                self.last_update=now
                self.frame+=1
                if self.frame == len(explosion_anim2):
                    self.kill()
                else:
                    center=self.rect.center
                    self.image=explosion_anim2[self.frame]
                    self.rect= self.image.get_rect()
                    self.rect.center=center

    def muestraGameOver():
        screen.fill(black)
        dibujarTexto(screen,"GAME OVER",70,width//2,height//2)
        pygame.display.flip()
        espera=True
        while espera:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    espera=False
    #cargar img explosiones
    #lista de explosiones
    explosion_anim=[]
    for i in range(9):
        file="img/regularExplosion0{}.png".format(i)
        img=pygame.image.load(file).convert()
        img.set_colorkey(black)
        img_scale=pygame.transform.scale(img,(70,70))
        explosion_anim.append(img_scale)

    explosion_anim2=[]
    img=pygame.image.load("img/regularExplosion03.png").convert()
    img.set_colorkey(black)
    img_scale=pygame.transform.scale(img,(70,70))
    explosion_anim2.append(img_scale)

    #cargando sonidos 
    laser_sound=pygame.mixer.Sound("sound/laser.ogg")
    explosion_sound=pygame.mixer.Sound("sound/explosion.wav")
    pygame.mixer.music.load("sound/soundPlayer.ogg")
    pygame.mixer.music.set_volume(0.4)
    





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
    pygame.mixer.music.play(loops=-1)
    Game_over=False


    back = pygame.draw.rect(screen, [0,0,255], (250,350,85,40), 0)
    running=True
    while running:
        
        if Game_over==True:
            muestraGameOver()
            running=False
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    jugador.disparar()

        all_sprites.update()
        #colisiones-meteoro-laser
        hits=pygame.sprite.groupcollide(meteoro_lista,bullets,True,True)
        #vuelve a caer los meteoros aunque se destruyan
        for hit in hits:
            score+=1
            explosion_sound.play()
            explosion=ExplosionBala(hit.rect.center)
            all_sprites.add(explosion)
            meteoro=Meteorito()
            all_sprites.add(meteoro)
            meteoro_lista.add(meteoro)
        #colisiones-jugador-meteoro
        hits = pygame.sprite.spritecollide(jugador,meteoro_lista,True)
        for hit in hits:
            explosion_sound.play()
            explosiones=ExplosionNave(hit.rect.center)
            all_sprites.add(explosiones)
            jugador.vida-=33.9
            meteoro=Meteorito()
            all_sprites.add(meteoro)
            meteoro_lista.add(meteoro)
            if jugador.vida<0:
                Game_over=True


        screen.fill(black)
        all_sprites.draw(screen)
        #marcador
        dibujarTexto(screen,str("kills:"),25,width-450,10)
        dibujarTexto(screen,str(score),25,width//2,10)
        dibujarBarraVida(screen,5,5,jugador.vida)
        pygame.display.flip()
    pygame.quit()
    return op


#inicio del juego
import pygame,sys,time,random

op = 1

#tamaño de las ventanas
size = [600, 600]

#colores
white = [255,255,255]
black = [0,0,0]

#iniciar pygame
pygame.init()
pygame.mixer.init()
salir = False
while salir == False :
    if op == 1:
        op = menu()
    elif op == 2:
        op = abaout()
    if op == 3:
        op = juego()
pygame.mixer.quit()
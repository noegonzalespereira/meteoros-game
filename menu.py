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
    screen=pygame.display.set_mode((width,height))
    pygame.display.set_caption("meteoros")
    clock= pygame.time.Clock()

    #clase para la nave espacial
    class Nave(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image=pygame.transform.scale((pygame.image.load("img/nave.png").convert()),(50,50))
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

    all_sprites=pygame.sprite.Group()

    jugador=Nave()
    all_sprites.add(jugador)
    back = pygame.draw.rect(screen, [0,0,255], (250,350,85,40), 0)
    runnig=True
    while runnig:
        
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            # if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #     if back.collidepoint(pygame.mouse.get_pos()):
            #         op = 1
            #         runnig = False
        all_sprites.update()
        screen.fill(black)
        all_sprites.draw(screen)
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
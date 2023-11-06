import pygame
import sys, random

pygame.init()
# definir colores 
black=(0, 0, 0)
white= (255, 255, 255)

#Definir tiempo
clok = pygame.time.Clock()

# muetra las imagenes de la pantalla principal
# fondo = pygame.image.load("fondoEspacio.jpg")
# fondo = pygame.transform.scale(fondo, (800,600))

#cargar fuente en diccionario
fuente1 = pygame.font.Font(None, 70)

# cargar fuente
fuente = pygame.font.SysFont("Cooper Black", 30)
fuente1 = pygame.font.SysFont("Ink Free", 30)

# caragar texto
texto = fuente.render("C r e d i t o s ", False, (245, 253, 3 ))
texto1 = fuente1.render(" Desarrolladores del juego :", False, (245, 253, 3 ))
noelia = fuente1.render(" - Noelia Gonzales ", False, (225, 195, 136 ))
ruben = fuente1.render(" - Ruben Camargo ", False, (225, 195, 136 ))
willian = fuente1.render(" - Jhon Fernández  ", False, (225, 195, 136 ))
carlos = fuente1.render(" - Juan Carlos Kama ", False, (225, 195, 136 ))
cristian = fuente1.render(" - Cristian Cayo  ", False, (225, 195, 136 ))

#muestra las coordenadas de los puntos (lluvia)
coord_list= []
for i in range(60):
        x = random.randint(0,800)
        y = random.randint(0, 600)
        coord_list.append([x,y])



# muestra la pantalla
screen = pygame.display.set_mode((800,600))

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: sys.exit()

    # muestra las imagenes a la pantalla principal
    screen.fill(black)
    #screen.blit(fondo, (0,0))
    


    # muuestra la lluvia aleatorio
    list_de_coordenadas= ()
    for j in coord_list:
            x = j[0]
            y = j[1]
            pygame.draw.circle(screen,white ,(x, y), 2)
            j[1] +=1
            if j[1] > 600:
              j[1] = 0 

    #mostrar texto de los desarrolladores del juego          
    screen.blit(texto, (300,10))
    screen.blit(texto1, (10,170))
    screen.blit(noelia, (10,210))
    screen.blit(ruben, (10,250))
    screen.blit(willian, (10,290))
    screen.blit(carlos, (10,330))
    screen.blit(cristian, (10,370))
    pygame.display.flip()
    clok.tick(30)
    
 
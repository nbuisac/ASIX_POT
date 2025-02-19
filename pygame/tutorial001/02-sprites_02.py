from pygame import sprite        #Para generar y tratar los sprites correctamente
from pygame.locals import *      #Para gestionar eventos

import pygame
import sys

#Inicializamos pygame
pygame.init()

#Establecemos el tamaño de la ventana.
ventana = pygame.display.set_mode((700,400))

''' Documentación sobre sprites
    http://caca.zoy.org/wiki/libcaca

    Principalmente los sprites están compuestos de una imagen
    y posteriormente de un objeto Rect (https://www.pygame.org/docs/ref/rect.html)
    que utiliza Pygame para situarlo dentro de la pantalla y otras cosas
    como colisiones, etc
'''
#Nuestro personaje hereda de la clase Sprite de Pygame
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((100, 100))
        self.surf.fill((0,255,40))
        self.rect = self.surf.get_rect(center = (ventana.get_width()/2, ventana.get_height()/2))

class Personaje(sprite.Sprite):

    def __init__(self):
        #Init de Sprite
        sprite.Sprite.__init__(self)
        ''' Cargamos la hoja completa de sprites del personaje.
            Se realiza convert_alpha() para que tenga en cuenta transparencias (capa alpha)
        '''
        self.spriteSheet = pygame.image.load("sprites/sheet_01.png").convert_alpha()

        ''' "image" se corresponde con la imagen actual a mostrar.
            La hacemos más pequeña para que quede mejor.

            Aquí lo que hacemos es coger de la hoja total de sprites, coger
            el sprite que nos interesa para dibujar. subsurface devuelve un trozo
            de una imagen más grande y con scale, se reduce el tamaño de la imagen.
        '''
        self.image = pygame.transform.scale(self.spriteSheet.subsurface((0,0,200,220)),(100,100)).split(horizontal=True)
        #Necesario para mostrar la imagen
        self.rect = self.image.get_rect()
        #Donde se situa la imagen.
        self.rect.center = (ventana.get_width()/2, ventana.get_height()/2)
        self.q = 0

    #Método heredado de la clase Sprite y que no vamos a usar ahora
    def update(self):
        self.q += 1
        self.image = pygame.transform.flip(self.image, True, False)
        self.q = 0

''' Con esto ya tenemos todo lo básico para generar el sprite.
    Así que toca pintarlo
'''

#Creación del personaje
magikarp = Personaje()
magikarp2 = Player()
''' Es buena práctica asignar sprites solitarios como en este caso
    a grupos de sprite de pygame. No es obligatorio, pero son buenas prácticas,
    ya que facilita algunas cosas como pintar o actualizar.

    Así que creamos el grupo y añadimos a nuestro magikarp 100% al grupo
'''
grupo_sprites = pygame.sprite.GroupSingle()
grupo_sprites.add(magikarp)
all_sprites = pygame.sprite.Group()
all_sprites.add(magikarp2)
#Bucle de "Juego"
while True:
    for event in pygame.event.get():    #Cuando ocurre un evento...
        if event.type == pygame.QUIT:   #Si el evento es cerrar la ventana
            pygame.quit()               #Se cierra pygame
            sys.exit()                  #Se cierra el programa

    #Actualizacion de cosas (si hubiese)

    #Dibujamos todo lo que hay en el grupo. En este caso a Magickarp
    ventana.blit(magikarp2.surf, magikarp2.rect)
    magikarp2.update(ventana)
    grupo_sprites.draw(ventana)
    #Actualiza la ventana
    pygame.display.flip()

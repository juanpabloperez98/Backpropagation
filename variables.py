import pygame
import Tests as T

Blanco = [255,255,255]
Rojo = [255,0,0]

class Segmento(pygame.sprite.Sprite):
    def __init__(self,ancho,alto,numero):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([ancho,alto])
        self.image.fill(Blanco)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.state = 0
        self.numero = numero
    
    def update(self):
        if self.state == 0:
            self.image.fill(Blanco)
        else:
            self.image.fill(Rojo)


segmentos_verticales = []
segmentos_horizontales = []
todos = pygame.sprite.Group() 

lista_numeros = [1,6,4,3]
for seg in range(4):
    segmento = Segmento(20,100,lista_numeros[seg])
    todos.add(segmento)
    segmentos_verticales.append(segmento)


lista_numeros_2 = [2,7,5]
for seg in range(3):
    if seg == 1:
        segmento = Segmento(125,12,lista_numeros_2[seg])
    else:
        segmento = Segmento(140,20,lista_numeros_2[seg])

    todos.add(segmento)
    segmentos_horizontales.append(segmento)






def calcular(entrada):
    img = ""
    lay,out = T.neuron.spread(entrada)

    

    for o in range(len(out)):
        if (out[o] > 0 and out[o] < 0.1):
            out[o] = 0
        elif (out[o] > 0.8 and out[o] < 1):
            out[o] = 1
        else:
            if out[o] < 0.5:
                out[o] = 0
            else:
                out[o] = 1


    
    
    out = list(out)

    print(out)

    if out == [0,0,0,0]:
        img = "imagenes/0.png"
    elif (out == [0,0,0,1]):
        img = "imagenes/1.png"
    elif (out == [0,0,1,0]):
        img = "imagenes/2.png"
    elif (out == [0,0,1,1]):
        img = "imagenes/3.png"
    elif (out == [0,1,0,0]):
        img = "imagenes/4.png"
    elif (out == [0,1,0,1]):
        img = "imagenes/5.png"
    elif (out == [0,1,1,0]):
        img = "imagenes/6.png"
    elif (out == [0,1,1,1]):
        img = "imagenes/7.png"
    elif (out == [1,0,0,0]):
        img = "imagenes/8.png"
    elif (out == [1,0,0,1]):
        img = "imagenes/9.png"
    else:
        img = "imagenes/null.png"

    

    return img



               



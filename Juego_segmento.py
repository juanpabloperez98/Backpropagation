import pygame
import Tests as RN
import variables as var
import numpy as np

ancho = 700
alto = 500



if __name__ == "__main__":

    #----------------Inicio----------------
    pygame.init()
    RN.iniciar()
    pantalla = pygame.display.set_mode([ancho,alto])
    fin = False
    #------------------------------------------------    
    Tancho = ancho/2   
    en_x = 85
    en_y = 150
    for elemento_vertical in range(len(var.segmentos_verticales)):
        var.segmentos_verticales[elemento_vertical].rect.x = en_x
        var.segmentos_verticales[elemento_vertical].rect.y = en_y   

        if elemento_vertical < 1:
            en_y += 105
        elif(elemento_vertical >= 1 and elemento_vertical < 2):
            en_x += 120
        else:            
            en_y -= 105

    #-----------------------------------------------------
    en_x = 85
    en_y = 125
    for elemento_horizontal in range(len(var.segmentos_horizontales)):
        #print(var.segmentos_horizontales[elemento_horizontal].rect[3])
        var.segmentos_horizontales[elemento_horizontal].rect.x = en_x
        var.segmentos_horizontales[elemento_horizontal].rect.y = en_y

        en_x = 85

        if elemento_horizontal == 0:
            en_x += 10

        en_y += 118
    
    #-----------------------------------------------------
    cargar_imagen = False
    imagen = ""
    salida = []
        
            
        

    while not fin:
        posy = 100
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for c in var.todos:
                        if c.rect.collidepoint(pos)==True:
                            if c.state == 0:
                                c.state = 1
                            else:
                                c.state = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    entradas = [0,0,0,0,0,0,0]
                    for i in var.todos:
                        entradas[i.numero-1] = i.state
                    
                    entrada = np.asarray(entradas)
                    imagen = var.calcular(entrada)
                    

                    cargar_imagen = True

        

        pantalla.fill([0,0,0])

        
        pygame.draw.rect(pantalla,var.Blanco,([Tancho,0],[ancho,alto]),0)
        if cargar_imagen:
            img = pygame.image.load(imagen)
            pantalla.blit(img,[Tancho+20,alto - img.get_rect()[3]-50])        
        
        var.todos.update()
        var.todos.draw(pantalla)

        pygame.display.flip()
        

import pygame as pg
import time

funcionando = True     #Esta variable es para parar pygame cuando terminemos
estado = False         #Esta es para ir cambiando el color del círculo
color = [(220,220,0), (50,50,50)]
pg.init()
screen = pg.display.set_mode((500,500),0,32)
tiempoInicial = time.process_time()*1000

while funcionando:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            funcionando = False 
            break
    tiempoActual = time.process_time()*1000
    if (tiempoActual - tiempoInicial) > 200:
        
        tiempoInicial = time.process_time()*1000
        estado = not(estado)

    screen.fill([100,100,100]) 
   
  
    pg.draw.circle(screen,color[estado]             ,(200,200),70) 
    pg.display.flip()


pg.quit() 

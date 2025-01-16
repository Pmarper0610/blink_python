import pygame as pg
from threading import Timer

funcionando = True     #Esta variable es para parar pygame cuando terminemos
estado = False         #Esta es para ir cambiando el color del círculo
color = [(220,220,0), (50,50,50)]
pg.init()
screen = pg.display.set_mode((500,500),0,32)

def blink():
    global estado
    global t 
    estado = not(estado)
    t = Timer(1, blink)
    t.start ()

t = Timer(1, blink)
t.start()


while funcionando:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            funcionando = False 
            break
   

    screen.fill([100,100,100]) 
   
  
    pg.draw.circle(screen,color[estado],(200,200),70) 
    pg.display.flip()


pg.quit() 

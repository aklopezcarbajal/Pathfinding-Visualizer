"""
Pathfinding visualizer
"""
import pygame

pygame.init()

#Window
W, H = 800,600
win = pygame.display.set_mode((W,H))

NODESIZE = 15
DIST = 5
ROWS, COLS = int(W/(NODESIZE+DIST)), int(H/(NODESIZE+DIST) )
color = (100,155,100)

def draw_grid():
    
    for i in range(1,ROWS):
        for j in range(1,COLS):
            posX = int( i*DIST + (i-1)*NODESIZE + NODESIZE/2)
            posY = int( j*DIST + (j-1)*NODESIZE + NODESIZE/2 )
            pygame.draw.rect(win, color, (posX,posY,NODESIZE,NODESIZE) )
 
running = True
while running:  
    win.fill((100,100,100))
    draw_grid()
    
    pygame.display.update()
            

#TODO:
    #node class
    #create grid
    #implement algorithms
    #UI





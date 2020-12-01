"""
Pathfinding visualizer
"""
import pygame
from node import node

pygame.init()

#Window
W, H = 800,600
win = pygame.display.set_mode((W,H))

NODESIZE = 15
DIST = 5
ROWS, COLS = int(W/(NODESIZE+DIST)), int(H/(NODESIZE+DIST) )
color = (100,155,100)

#TODO:
    #implement algorithms
    #UI
    #index to position function and viceversa
    
def index_to_position(i, j):
    x = int( i*DIST + (i-1)*NODESIZE + NODESIZE/2)
    y = int( j*DIST + (j-1)*NODESIZE + NODESIZE/2 )
    return [x,y]
   

def draw_grid():
    
    for i in range(1,ROWS):
        for j in range(1,COLS):
            position = index_to_position(i, j)
            pygame.draw.rect(win, color, (position[0],position[1],NODESIZE,NODESIZE) )

def create_grid(n, m):
    grid = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(node(i,j))
        grid.append(row)
    return grid
            
def connect_nodes(grid):
    n = len(grid)
    m = len(grid[0])
    
    for i in range(n):
        for j in range(m):
            grid[i][j].find_neighbors(grid)
    
    

running = True
while running:  
    win.fill((100,100,100))
    draw_grid()
    
    pygame.display.update()




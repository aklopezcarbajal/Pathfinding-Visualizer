"""
Pathfinding visualizer
"""
import pygame
import numpy as np
from node import node
from algorithms import Dijkstra

pygame.init()

#Window
W, H = 800,600
win = pygame.display.set_mode((W,H))

NODESIZE = 15
DIST = 5
ROWS, COLS = 10, 5#int(W/(NODESIZE+DIST)), int(H/(NODESIZE+DIST) )
#Colors
green = (100,255,100)
blue  = (100,100,255)
grey  = (50,50,50)

#TODO:
    #implement algorithms
    #UI

def create_grid(n, m):
    grid = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(node(i,j))
        grid.append(row)
    return grid
            
def connect_nodes(grid):
    n = np.size(grid, 0)
    m = np.size(grid, 1)
    
    for i in range(n):
        for j in range(m):
            grid[i][j].find_neighbors(grid)
            
def add_obstacle(position, grid):
    index = position_to_index(position[0], position[1])
    grid[index[0]][index[1]].isObstacle = True
    
def position_to_index(x,y):
    i = int( (y-DIST - NODESIZE/2)/(DIST + NODESIZE) )
    j = int( (x-DIST - NODESIZE/2)/(DIST + NODESIZE) )
    return [i,j]
    
def index_to_position(i, j):
    x = int( (j+1)*DIST + j*NODESIZE + NODESIZE/2 )
    y = int( (i+1)*DIST + i*NODESIZE + NODESIZE/2)
    return [x,y]
   

def draw_grid(grid):
    for i in range(0,ROWS):
        for j in range(0,COLS):
            position = index_to_position(i, j)
            if grid[i][j].isObstacle:
                pygame.draw.rect(win, grey, (position[0],position[1],NODESIZE,NODESIZE) )
            else:
                pygame.draw.rect(win, green, (position[0],position[1],NODESIZE,NODESIZE) )

def draw_path(path):
    for u in path:
        position = index_to_position(u.i, u.j)
        pygame.draw.rect(win, blue, (position[0],position[1],NODESIZE,NODESIZE) )
        
    
"""--------------------------------------------------------"""

G = create_grid(ROWS, COLS)
connect_nodes(G)  
#p = Dijkstra(G, G[0][0], G[3][4])


running = True
while running:  
    win.fill((50,50,80))
    draw_grid(G)
    #draw_path(p)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            add_obstacle([x,y], G)
    
    pygame.display.update()




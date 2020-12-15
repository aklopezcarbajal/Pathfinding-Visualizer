"""
Misc | Pathfinding Visualizer
"""
import pygame
import numpy as np
from node import node

NODESIZE = 15
DIST = 5

#Colors
bg    = (80,80,100)
green = (100,255,100)
blue  = (100,100,255)
darkBlue = (30,30,60)
red   = (255,100,100)
grey  = (130,130,130)
darkGrey = (30,30,30)

def create_grid(n, m):
    grid =[]
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

def add_obstacle(grid, position):
    [i,j] = position_to_index(position[0], position[1])
    
    rows = np.size(grid, 0)
    cols = np.size(grid, 1)
    if 0 <= i and i < rows:
        if 0 <= j and j < cols:
            grid[i][j].isObstacle = True
    
def position_to_index(x,y):
    i = int( (y-DIST - NODESIZE/2)/(DIST + NODESIZE) )
    j = int( (x-DIST - NODESIZE/2)/(DIST + NODESIZE) )
    return [i,j]
    
def index_to_position(i, j):
    x = int( (j+1)*DIST + j*NODESIZE + NODESIZE/2 )
    y = int( (i+1)*DIST + i*NODESIZE + NODESIZE/2)
    return [x,y]
 
def draw_grid(win, grid):
    rows = np.size(grid, 0)
    cols = np.size(grid, 1)
    
    for i in range(0,rows):
        for j in range(0,cols):
            [x,y] = index_to_position(i, j)
            
            pygame.draw.rect(win, grey, (x,y,NODESIZE,NODESIZE) )
            
            if grid[i][j].isObstacle:
                pygame.draw.rect(win, darkGrey, (x,y,NODESIZE,NODESIZE) )
            else:
                if grid[i][j].inQueue:
                    pygame.draw.circle(win, blue, (x +NODESIZE/2,y +NODESIZE/2), NODESIZE/2 - 1)
                if grid[i][j].visited:
                    pygame.draw.rect(win, darkBlue, (x,y,NODESIZE,NODESIZE) )
        
    pygame.display.update()


def draw_path(win, path):
    for u in path:
        position = index_to_position(u.i, u.j)
        if u == path[0] or u == path[-1]:
            pygame.draw.rect(win, red, (position[0],position[1],NODESIZE,NODESIZE) )
        else:
            pygame.draw.rect(win, blue, (position[0],position[1],NODESIZE,NODESIZE) )
 
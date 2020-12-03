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
ROWS, COLS = 15, 25#int(W/(NODESIZE+DIST)), int(H/(NODESIZE+DIST) )
color = (100,155,100)
grey  = (50,50,50)

#TODO:
    #implement algorithms
    #UI
    #index to position function and viceversa


def create_grid(n, m):
    grid = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(node(i,j))
        grid.append(row)
    return grid
            
def connect_nodes(grid):
    n = len(grid)
    m = len(grid[0])
    
    for i in range(n):
        for j in range(m):
            grid[i][j].find_neighbors(grid)
            
#def add_obstacle(position, grid):
    #position to index
    #grid[i][i].isObstacle
    
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
                pygame.draw.rect(win, color, (position[0],position[1],NODESIZE,NODESIZE) )
            if len(grid[i][j].neighbors) > 0:
                pygame.draw.rect(win, (200,100,100), (position[0],position[1],NODESIZE,NODESIZE) )
                
    
"""--------------------------------------------------------"""

G = create_grid(ROWS, COLS)
G[3][5].isObstacle = True    
G[5][15].isObstacle = True    
G[10][10].isObstacle = True
connect_nodes(G)  


running = True
while running:  
    win.fill((100,100,100))
    draw_grid(G)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()




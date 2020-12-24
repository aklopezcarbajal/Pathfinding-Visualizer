"""
Pathfinding visualizer
"""
import pygame
import numpy as np
from algorithms import *
from misc import *

pygame.init()

#Window
W, H = 800,600
win = pygame.display.set_mode((W,H))

ROWS, COLS = 3, 5#int(W/(NODESIZE+DIST)), int(H/(NODESIZE+DIST) )
  
"""--------------------------------------------------------"""

G = create_grid(ROWS, COLS)
connect_nodes(G)  
#Obstacle
"""
G[1][2].isObstacle = True
G[2][2].isObstacle = True
G[3][2].isObstacle = True
G[4][2].isObstacle = True
G[4][1].isObstacle = True
G[4][0].isObstacle = True
"""
test = [ [i for i in range(COLS)] for j in range(ROWS)  ]
print(test)

start = G[0][0]
end   = G[2][3]

running = True
while running:  
    win.fill(bg)
    draw_grid(win, G)
    #draw_path(win, p)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            #make_maze(win,G)
            #bfs(win,G,start,end)
            #Dijkstra(win, G, start)
            Astar(win,G,start,end)
            #path = return_path(G, start, end)
            x, y = event.pos
            add_obstacle(G, [x,y])
    
    pygame.display.update()




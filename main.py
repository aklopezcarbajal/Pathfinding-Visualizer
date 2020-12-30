"""
Pathfinding visualizer
"""
import pygame
import numpy as np
from algorithms import *
from misc import *
from UI import *

pygame.init()

#Window
W, H = 800,600
win = pygame.display.set_mode((W,H))

ROWS, COLS = 10, 10#int(W/(NODESIZE+DIST)), int(H/(NODESIZE+DIST) )

#Buttons
buttonWidth, buttonHeight = 80, 50
buttons = []
bfs_button = button( [10,10], buttonWidth, buttonHeight, 'Check this font' )
buttons.append(bfs_button)
dfs_button = button( [20+buttonWidth,10], buttonWidth, buttonHeight, 'DFS' )
buttons.append(dfs_button)
Astar_button = button( [10 +2*(10+buttonWidth),10], buttonWidth, buttonHeight, 'A*' )
buttons.append(Astar_button)
maze_button = button( [10+ 3*(10+buttonWidth),10], buttonWidth, buttonHeight, 'Maze' )
buttons.append(maze_button)

fonts = pygame.font.get_fonts()
"""--------------------------------------------------------"""

G = create_grid(ROWS, COLS)
connect_nodes(G)  
#Obstacle

G[1][2].isObstacle = True
G[2][2].isObstacle = True
G[3][2].isObstacle = True
G[4][2].isObstacle = True
G[4][1].isObstacle = True
G[4][0].isObstacle = True

start = G[0][0]
end   = G[7][3]

def show_buttons():
    for b in buttons:
        b.draw(win)

running = True
while running:  
    win.fill(bg)
    #draw_grid(win, G)
    show_buttons()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            #make_maze(win,G)
            #dfs(win,G,start,end)
            #Dijkstra(win, G, start)
            #Astar(win,G,start,end)
            #get_path(G, start, end)
            
            x, y = event.pos
            add_obstacle(G, [x,y])
    
    pygame.display.update()




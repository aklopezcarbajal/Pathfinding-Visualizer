"""
Pathfinding visualizer
"""
import pygame
import numpy as np
from algorithms import *
from UI import *

pygame.init()

#Window
W, H = 800,600
win = pygame.display.set_mode((W,H))

ROWS, COLS = 25, 35#int(W/(NODESIZE+DIST)), int(H/(NODESIZE+DIST) )

#Buttons
buttonWidth, buttonHeight = 80, 35
bfs_button      = button( [10,10], buttonWidth, buttonHeight, 'BFS' )
dfs_button      = button( [20+buttonWidth,10], buttonWidth, buttonHeight, 'DFS' )
Dijkstra_button = button( [10+ 2*(10+buttonWidth),10], buttonWidth, buttonHeight, 'Dijkstra' )
Astar_button    = button( [10 +3*(10+buttonWidth),10], buttonWidth, buttonHeight, 'A*' )
maze_button     = button( [10 +4*(10+buttonWidth),10], buttonWidth, buttonHeight, 'Maze' )
reset_button    = button( [10 +5*(10+buttonWidth),10], buttonWidth, buttonHeight, 'Reset' )

buttons = [bfs_button, dfs_button, Dijkstra_button, Astar_button, maze_button, reset_button]

fonts = pygame.font.get_fonts()
"""--------------------------------------------------------"""
#Initialize grid
grid = create_grid(ROWS, COLS)
connect_nodes(grid)  
startNode, endNode = None, None

running = True
while running:  
    update_window(win, buttons, grid)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            
            #Check buttons
            if bfs_button.isPressed(x,y):
                if not startNode or not endNode:
                    show_message()
                else:
                    bfs(win,grid,startNode,endNode)
                    get_path(grid, startNode, endNode)
            if dfs_button.isPressed(x,y):
                if not startNode or not endNode:
                    show_message()
                else:
                    dfs(win,grid,startNode,endNode)
                    get_path(grid, startNode, endNode)
            if Dijkstra_button.isPressed(x,y):
                if not startNode or not endNode:
                    show_message()
                else:
                    Dijkstra(win, grid, startNode)
                    get_path(grid, startNode, endNode)
            if Astar_button.isPressed(x,y):
                if not startNode or not endNode:
                    show_message()
                else:
                    Astar(win,grid,startNode,endNode)
                    get_path(grid, startNode, endNode)
            if maze_button.isPressed(x,y):
                startNode, endNode = make_maze(win,grid)
            if reset_button.isPressed(x,y):
                reset_grid(grid)
                startNode, endNode = None, None
            
            onGrid = grid_click(grid, [x,y])
            
            if onGrid:
                if startNode and endNode:
                    set_obstacle(grid, [x,y])
                if startNode and not endNode:
                    endNode = set_end(grid, [x,y])
                if not startNode:
                    startNode = set_start(grid, [x,y])




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

ROWS, COLS = 28, 40#int(W/(NODESIZE+DIST)), int(H/(NODESIZE+DIST) )

#Buttons
buttonWidth, buttonHeight = 70, 35
buttons = []
bfs_button = button( [10,10], buttonWidth, buttonHeight, 'BFS' )
buttons.append(bfs_button)
dfs_button = button( [20+buttonWidth,10], buttonWidth, buttonHeight, 'DFS' )
buttons.append(dfs_button)
Astar_button = button( [10 +2*(10+buttonWidth),10], buttonWidth, buttonHeight, 'A*' )
buttons.append(Astar_button)
maze_button = button( [10+ 3*(10+buttonWidth),10], buttonWidth, buttonHeight, 'Maze' )
buttons.append(maze_button)

fonts = pygame.font.get_fonts()
"""--------------------------------------------------------"""

grid = create_grid(ROWS, COLS)
connect_nodes(grid)  
#Obstacle
"""
grid[1][2].isObstacle = True
grid[2][2].isObstacle = True
grid[3][2].isObstacle = True
grid[4][2].isObstacle = True
grid[4][1].isObstacle = True
grid[4][0].isObstacle = True
"""
start = grid[0][0]
end   = grid[7][3]

startNode, endNode = None, None
alg = None

running = True
while running:  
    update_window(win, buttons, grid)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            
            #bfs(win,grid,start,end)
            #make_maze(win,grid)
            #dfs(win,grid,start,end)
            #Dijkstra(win, grid, start)
            #Astar(win,grid,start,end)
            #get_path(grid, start, end)
            
            node = node_click(grid, [x,y])
            print(node.i,node.j)
            if node:
                if node.isStart:
                    node.isStart = False
                    startNode = None
                if startNode == None:
                    startNode = node
                    node.isStart = True
                if startNode and endNode == None:
                    endNode = node
                    node.isEnd = True




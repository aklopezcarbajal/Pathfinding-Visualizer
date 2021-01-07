"""
Pathfinding visualizer
--------------------------------------------------------
How to:
    - Select start node
    - Select target node
    - Add obstacles
    - Choose an algorithm
    or
    - Select Maze
    - Choose an algorithm
"""
import pygame
import sys
from algorithms import *
from UI import *

pygame.init()

#Window
W, H = 740, 600
win = pygame.display.set_mode((W,H))
pygame.display.set_caption("Pathfinding Visualizer")

#Buttons
buttonWidth, buttonHeight = 80, 35
bfs_button      = button( [10,10], buttonWidth-10, buttonHeight, 'BFS' )
dfs_button      = button( [10+buttonWidth,10], buttonWidth-10, buttonHeight, 'DFS' )
Dijkstra_button = button( [10 +2*buttonWidth,10], buttonWidth+20, buttonHeight, 'Dijkstra' )
Astar_button    = button( [10 +3*(10+buttonWidth),10], buttonWidth, buttonHeight, 'A*' )
maze_button     = button( [10 +4*(10+buttonWidth),10], buttonWidth, buttonHeight, 'Maze' )
reset_button    = button( [10 +5*(10+buttonWidth),10], buttonWidth, buttonHeight, 'Reset' )
reset_button.set_color('button','#EDC7B7')
reset_button.set_color('font','#AC3B61')

buttons = [bfs_button, dfs_button, Dijkstra_button, Astar_button, maze_button, reset_button]

#Initialize grid
rows, cols = 30, 40
grid = create_grid(rows, cols)
connect_nodes(grid)  
startNode, endNode = None, None

"""--------------------------------------------------------"""

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
                    show_message('info')
                else:
                    bfs(win,grid,startNode,endNode)
                    if not get_path(grid, startNode, endNode):
                        show_message('error')
            if dfs_button.isPressed(x,y):
                if not startNode or not endNode:
                    show_message('info')
                else:
                    dfs(win,grid,startNode,endNode)
                    if not get_path(grid, startNode, endNode):
                        show_message('error')
            if Dijkstra_button.isPressed(x,y):
                if not startNode or not endNode:
                    show_message('info')
                else:
                    Dijkstra(win, grid, startNode)
                    if not get_path(grid, startNode, endNode):
                        show_message('error')
            if Astar_button.isPressed(x,y):
                if not startNode or not endNode:
                    show_message('info')
                else:
                    Astar(win,grid,startNode,endNode)
                    if not get_path(grid, startNode, endNode):
                        show_message('error')
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
                
pygame.quit()
sys.exit()



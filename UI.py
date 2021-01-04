"""
UI | Pathfinding Visualizer
"""
import pygame
import numpy as np
from node import node
from tkinter import *
from tkinter import messagebox

#Background
background = '#EEE2DC'#55708D'

#Buttons
button_color = '#B0A8AB'#4E6E91'
font_color = '#2F4454'

#Grid
grid_position = [0,40]
NODESIZE = 15
DIST = 3

unvisited_color = '#BAB2B5'
visited_color = '#123C69'
inQueue_color = '#374785'
path_color = '#AC3B61'
obstacle_color = '#112636'


def update_window(win, buttons, grid):
    win.fill(background)
    
    for b in buttons:
        b.draw(win)
        
    draw_grid(win, grid)
    #pygame.display.update()

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

def grid_click(grid, position):
    rows = np.size(grid, 0)
    cols = np.size(grid, 1)
    
    w, h = grid_position[0] + (NODESIZE + DIST)*cols, grid_position[1] + (NODESIZE + DIST)*rows
    
    
    if grid_position[0] <= position[0] and position[0] < w:
        if grid_position[1] <= position[1] and position[1] < h:
            return True
    return False

def set_start(grid, position):
    [i,j] = position_to_index(position[0], position[1])
    if not grid[i][j].isEnd and not grid[i][j].isObstacle:
        grid[i][j].isStart = True
        return grid[i][j]

def set_end(grid, position):
    [i,j] = position_to_index(position[0], position[1])
    if not grid[i][j].isStart and not grid[i][j].isObstacle:
        grid[i][j].isEnd = True
        return grid[i][j]

def set_obstacle(grid, position):
    [i,j] = position_to_index(position[0], position[1])
    if grid[i][j].isObstacle:
        grid[i][j].isObstacle = False
    elif not grid[i][j].isStart and not grid[i][j].isEnd:
        grid[i][j].isObstacle = True
    
def position_to_index(x,y):
    x -= grid_position[0]
    y -= grid_position[1]
    i = int( (y-DIST - NODESIZE/2)/(DIST + NODESIZE) )
    j = int( (x-DIST - NODESIZE/2)/(DIST + NODESIZE) )
    return [i,j]
    
def index_to_position(i, j):
    x = int( (j+1)*DIST + j*NODESIZE + NODESIZE/2 )
    y = int( (i+1)*DIST + i*NODESIZE + NODESIZE/2)
    return [x + grid_position[0],y + grid_position[1]]


def draw_grid(win, grid):
    rows = np.size(grid, 0)
    cols = np.size(grid, 1)
    
    for i in range(0,rows):
        for j in range(0,cols):
            [x,y] = index_to_position(i, j)
            
            pygame.draw.rect(win, unvisited_color, (x,y,NODESIZE,NODESIZE) )
            
            if grid[i][j].isObstacle:
                pygame.draw.rect(win, obstacle_color, (x,y,NODESIZE,NODESIZE) )
            if grid[i][j].isStart:
                pygame.draw.polygon(win, '#253A4A',( (x+1,y), (x+NODESIZE -1, y+NODESIZE/2), (x+1,y+NODESIZE) ) )
            if grid[i][j].isEnd:
                pygame.draw.circle(win, '#253A4A', (x +NODESIZE/2,y +NODESIZE/2), int(NODESIZE/2) - 1)
            if not grid[i][j].isStart and not grid[i][j].isEnd and not grid[i][j].isObstacle:
                if grid[i][j].inQueue:
                    pygame.draw.circle(win, inQueue_color, (x +NODESIZE/2,y +NODESIZE/2), NODESIZE/2 - 1)
                if grid[i][j].visited:
                    pygame.draw.rect(win, visited_color, (x,y,NODESIZE,NODESIZE) )
                if grid[i][j].isOnPath:
                    pygame.draw.rect(win, path_color, (x,y,NODESIZE,NODESIZE) )
    pygame.display.update()

def reset_grid(grid):
    rows = np.size(grid, 0)
    cols = np.size(grid, 1)
    
    for i in range(rows):
        for j in range(cols):
            grid[i][j].reset()
    
def show_message():
    Tk().wm_withdraw() #to hide the main window
    messagebox.showinfo('Continue','Please select a start node and an end node')
            

#---------- Button class ----------
class button():
    def __init__(self, position, width, height, text=''):
        self.color = button_color
        self.x = position[0]
        self.y = position[1]
        self.width = width
        self.height = height
        self.text = text
        
    def draw(self,win):
        #pygame.draw.rect(win, outline_color, (self.x-2,self.y-2,self.width+4,self.height+4),0)
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),border_radius=5)
        
        if self.text != '':
            font = pygame.font.SysFont('arial', 20)
            text = font.render(self.text, 1, font_color)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isPressed(self, x, y):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if x > self.x and x < self.x + self.width:
            if y > self.y and y < self.y + self.height:
                print("button pressed")
                return True
            
        return False
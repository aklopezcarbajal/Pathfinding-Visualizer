"""
Node class | Pathfinding Visualizer
"""
import sys
import numpy as np

class node:
    def __init__(self, row, col):
        self.i = row
        self.j = col
        self.parent    = None
        self.neighbors = []
        self.visited   = False
        self.inQueue   = False
        self.distance  = sys.maxsize
        
        self.isObstacle = False
        self.isOnPath   = False
        
    def find_neighbors(self, grid):
        if self.isObstacle:
            return
        rows = np.size(grid, 0)
        cols = np.size(grid, 1)
        if self.i > 0:
            self.neighbors.append(grid[self.i-1][self.j])
        if self.i < rows-1:
            self.neighbors.append(grid[self.i+1][self.j])
        if self.j > 0:
            self.neighbors.append(grid[self.i][self.j-1])
        if self.j < cols-1:
            self.neighbors.append(grid[self.i][self.j+1])
            
        
        
        
    

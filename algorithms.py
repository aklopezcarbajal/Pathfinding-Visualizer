"""
Pathfinding Algorithms
"""
import numpy as np
from node import node
from collections import deque

def return_path(grid, start, end):
    path = []
    u = end
    while u.parent != None:
        path.append(u)
        u = u.parent
    path.append(u)
    return path
        

def Dijkstra(grid, start, end):
    queue = deque([start])
    
    while len(queue) > 0:
        u = queue.popleft()
        #if u == end --> find path and return
        for v in u.neighbors:
            if v.visited == False and v.isObstacle == False:
                queue.append(v)
                v.parent = u
                u.visited = True
    return return_path(grid, start, end)
    
    
    
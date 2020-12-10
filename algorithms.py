"""
Pathfinding Algorithms
"""
import numpy as np
from collections import deque
from queue import PriorityQueue

def return_path(grid, start, end):
    path = []
    u = end
    while u.parent != None:
        path.append(u)
        u = u.parent
    path.append(u)
    return path
        

def bfs(start, end):
    queue = deque([start])
    
    while len(queue) > 0:
        u = queue.popleft()
        #if u == end --> find path and return
        for v in u.neighbors:
            if v.visited == False and v.isObstacle == False:
                queue.append(v)
                v.parent = u
        u.visited = True
    
def dfs_visit(u,end):
    u.inQueue = True
    for v in u.neighbors:
        if not v.visited and not v.inQueue:
            v.parent = u
            if v == end:
                return
            dfs_visit(v, end)
    u.visited = True
    u.inQueue = False

#We need to create an id to insert the nodes in the priority queue
def node_id(node):
    istr = str(node.i)
    jstr = str(node.j)
    return [istr,jstr]

def get_node(grid, index):
    i = int(index[0])
    j = int(index[1])
    return grid[i][j]
    
#In this case, the grid has equal weight on every edge
def Dijkstra(grid, s):
    queue = PriorityQueue()
    queue.put((0, node_id(s)))
    s.distance = 0
    
    while not queue.empty():
        u_id = queue.get()[1]
        u = get_node(grid,u_id)
        
        for v in u.neighbors:
            if v.visited == False and v.isObstacle == False:
                dist = u.distance + 1
                if v.distance > dist:
                    v.distance = dist
                    v.parent = u
                    queue.put((v.distance, node_id(v)))
        u.visited = True
        
        
    
    


    
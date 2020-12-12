"""
Pathfinding Algorithms
"""
import numpy as np
from collections import deque
from queue import PriorityQueue
from misc import *

def return_path(grid, start, end):
    path = []
    u = end
    while u.parent != None:
        path.append(u)
        u = u.parent
    path.append(u)
    return path
        

def bfs(win, grid, start, end):
    queue = deque([start])
    
    while len(queue) > 0:
        u = queue.popleft()
        #if u == end --> find path and return
        for v in u.neighbors:
            if not v.visited and not v.isObstacle and not v.inQueue:
                queue.append(v)
                v.parent = u
                v.inQueue = True
                draw_grid(win,grid)
        u.visited = True
        u.inQueue = False
        draw_grid(win,grid)
    
def dfs_visit(u,end):
    u.inQueue = True
    for v in u.neighbors:
        if not v.visited and not v.isObstacle and not v.inQueue:
            v.parent = u
            if v == end:
                return
            dfs_visit(v, end)
    u.visited = True
    u.inQueue = False

#We need to create an id to insert the nodes in the priority queue
def node_id(node):
    return (node.i, node.j)

def get_node(grid, pair):
    i = pair[0]
    j = pair[1]
    return grid[i][j]
    
#In this case, the grid has equal weight on every edge
def Dijkstra(win, grid, s):
    queue = PriorityQueue()
    queue.put((0, node_id(s)))
    s.distance = 0
    
    while not queue.empty():
        u_id = queue.get()[1]
        u = get_node(grid,u_id)
        
        for v in u.neighbors:
            if not v.visited and not v.isObstacle and not v.inQueue:
                dist = u.distance + 1
                if v.distance > dist:
                    v.distance = dist
                    v.parent = u
                    queue.put((v.distance, node_id(v)))
                    v.inQueue = True
                    draw_grid(win,grid)
                    
        u.visited = True
        v.inQueue = False
        draw_grid(win,grid)

#Distance to the start node (Manhattan Distance)
def g(s, u):
    return abs(s.i - u.i) + abs(s.j - u.j)

#Distance to the end node (Manhattan Distance)
def h(e, u):
    return abs(e.i - u.i) + abs(e.j - u.j)

def f(u, start, end):
    return g(start,u) + h(end,u)
  
def Astar(grid, start, end):
    queue = PriorityQueue()
    queue.put((0, node_id(start)))
    
    while not queue.empty():
        u_id = queue.get()[1]
        u = get_node(grid,u_id)
        
        if u == end:
            return
        
        for v in u.neighbors:
            if v.visited == False and v.isObstacle == False:
                return
    


    
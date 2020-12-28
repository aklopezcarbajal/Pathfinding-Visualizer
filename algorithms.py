"""
Pathfinding Algorithms
"""
import sys
import numpy as np
import random
from collections import deque
from queue import PriorityQueue
from misc import *

def get_path(grid, start, end):
    path = []
    u = end
    while u.parent != None:
        u.isOnPath = True
        path.append(u)
        u = u.parent
    
    u.isOnPath = True
    path.append(u)
    
def valid(u):
    if not u.visited and not u.isObstacle and not u.inQueue:
        return True
    return False
    
def bfs(win, grid, start, end):
    queue = deque([start])
    
    while len(queue) > 0:
        u = queue.popleft()
        
        if u == end:
            return
        for v in u.neighbors:
            if valid(v):
                queue.append(v)
                v.parent = u
                v.inQueue = True
                draw_grid(win,grid)
        u.visited = True
        u.inQueue = False
        draw_grid(win,grid)
    
def dfs(win, grid, u, end):
    if u == end:
        return
    
    u.inQueue = True
    for v in u.neighbors:
        if valid(v):
            v.parent = u
            dfs(win, grid, v, end)
    u.visited = True
    u.inQueue = False
    draw_grid(win,grid)

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
            if valid(v):
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

 #Distance to the end node (Manhattan Distance)
def h(u, e):
    return abs(e.i - u.i) + abs(e.j - u.j)
 
def Astar(win, grid, start, end):
    queue = PriorityQueue()
    openSet = set([])    
    
    n = np.size(grid, 0)
    m = np.size(grid, 1)
    g = [ [sys.maxsize for i in range(m)] for j in range(n)  ]
    f = [ [sys.maxsize for i in range(m)] for j in range(n)  ]
    
    order = 0
    queue.put((0, order, node_id(start)))
    openSet.add(start)
    
    g[start.i][start.j] = 0
    f[start.i][start.j] = h(start, end)
    
    while not queue.empty():
        u = get_node(grid, queue.get()[2])
        openSet.remove(u)
        u.visited = True
        u.inQueue = False
        
        draw_grid(win, grid)
        
        if u == end:
            return
        
        for v in u.neighbors:
            if not v.visited and not v.isObstacle:
                cost = g[u.i][u.j] + 1
                
                if cost < g[v.i][v.j]:
                    g[v.i][v.j] = cost
                    f[v.i][v.j] = g[v.i][v.j] + h(v,end)
                    v.parent = u
                    
                    if v not in openSet:
                        order += 1
                        queue.put((f[v.i][v.j], order, node_id(v)))
                        openSet.add(v)
                        v.inQueue = True
                        draw_grid(win, grid)                  
                        

#Randomized Prim's Alg
def make_maze(win, grid):
    n = np.size(grid, 0)
    m = np.size(grid, 1)
    #Start with a grid full of walls
    for i in range(n):
        for j in range(m):
            grid[i][j].isObstacle = True
    #Pick a cell, mark it as part of the maze. Add the walls of the cell to the wall list.
    s = grid[random.randrange(n)][random.randrange(m)]
    s.visited = True
    s.isObstacle = False
    
    wall_list = []
    for v in s.neighbors:
        wall_list.append(v)
    #While there are walls in the list:
    while len(wall_list) > 0:
        draw_grid(win,grid)
        #Choose a random node from the list
        randi = random.randrange(len(wall_list) )
        u = wall_list[randi]
        
        #Pick a random wall from the list. If only one of the two cells that the wall divides is visited, then:
            #Make the wall a passage and mark the unvisited cell as part of the maze.
            #Add the neighboring walls of the cell to the wall list.
        #Remove the wall from the list.

    
# Pathfinding Visualizer

This pygame application finds a path between two given nodes in a grid.

<img src="/imgs/pathfinding_bfs.png" alt="Pathfinding Visualizer" width="400" height="300"/>

## Algorithms
<ul>
  <li> <b> Breadth First Search </b> : Explores each of the neighbor nodes before going on to the next depth level.</li>
  <li> <b> Depth First Search </b> : Explores each branch completely before going on to the next branch. Does not guarantee shortest path. </li>
  <li> <b> Dijkstra </b> : Finds shortest path from the source to every node in the grid. At each step, it selects the node with the minimum distance from the source. </li>
  <li> <b> A* </b> : Finds the shortest path. 
	At each step, it selects the node u with the smallest f(u) value, 
	where f(u) is the sum of
   <ul>
      <li>- g(u) = the cost from the source to the node u</li>
      <li>- h(u) = an estimation of the cost from u to the target node</li>
  </ul>
	</li>
  <li> <b> Maze Generator </b> : Creates a maze using Randomized Prim's algorithm. It automatically selects an entrance and an exit.</li>
</ul>
 <img src="/imgs/pathfinding_astar.png" alt="Astar algorithm" width="400" height="300" style="float:right"/>
 
## How to:
<ol>
  <li>Select start node</li>
  <li>Select target node</li>
  <li>Add obstacles</li>
  <li>Choose an algorithm</li>
</ol>
or
<ol>
  <li>Generate a maze </li>
  <li>Choose an algorithm</li>
</ol>

<img src="/imgs/pathfinding_maze.gif" alt="Demo" width="400" height="300" style="float:right"/>

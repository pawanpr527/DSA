'''BFS (Breadth First Search)
Travsing graph has only issue that graph may have cycle, You may revisit a Node
To avoid processing a node more than once, we divide the vertics into two categories:
1. Visited
2. Unvisited

We start from a vertice, and mark it as visited, then we add all the adjacent vertics to the queue
and mark them as visited.

We repeat this process until the queue is empty.

'''
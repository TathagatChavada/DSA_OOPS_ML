from collections import deque

# BFS implementation using adjacency list
def bfs(graph,start):
    
    visited = set()
    queue = deque()
    
    visited.add(start)
    queue.append(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end = ' ')
        
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                
    
graph2 = {0: [1, 2], 
      1: [2], 
      2: [3], 
      3: [1, 2]}

print("Breadth First Search")
bfs(graph2, 0)
from collections import deque

# DFS implementation using adjacency list
def dfs(graph, start, visited):
    
    # Mark the current node as visited
    visited[start] = True
    print(start, end=' ')

    # Recur for all the vertices adjacent to the current node
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)


# Example graph represented as an adjacency list
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1, 4, 5],
    4: [1, 2, 3, 5],
    5: [3, 4]
}

# Create a list to track visited nodes
visited = [False] * len(graph)

# Call the DFS function with the graph, starting node, and visited list
print("Depth First search")
dfs(graph, 0, visited)
print('\n')



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
from collections import defaultdict

class Graph:
    
    def __init__(self) -> None:
        self.graph = defaultdict(list)
        self.visited = set()
        
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
    

    def dfs(self, v):
        self.visited.add(v)
        print(v, end=' ')

        # Recur for all the vertices adjacent to the current node
        for next in self.graph[v]:
            if next not in self.visited:
                self.dfs(next)



g = Graph()

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 4)
g.addEdge(3, 0)
g.addEdge(4, 2)


print("Depth First search: ")
g.dfs(2)
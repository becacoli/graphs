class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * self.V for _ in range(self.V)]
 
    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w
 
    def prim(self):
       
        visited = [False] * self.V
 
       
        key = [float('inf')] * self.V
       
        key[0] = 0

        parent = [None] * self.V
        parent[0] = -1
 
        for _ in range(self.V):
            
            u = min((key[i], i) for i in range(self.V) if not visited[i])[1]
            visited[u] = True
    
            for v in range(self.V):
                if self.graph[u][v] and not visited[v] and self.graph[u][v] < key[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
 
        for i in range(1, self.V):
            print(f"Edge: {parent[i]} - {i} Weight: {self.graph[i][parent[i]]}")

def main():
    
    g = Graph(5)

    g.add_edge(0, 1, 2)
    g.add_edge(0, 3, 6)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 8)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 4, 7)
    g.add_edge(3, 4, 9)

    g.prim()


main()
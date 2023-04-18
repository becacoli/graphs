from math import inf

class Graph:
    n = 0
    matrix = 0

    # constructor
    def __init__(self, n):
        self.n = n
        self.matrix = [[0 for i in range(n)] for j in range(n)]

    # printing
    def __str__(self):
        graph = ''
        for i in range(self.n):
            for j in range(self.n):
                graph += str(self.matrix[i][j])+' '
            graph += '\n'
        return graph

    # inserting
    def add_edge(self, vi, vj, w):
        self.matrix[vi][vj] = w

    # removing
    def remove_edge(self, vi, vj):
        self.matrix[vi][vj] = 0

    def get_vertices(self):
        return [i for i in range(self.n)]

    def get_neighbors(self, vi):
        neighbors = []
        for vj in range(self.n):
            if vi != vj and self.matrix[vi][vj] != 0:
                neighbors.append(vj)
        return neighbors

def dijkstra(g):
    n = g.n
    # initialization of the algorithm
    distances = [inf] * n
    routes = [0] * n
    visited = [0] * n
    visited[0] = 1
    distances[0] = 0
    v = 0

    # algorithm
    for r in range(n-1):
        # check its neighbors and update distances for those neighbors
        for i in range(n):
            if g.matrix[v][i] != 0 and distances[v] + g.matrix[v][i] < distances[i]:
                distances[i] = distances[v] + g.matrix[v][i]
                routes[i] = v

        # get the neighbor with minimum distance not yet visited and add to the route
        min_d = inf
        min_i = 0
        for i in range(n):
            if visited[i] == 0 and distances[i] < min_d:
                min_d = distances[i]
                min_i = i
        visited[min_i] = 1
        v = min_i

    return distances, visited, routes


def main():
  

  g = Graph(5)

  g.add_edge(0, 1, 5)
  g.add_edge(0, 2, 10)
  g.add_edge(1, 2, 3)
  g.add_edge(1, 3, 2)
  g.add_edge(1, 4, 9)
  g.add_edge(2, 1, 2)
  g.add_edge(2, 4, 1)
  g.add_edge(3, 0, 7)
  g.add_edge(3, 4, 6)
  g.add_edge(4, 3, 4)

  print(g)

  distances, visited, routes = dijkstra(g)
  print(distances, visited, routes)



main()
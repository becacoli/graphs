# THE ROWS ARE THE EDGES AND THE COLUMNS ARE THE VERTICES
class Graph:
    def __init__(self, n_vertices, n_edges):
        self.n_edges = n_edges
        self.n_vertices = n_vertices
        self.matrix = [[0 for _ in range(n_edges)] for _ in range(n_vertices)]

    def __str__(self):
        graph = ''
        for i in range(self.n_vertices):
            for j in range(self.n_edges):
                graph += str(self.matrix[i][j]) + ' '
            graph += '\n'
        return graph

    def add_edge(self, vi, vj, e):
        self.matrix[vi][e] += 1
        self.matrix[vj][e] += 1

    def remove_edge(self, vi, vj, e):
        self.matrix[vi][e] -= 1
        self.matrix[vj][e] -= 1

    def has_edge(self, vi, vj, e):
        return self.matrix[vi][e] != 0 and self.matrix[vj][e] != 0

    def get_edge_between_vertices(self, vi, vj):
        for e in range(self.n_edges):
            if self.has_edge(vi, vj, e):
                return e
        return -1

    # number of edges incident on a vertex
    def get_degree_of_vertex(self, vertex):
        degree = 0
        for e in range(self.n_edges):
            degree += self.matrix[vertex][e]
        return degree

    # sum of the degree of all vertices (or twice the number of edges), the degree will always be an even number
    def get_degree_of_graph(self):
        degree = 0
        for v in range(self.n_vertices):
            degree += self.get_degree_of_vertex(v)
        return degree

    def has_loop(self):
        for v in range(self.n_vertices):
            for e in range(self.n_edges):
                if self.matrix[v][e] > 1:
                    return True
        return False

    def has_parallel_edges(self):
        # Check for parallel edges
        for e1 in range(self.n_edges - 1):
            for e2 in range(e1 + 1, self.n_edges):
                edges1 = [self.matrix[v][e1] for v in range(self.n_vertices)]
                edges2 = [self.matrix[v][e2] for v in range(self.n_vertices)]
                if edges1 == edges2:
                    return True
        return False

    def is_simple(self):
        # Check if the graph is simple
        if self.has_loop() or self.has_parallel_edges():
            return False
        return True

    # complete graph - every vertex is adjacent to every other vertex
    def is_complete(self):
        for i in range(self.n_vertices):
            for j in range(i + 1, self.n_vertices):
                if not self.has_edge(i, j, 0):
                    return False
        return True

    def is_bipartite(self):
        colors = [0 for i in range(self.n_vertices)]
        colors[0] = 1
        queue = []
        queue.append(0)
        while queue:
            v = queue.pop(0)
            for u in range(self.n_vertices):
                if self.matrix[v][u] != 0:
                    if colors[u] == 0:
                        colors[u] = 3 - colors[v]
                        queue.append(u)
                    elif colors[u] == colors[v]:
                        return False
        return True

    def is_subgraph(smaller_graph, larger_graph):
        if smaller_graph.n_vertices > larger_graph.n_vertices or smaller_graph.n_arestas > larger_graph.n_arestas:
            return False
    
        for v1 in range(smaller_graph.n_vertices):
            for v2 in range(v1+1, smaller_graph.n_vertices):
                edge = smaller_graph.get_aresta_entre_vertices(v1, v2)
                if edge == -1 or not larger_graph.existe_aresta(v1, v2, edge):
                    return False
            
        return True
    
def main():
    # create a graph
    g = Graph(3, 3)
    g.add_edge(0, 1, 0)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 2, 2)

    # print the graph
    print("Graph:")
    print(g)

    # check if the graph is simple
    print("Is the graph simple?")
    print(g.is_simple())

    # check if the graph is complete
    print("Is the graph complete?")
    print(g.is_complete())

    # check if the graph is bipartite
    print("Is the graph bipartite?")
    print(g.is_bipartite())

    # create a smaller graph
    sg = Graph(2, 2)
    sg.add_edge(0, 1, 0)
    sg.add_edge(0, 1, 1)

    # check if the smaller graph is a subgraph of the larger graph
    print("Is the smaller graph a subgraph of the larger graph?")
    print(g.is_subgraph(sg))

main()

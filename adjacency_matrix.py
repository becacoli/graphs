class Graph:
    def __init__(self,n):
        self.n = n
        self.matrix = [[0 for i in range(n)] for j in range(n)]

    def __str__(self):
        graph = ""
        for i in range(self.n):
            for j in range(self.n):
                graph += str(self.matrix[i][j]) + " "
            graph += "\n"
        return graph

    def add_edge(self, v1, v2):
        self.matrix[v1][v2] += 1
        self.matrix[v2][v1] += 1

    def remove_edge(self, v1, v2):
        self.matrix[v1][v2] -= 1
        self.matrix[v2][v1] -= 1

    def edge_exists(self, vi, vj):
        return self.matrix[vi][vj] > 0

    def get_degree_of_vertex(self, vertex):
        degree = 0
        for v in range(self.n):
            degree += self.matrix[v][vertex]
        return degree

    def get_degree_of_graph(self):
        degree = 0
        for v in range(self.n):
            degree += self.get_degree_of_vertex(v)
        return degree

    def has_loop(self):
        for i in range(self.n):
            if self.matrix[i][i] != 0:
                return True
        return False

    def has_parallel_edges(self):
        for i in range(self.n):
            for j in range(i+1, self.n):
                if self.matrix[i][j] > 1:
                    return True
        return False

    def is_simple(self):
        return not self.has_loop() and not self.has_parallel_edges()

    def is_bipartite(g):
        n = g.n
        color = [None]*n
        color[0] = 0
        print(color)
        for i in range(n-1):
            for j in range(i+1,n):
                if g.matrix[i][j] == 1: 
                    print(color)
                    if color[i] == color[j]:
                        return False
                    elif color[j] == None:
                        color[j] = (color[i]+1) % 2
        return True

    def is_complete(self):
        for i in range(self.n):
            for j in range(i+1, self.n):
                if self.matrix[i][j] == 0:
                    return False
        return True

    def is_subgraph(self, g):
        # Check if the vertices of G are a subset of the vertices of H
        vertices_H = set(range(self.n))
        vertices_G = set(range(g.n))
        if not vertices_G.issubset(vertices_H):
            return False

        # Check if the edges of G are contained in H
        for i in range(g.n):
            for j in range(i+1, g.n):
                if g.matrix[i][j] != 0 and self.matrix[i][j] == 0:
                    return False

        return True
    
def main():
    # create a graph with 4 vertices
    g = Graph(4)

    # add some edges to the graph
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)
    g.add_edge(1, 3)

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

    # create a smaller graph with 3 vertices
    sg = Graph(3)
    sg.add_edge(0, 1)
    sg.add_edge(1, 2)

    # check if the smaller graph is a subgraph of the larger graph
    print("Is the smaller graph a subgraph of the larger graph?")
    print(g.is_subgraph(sg))

main()


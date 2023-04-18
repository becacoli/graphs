from collections import defaultdict
 
class Graph:
 
    def __init__(self, vertices):
        self.V = vertices  
        self.graph = defaultdict(list) 
 
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
 
    
    def g_util(self, v, visited):
        
        visited[v] = True
        
        for i in self.graph[v]:
            if visited[i] == False:
                self.g_util(i, visited)
 
 
    def is_connected(self):
        
        visited = [False]*(self.V)
       
        for i in range(self.V):
            if len(self.graph[i]) != 0:
                break

        if i == self.V-1:
            return True

        self.g_util(i, visited)
 
        for i in range(self.V):
            if visited[i] == False and len(self.graph[i]) > 0:
                return False
 
        return True
 
    def is_eurelian(self):
        
        if self.is_connected() == False:
            return 0
        else:
           
            odd = 0
            for i in range(self.V):
                if len(self.graph[i]) % 2 != 0:
                    odd += 1
 
            if odd == 0:
                return 2
            elif odd == 2:
                return 1
            elif odd > 2:
                return 0

 
    def confirm_eurelian(self):
        res = self.is_eurelian()
        if res == 0:
            print("graph is not Eulerian")
        elif res == 1:
            print("graph has a Euler path")
        else:
            print("graph has a Euler cycle")
 

def main():
        g1 = Graph(5)
        g1.add_edge(1, 0)
        g1.add_edge(0, 2)
        g1.add_edge(2, 1)
        g1.add_edge(0, 3)
        g1.add_edge(3, 4)
        g1.confirm_eurelian()

        f = Graph(4)
        f.add_edge(0,1) #aresta 1
        f.add_edge(0,1) #aresta 2
        f.add_edge(1,2) #aresta 3
        f.add_edge(2,3) #aresta 4
        f.add_edge(0,3) #aresta 5
        f.add_edge(3,3) #aresta 6
        f.add_edge(1,3) #aresta 7
        f.confirm_eurelian()


main()
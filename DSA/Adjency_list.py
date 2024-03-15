class Graph:
    def __init__(self,vno):
        self.vertics_count=vno
        self.adj_list = {v:[] for v in range(vno)}
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertics_count and 0<=v<self.vertics_count:
            self.adj_list[u].append((v,weight))
            self.adj_list[v].append((u,weight))
        else:
            print("Invalid Vertics")
    def remove_edge(self,u,v):
        if 0<=u<self.vertics_count and 0<=v<self.vertics_count:
            self.adj_list[u].remove((v,1))
            self.adj_list[v].remove((u,1))
            self.adjlist[u] = [(vertex,weight) for vertex,weight in self.adj_list[u] if vertex!=v]
            self.adjlist[v] = [(vertex,weight) for vertex,weight in self.adj_list[v] if vertex!=u]
        else:
            print("Invalid Vertics")
    def hash_edge(self,u,v):
        if 0<=u<self.vertics_count and 0<=v<self.vertics_count:
            return any(vertex == v for vertex,x in self.adj_list[u])
        else:
            print("Invalid Vertics")
            return False
    def print_adj_list(self):
        for v,n in self.adj_list.items():
            print("V",v,":",n)
g = Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.print_adj_list()            
            
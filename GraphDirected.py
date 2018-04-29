import sys
from platform import dist

class GraphDirected:
    
    def __init__(self):
        self._my_graph={}
        self._vertices=[]
        
    def add_vertex(self, node):
        self._my_graph[node]= {}
        self._vertices.append(node)
        
    def add_edge(self,node, neighbour, weight):
        self._my_graph[node][neighbour]=weight
    
    def get_neighbours(self, node):
        """
        Method to get neighbours of a node
        """
        return self._my_graph[node].keys()
    
    def get_weight(self,node,neighbour):
        return self._my_graph[node][neighbour]
            
    def print_str(self):
        for key in self._my_graph.keys():
            print(key, self._my_graph[key])
    
    
        

if __name__=="__main__":
    graph = GraphDirected()
    graph.add_vertex("DUB")
    graph.add_vertex("SYD")
    graph.add_vertex("MUP")
    graph.add_vertex("ORK")
    graph.add_edge("DUB","SYD",17000)
    graph.add_edge("DUB","ORK",300)
    graph.add_edge("DUB","MUP",50)
    graph.add_edge("SYD","DUB",20000)
    graph.add_edge("SYD","ORK",19500)
    graph.add_edge("SYD","MUP",19600)
    graph.add_edge("ORK","DUB",300)
    graph.add_edge("ORK","SYD",16800)
    graph.add_edge("ORK","MUP",100)
    graph.add_edge("MUP","ORK",100)
    graph.add_edge("MUP","DUB",400)
    graph.add_edge("MUP","SYD",16900)
    print(graph.shortest_path('DUB'))
    
    
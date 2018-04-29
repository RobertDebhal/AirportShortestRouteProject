class Graph:
    
    def __init__(self):
        self.__my_adjacency_list=[]
        self.__vertex_content=[]
        
    def add_vertex(self, x):
        self.__my_adjacency_list.append([])
        self.__vertex_content.append(x)
    
    def add_edge(self,x, y):
        if y not in self.__my_adjacency_list[x]:
            self.__my_adjacency_list[x].append(y)
            self.__my_adjacency_list[y].append(x)
            
    def neighbours(self, x):
        return self.__my_adjacency_list[x]
    
    def print_str(self):
        for i in range(0, len(self.__my_adjacency_list)):
            print("node "+str(i)+" ( "+str(self.__vertex_content[i])+ " ) = " + str(self.__my_adjacency_list[i]))
   

if __name__=="__main__":
    graph=Graph()
    graph.add_vertex("DUB")
    graph.add_vertex("SYD")
    graph.add_edge(0,1)
    graph.add_edge(1,0)
    graph.print_str()
    print(graph.neighbours(1))
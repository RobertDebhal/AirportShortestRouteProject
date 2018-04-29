import sys
from GraphDirected import GraphDirected
from Itinerary import Itinerary

class GraphRouteConstructor(GraphDirected):
    '''
    classdocs
    '''


    def __init__(self, itinerary,atlas):
        GraphDirected.__init__(self)
        for route in itinerary:
            self.BFS_construct(route,atlas)
        
    def BFS_construct(self,route,atlas):
        for i in range(0,len(route),3):
            airport=route[i:i+3]
            if airport not in self._vertices:
                self.add_vertex(airport)
        
        for vertex in self._vertices:
            ##consider implementing vertices as a set
            for neighbour in self._vertices:
                if neighbour == vertex:
                    pass
                else:
                    self.add_edge(vertex, neighbour,atlas.getDistanceBetweenAiports(vertex,neighbour))
            
        
        
    def shortest_path(self, start):
        '''
            output the shortest path from start hitting all nodes
        '''
        
        current=start
        path = [start]
        to_visit=self._vertices
        to_visit.remove(start)
        
        while len(to_visit)>0:
            min_distance=sys.maxint
            for neighbour in self.get_neighbours(current):
                dist=self.get_weight(current, neighbour)
                if dist < min_distance and neighbour in to_visit:
                    min_distance=dist
                    next_node=neighbour
            current=next_node
            path.append(next_node)
            to_visit.remove(next_node)
        
        path.append(start)
        return path    
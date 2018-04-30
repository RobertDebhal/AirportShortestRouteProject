import sys
from GraphDirected import GraphDirected
from Itinerary import Itinerary
from AircraftTable import AircraftTable

class GraphRouteConstructor(GraphDirected):
    '''
    Extends the GraphDirected class
    
    This class takes an itinerary (a set of airports in a given route), an AirportAtlas object and a Currency object to construct
    a weighted graph of all possible routes between airports. 
    '''

    def __init__(self,itinerary,atlas,currency):
        """
        Instantiates a graph object using BFS_construct for a single route in a given itinerary
        """
        GraphDirected.__init__(self)
        self.airports=itinerary[:len(itinerary)-1]
        self.start=itinerary[0]
        self.aircraft_code=itinerary.pop()
        self.BFS_construct(itinerary,atlas,currency)
        
    def BFS_construct(self,itinerary,atlas,currency):
        """
        Constructs a directed graph using breadth first search
        
        Requires an AirportAtlas object and Currency object as input to calculate the weights
        """
        for airport in itinerary:
            if airport not in self._vertices:
                self.add_vertex(airport)
        
        for vertex in self._vertices:
            ##consider implementing vertices as a set
            for neighbour in self._vertices:
                if neighbour == vertex:
                    pass
                else:
                    self.add_edge(vertex, neighbour,atlas.getCostOfJourney(vertex,neighbour,currency))
            
        
        
    def shortest_path(self, aircraft, atlas):
        '''
            Output the shortest (cheapest) path from start hitting all nodes
        
            Uses a sufficient greedy algorithm which will move to the closest adjacent node in the graph at each stage of the journey.
            Also takes into account the fuel capacity of a specified aircraft. If at any point on the journey the shortest
            distance is greater than the fuel capacity the journey will be considered infeasible for this aircraft.
        '''
        
        current=self.start
        path = [self.start]
        to_visit=self._vertices
        to_visit.remove(self.start)
        cost=0
        
        while len(to_visit)>0:
            min_distance=sys.maxint
            for neighbour in self.get_neighbours(current):
                dist=self.get_weight(current, neighbour)
                if dist < min_distance and neighbour in to_visit:
                    min_distance=dist
                    next_node=neighbour
            if atlas.getDistanceBetweenAirports(current,next_node)>aircraft._maxFuel:
                return "This journey is infeasible for your aircraft"
            cost+=min_distance
            current=next_node
            path.append(next_node)
            to_visit.remove(next_node)
        
        path.append(self.start)
        cost+=self.get_weight(current,self.start)
        cost=round(cost,2)
        return path, cost    
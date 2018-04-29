import GraphRouteConstructor as gc
import Itinerary as it
import AirportAtlas as atl

if __name__ == "__main__":
    itinerary = it.Itinerary('input/testroutes_new.csv').get_itinerary()
    print(itinerary[0])
    print(itinerary[1])
    print(itinerary[2])
    print('------------------------------------------')
    atlas = atl.AirportAtlas('input/airport.csv')
    graph = gc.GraphRouteConstructor(itinerary[0],atlas)
    graph1 = gc.GraphRouteConstructor(itinerary[1],atlas)
    graph2 = gc.GraphRouteConstructor(itinerary[2],atlas)
    print(graph.shortest_path(itinerary[0][0]))
    print(graph1.shortest_path(itinerary[1][0]))
    print(graph2.shortest_path(itinerary[2][0]))
    graph.print_str()

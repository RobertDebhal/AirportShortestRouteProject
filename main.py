import GraphRouteConstructor as gc
import Itinerary as it
import AirportAtlas as atl
import AircraftTable as at
import Currency as c
import csv

if __name__ == "__main__":
    #prompt user for path to input file
    path=input("Please type a path to an itinerary file: ")
    #initialise itinerary object using given path and get list of itineraries
    itinerary = it.Itinerary(path).get_itinerary()
    #initialise airport atlas object using project files
    atlas = atl.AirportAtlas('input/airport.csv')
    #Initialise aircraft table using project files
    aircraft_table = at.AircraftTable('input/aircraft.csv')
    #Initialise currency table using project files
    currency= c.Currency('input/countrycurrency.csv','input/currencyrates.csv')
    graphs = [] # make empty stack (reinforced using only append() ('push') and pop())
    for i in itinerary:
        graph=gc.GraphRouteConstructor(i,atlas,currency)
        graphs.append(graph)
    with open('bestRoutes.csv','w') as best:
        csvOpen = csv.writer(best,delimiter=',')
        csvOpen.writerow(["Aircraft","Airports","Cheapest Path","Feasibility","Fuel Cost"])
        while len(graphs)>0:
            x=graphs.pop()
            route = x.shortest_path(aircraft_table.getAircraft(x.aircraft_code), atlas)
            if route == "This journey is infeasible for your aircraft":
                csvOpen.writerow([x.aircraft_code,x.airports,"","Infeasible","NA"])
            else:
                csvOpen.writerow([x.aircraft_code,x.airports,route[0],"Feasible",route[1]])
    
    
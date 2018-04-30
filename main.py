import GraphRouteConstructor as gc
import Itinerary as it
import AirportAtlas as atl
import AircraftTable as at
import Currency as c
import csv
import os.path
import sys

def check_file(path):
    if not os.path.isfile(path):
        return False
    return True
         
def check_format(path):
    """
    Test to check that itinerary file is in the correct format
        
    Checks to see that each row consists of cells containing only three letter airport codes 
    and that the first and last code are the same for each row (assumes round trip)
    """
    itinerary=it.Itinerary(path)
    valid=True
    for route in itinerary.get_itinerary():
        for airport in route:
            if len(airport)!=3 and airport != route[-1]:
                valid=False  
    return valid

if __name__ == "__main__":
    #prompt user for path to input file
    path=input("Please type a path to an itinerary file: ")
    if not check_file(path):
        print("Please type the full path to a valid file")
        print("Terminating program")
        sys.exit()
    if not check_format(path):
        print("Please type the full path to a file in the specified format")
        print("Terminating program")
        sys.exit()
    
    #initialise itinerary object using given path and get list of itineraries
    itinerary = it.Itinerary(path).get_itinerary()
    
    #initialise airport atlas object using project files
    atlas = atl.AirportAtlas('input/airport.csv')
    
    #Initialise aircraft table using project files
    aircraft_table = at.AircraftTable('input/aircraft.csv')
    
    #Initialise currency table using project files
    currency= c.Currency('input/countrycurrency.csv','input/currencyrates.csv')
    
    graphs = [] # make empty stack (reinforced using only .append() ('push') and .pop())
                # stack makes sense as we do not need to retain the order of the itinerary (route is stored in each graph)
                # and insertion/deletion are O(1)
    for i in itinerary:
        graph=gc.GraphRouteConstructor(i,atlas,currency)
        graphs.append(graph)
    with open('bestroutes.csv','w') as best:
        csvOpen = csv.writer(best,delimiter=',')
        csvOpen.writerow(["Aircraft","Airports","Cheapest Path","Feasibility","Fuel Cost"])
        while len(graphs)>0:
            x=graphs.pop()
            route = x.shortest_path(aircraft_table.getAircraft(x.aircraft_code), atlas)
            if route == "This journey is infeasible for your aircraft":
                csvOpen.writerow([x.aircraft_code,x.airports,"","Infeasible","NA"])
            else:
                csvOpen.writerow([x.aircraft_code,x.airports,route[0],"Feasible",route[1]])
    
    
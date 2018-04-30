import Airport
import csv
from math import pi,sin,cos,acos

class AirportAtlas:
    """
    Class for storing a dictionary of airport objects.
    """
    def __init__(self, csvFile):
        """
        Instantiate an AirportAtlas object given a csv file
        """
        self.Atlas={}
        with open(csvFile) as csvFile:
            csvOpen = csv.reader(csvFile,delimiter=',')
            for row in csvOpen:
                for i in range(len(row)):
                    row[i]=row[i].strip()
                airport=Airport.Airport(row[4],row[6],row[7],row[3])
                self.Atlas[row[4]]=airport
        
    def addAirport(self,airport):
        """Add an Airport object to the atlas"""
        self.Atlas[airport.code]=[airport]
    
    def getAirport(self,key):
        """retrieve an airport from the atlas"""
        return self.Atlas[key]

    @staticmethod            
    def greatcircledistance(lat1,lng1,lat2,lng2):
        """
        Computes the great circle distance between coordinates given two pairs of lat and long
        """
        radius_earth=6371 #km
        theta1 = lng1 * (2 * pi) / 360
        theta2 = lng2 * (2 * pi) / 360
        phi1 = (90 - lat1) * (2 * pi) / 360
        phi2 = (90 - lat2) * (2 * pi) / 360
        distance = int(acos(sin(phi1) * sin(phi2) * cos(theta1 - theta2) + cos(phi1) * cos(phi2)) * radius_earth)
        return distance
    
    def getDistanceBetweenAirports(self,Airport1,Airport2):
        """
        Calculates distance between two airports
        """
        airport1 = self.Atlas.get(Airport1)
        airport2 = self.Atlas.get(Airport2)
        lat1=airport1.getLat()
        lng1=airport1.getLong()
        lat2=airport2.getLat()
        lng2=airport2.getLong()
        return AirportAtlas.greatcircledistance(lat1,lng1,lat2,lng2)
        
    def getCostOfJourney(self,Airport1,Airport2,currency):
        """
        Calculates cost of journey from one airport to another
        """
        distance = self.getDistanceBetweenAirports(Airport1, Airport2)
        airport1 = self.Atlas.get(Airport1)
        rate = currency.getRate(airport1.getCountry())
        cost = rate*distance
        return cost
    
    def getAirports(self):
        """
        Return list containing codes of all airports stored in atlas object
        """
        return self.Atlas.keys()
    
if __name__=="__main__":
    from Currency import *
    curr = Currency('input/countrycurrency.csv','input/currencyrates.csv')
    atlas=AirportAtlas('input/airport.csv')
    print(atlas.getCostOfJourney('LHR', 'DUB',curr))
    
        
        

import csv

class Aircraft:
    """
    Class describing aircraft and their important features. 
    
    For the purpose of this project fuel capacity in litres is the most important feature.
    """
    __MIN_FUEL = 100

    def __init__(self,csvFile,flightNumber=''):
        AircraftTable={}
        with open(csvFile) as csvFile:
            csvOpen = csv.reader(csvFile,delimiter=',')
            
        
        self.flightNumber=flightNumber #you must have a flight number assigned to fly
        self.__fuel=0 #private attribute containing current fuel in aircraft
        self.__fuelCheck=False #this is a boolean flag for a pre-flight check
        self._maxFuel=self.__MIN_FUEL
        self.__flightClearance=False

    def fuelCheck(self):
        if self.__fuel<self.__MIN_FUEL:
            self.__fuelCheck = False
        else:
            self.__fuelCheck = True
        return self.__fuelCheck

    def fuelLevel(self):
        return self.__fuel
        
    def reFuel(self,rate):
        """
        Refuels aircraft to max capacity.
        
        Cost of fuel is returned as a float. It is assumed that a rate is given to calculate the cost of fuel. 
        If aircraft is already full a value of 0 is returned
        """
        
        fuel_cost=0
        if self.__fuel < self._maxFuel:
            self.__fuel = self._maxFuel
            fuel_cost = (self._maxFuel - self.__fuel)*rate
            
        return fuel_cost
        

import csv
from __builtin__ import False

class Aircraft:
    """
    Class describing aircraft and their important features. 
    
    For the purpose of this project fuel capacity in litres is the most important feature.
    """

    def __init__(self,code,maxFuel):
        self.__code=code 
        self._maxFuel=float(maxFuel)
        self.__fuel=float(maxFuel) #private attribute containing current fuel in aircraft. Aircraft is assumed to start journey with full tank.
        self.__fuelCheck=False # Boolean to determine if aircraft has sufficient fuel for journey. Initialised to False.
        
    def fuelCheck(self,distance):
        """
        Function to determine if aircraft has sufficient fuel to make a journey of a given distance.
        
        It is assumed that distance is in km and the fuel is in litres with 1 litre being used per km.
        """
        if self.__fuel<distance:
            self.__fuelCheck = False
        else:
            self.__fuelCheck = True
        return self.__fuelCheck

    def getFuelLevel(self):
        """
        Returns current fuel
        """
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
    
    def print_str(self):
        """
        To string method
        """
        print(self.__code,self.__fuel,self._maxFuel)

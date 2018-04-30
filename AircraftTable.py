import Aircraft
import csv

class AircraftTable:
    
    def __init__(self, csvFile):
        """
        Reads a csv file to create a dictionary of aircraft objects.
        
        It is assumed that the code of an aircraft is contained in the first row of the csv and that the 
        aircraft fuel capacity in litres is in the fifth row of the csv.
        """
        self.Table={}
        with open(csvFile) as csvFile:
            csvOpen = csv.reader(csvFile,delimiter=',')
            count=0
            for row in csvOpen:
                if count != 0:
                    aircraft=Aircraft.Aircraft(row[0],row[4])
                    self.Table[row[0]]=aircraft
                count+=1
                
    def getAircraftFuelCapacity(self,code):
        return self.Table[code]._maxFuel
    
    def getAircraft(self,code):
        return self.Table[code]

if __name__=="__main__":
    table=AircraftTable("input/aircraft.csv")
    print(table.getAircraftFuelCapacity('747'))

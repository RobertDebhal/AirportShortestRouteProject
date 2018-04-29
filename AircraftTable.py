import Aircraft
import csv

class AircraftTable:
    
    def __init__(self, csvFile):
        self.Table={}
        with open(csvFile) as csvFile:
            csvOpen = csv.reader(csvFile,delimiter=',')
            for row in csvOpen:
                aircraft=Aircraft.Aircraft(row[4],row[6],row[7],row[3])
                self.Table[row[4]]=aircraft

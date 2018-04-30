import csv

class Itinerary:
    
    def __init__(self, csvFile):
        self.Itinerary=[]
        with open(csvFile) as csvFile:
            csvOpen = csv.reader(csvFile,delimiter=',')
            count=0
            for row in csvOpen:
                self.Itinerary.append([])
                for cell in row:
                    self.Itinerary[count].append(cell)
                count+=1
        
    def get_itinerary(self):    
        return self.Itinerary

if __name__=="__main__":
    Itinerary=Itinerary('input/testroutes.csv')
    
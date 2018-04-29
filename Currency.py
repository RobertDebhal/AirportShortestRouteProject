import csv

class Currency:
    """
    
    """
    def __init__(self,country):
        self.currency_info={'currency':"",'to_EUR_rate':0}
        #should maybe have 'master' class to handle opening files?
        with open('input/countrycurrency.csv') as rates:
            csvOpen = csv.reader(rates,delimiter=',')
            for row in csvOpen:
                if row[0]==country:
                    self.currency_info['currency']=row[14]
                    
        with open('input/currencyrates.csv') as rates:
            csvOpen = csv.reader(rates,delimiter=',')
            for row in csvOpen:
                if self.currency_info['currency']==row[1]:
                    self.currency_info['to_EUR_rate']=row[2]
    
    def getCurrency(self):
        return self.currency_info['currency']
    
    def getToEURRate(self):
        return self.currency_info['to_EUR_rate']
                
if __name__=="__main__":
    curr = Currency('Fiji')
    print(curr.getCurrency())
    print(curr.getToEURRate())
    
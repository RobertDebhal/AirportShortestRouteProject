import csv

class Currency:
    """
    
    """
    def __init__(self,countryCurrency,currencyRates):
        self.countryCurrency={}
        self.currencyRates={}

        with open(countryCurrency) as csvFile:
            csvOpen = csv.reader(csvFile,delimiter=',')
            for row in csvOpen:
                self.countryCurrency[row[0]]=row[14]
                    
        with open(currencyRates) as rates:
            csvOpen = csv.reader(rates,delimiter=',')
            for row in csvOpen:
                self.currencyRates[row[1]]=row[2]
    
    def getCurrencyByCountry(self,country):
        return self.countryCurrency[country]

    def getRateByCurrency(self,currency):
        return float(self.currencyRates[currency])
    
    def getRate(self, country):
        return self.getRateByCurrency(self.getCurrencyByCountry(country))
                
if __name__=="__main__":
    curr = Currency('input/countrycurrency.csv','input/currencyrates.csv')
    print(curr.getCurrencyByCountry('Ireland'))
    print(curr.getRateByCurrency('GBP'))
    
class Airport:
    def __init__(self,code,lat,lng,country):
        self.code=code 
        self.lat=float(lat)
        self.lng=float(lng)
        self.country=country
    
    def getLat(self):
        return float(self.lat)
    
    def getLong(self):
        return float(self.lng)
    
    def getCode(self):
        return self.code
    
    def getCountry(self):
        return self.country
    
    def __str__(self):
        return str(self.__dict__)
    
if __name__=="__main__":        
    a=Airport('DUB',53,-6.13,'Ireland')
    print(a)  
    
import unittest
from AirportAtlas import *
from GraphRouteConstructor import *
from Currency import *
from Itinerary import *
from AircraftTable import *
from main import check_file, check_format

class UnitTests(unittest.TestCase):
    def test_whitespace_airport_atlas(self):
        """
        Test to ensure AirportAtlas can handle input file with leading and/or trailing whitespace
        """
        atlas=AirportAtlas('testFiles/test_airports_whitespace.csv')
        self.assertTrue('DUB' in atlas.getAirports())
        self.assertTrue(53.421333 == atlas.getAirport('DUB').getLat())
        self.assertTrue(-6.270075 == atlas.getAirport('DUB').getLong())
        self.assertTrue('Ireland' in atlas.getAirport('DUB').getCountry())
    
    def test_check_file(self):
        """
        Check if input is a valid directory/file
        """
        self.assertFalse(check_file('madeup'))
        self.assertTrue(check_file('testFiles/test_path_feasible_747.csv'))

    def test_check_format(self):
        """
        Test to check that the given itinerary file is in the correct format
        """
        self.assertTrue(check_format('testFiles/test_path_feasible_747.csv'))
        self.assertFalse(check_format('testFiles/test_airports.csv'))
        
    def test_shortest_path_infeasible(self):
        """
        Test that shortest path returns infeasible result for known infeasible journey
        
        747 can not fly directly from Ireland to Australia so route in test_path.csv is infeasible 
        """
        itinerary = Itinerary('testFiles/test_path_infeasible_747.csv')
        atlas = AirportAtlas('input/airport.csv')
        aircraft_table = AircraftTable('input/aircraft.csv')
        currency= Currency('input/countrycurrency.csv','input/currencyrates.csv')
        graph=GraphRouteConstructor(itinerary.get_itinerary()[0],atlas,currency)
        self.assertTrue(graph.shortest_path(aircraft_table.getAircraft('747'), atlas)=="This journey is infeasible for your aircraft")    
    
    def test_shortest_path_feasible(self):
        """
        Test that shortest path returns infeasible result for known feasible journey
        
        747 has range of 9,800 so route within Ireland like in test_path_feasible_747.csv is feasible 
        """
        itinerary = Itinerary('testFiles/test_path_feasible_747.csv')
        atlas = AirportAtlas('input/airport.csv')
        aircraft_table = AircraftTable('input/aircraft.csv')
        currency= Currency('input/countrycurrency.csv','input/currencyrates.csv')
        graph=GraphRouteConstructor(itinerary.get_itinerary()[0],atlas,currency)
        self.assertTrue(graph.shortest_path(aircraft_table.getAircraft('747'), atlas)!="This journey is infeasible for your aircraft")
        
    def test_cost_shortest_path(self):
        """
        Test to check for value returned for simple shortest path cost 
        """
        itinerary = Itinerary('testFiles/test_path_cost_simple.csv')
        atlas = AirportAtlas('input/airport.csv')
        aircraft_table = AircraftTable('input/aircraft.csv')
        currency= Currency('input/countrycurrency.csv','input/currencyrates.csv')
        graph=GraphRouteConstructor(itinerary.get_itinerary()[0],atlas,currency)
        cost=graph.shortest_path(aircraft_table.getAircraft('747'), atlas)[1]
        #SNN to DUB, DUB to OSL, OSL to SNN
        #194+1291+0.1155*1476=1655.48
        self.assertTrue(cost==1655.48) 

    
    def test_whitespace_itinerary(self):
        """
        Test to ensure Itinerary can handle input file with leading and/or trailing whitespace
        
        Similar to AirportAtlas
        """
        pass
    
    def test_whitespace_currency(self):
        """
        Test to ensure Currency can handle input file with leading and/or trailing whitespace
        
        Similar to AirportAtlas
        """
        pass
    
    def test_whitespace_aircrafttable(self):
        """
        Test to ensure AircraftTable can handle input file with leading and/or trailing whitespace
        
        Similar to AirportAtlas
        """
        pass
    
        
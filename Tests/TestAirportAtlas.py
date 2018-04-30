import unittest
from AirportAtlas import *

class TestAirportAtlas(unittest.TestCase):
    
    def test_whitespace(self):
        """
        Test to confirm AirportAtlas class can handle leading and trailing whitespace
        """
        atlas=AirportAtlas('test_airports_whitespace.csv')
        self.assertTrue('DUB' in [])
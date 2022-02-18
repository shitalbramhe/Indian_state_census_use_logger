from InvalidTypeException import InvalidTypeException
from state_census import StateCensusAnalyser

import unittest
import state_census
class Test(unittest.TestCase):
    def test_number_records_matches(self):
        result = state_census.StateCensusAnalyser.count_number_records()
        expected = 30
        self.assertEqual(expected, result)

    def test_file(self):
        result = state_census.StateCensusAnalyser.check_file()
        expected = "StateCensusData.csv"
        self.assertEqual(expected, result)
    
    def test_file_extension(self):
        result = state_census.StateCensusAnalyser.check_file_extension()
        expected = ".csv"
        self.assertEqual(expected, result)

    def test_check_delimiter(self):
        result = state_census.StateCensusAnalyser.check_delimiter()
        expected = ','
        self.assertEqual(expected, result)
        
    def test_check_header(self):
        result = state_census.StateCensusAnalyser.check_header()
        expected = True
        self.assertEqual(expected, result)

    

if __name__ =='__main__':
    unittest.main()
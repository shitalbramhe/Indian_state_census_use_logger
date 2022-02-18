from InvalidTypeException import InvalidTypeException
from state_code import StateCodeAnalyser

import unittest
import state_code
class Test(unittest.TestCase):
    def test_number_records_matches(self):
        result = state_code.StateCodeAnalyser.count_number_records()
        expected = 38
        self.assertEqual(expected, result)

    def test_file(self):
        result = state_code.StateCodeAnalyser.check_file()
        expected = "StateCode.csv"
        self.assertEqual(expected, result)
    
    def test_file_extension(self):
        result = state_code.StateCodeAnalyser.check_file_extension()
        expected = ".csv"
        self.assertEqual(expected, result)

    def test_check_delimiter(self):
        result = state_code.StateCodeAnalyser.check_delimiter()
        expected = ','
        self.assertEqual(expected, result)
        
    def test_check_header(self):
        result = state_code.StateCodeAnalyser.check_header()
        expected = True
        self.assertEqual(expected, result)

    

if __name__ =='__main__':
    unittest.main()
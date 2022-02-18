from InvalidTypeException import InvalidTypeException
from merge_two_csv_file import StateCensusAnalyser

import unittest
import merge_two_csv_file
class Test(unittest.TestCase):
    def test_number_records_matches(self):
        result = merge_two_csv_file.StateCensusAnalyser.count_number_records()
        expected = 30
        self.assertEqual(expected, result)

    def test_file(self):
        result = merge_two_csv_file.StateCensusAnalyser.check_file()
        expected = "resultfile.csv"
        self.assertEqual(expected, result)
    
    def test_file_extension(self):
        result = merge_two_csv_file.StateCensusAnalyser.check_file_extension()
        expected = ".csv"
        self.assertEqual(expected, result)

    def test_check_delimiter(self):
        result = merge_two_csv_file.StateCensusAnalyser.check_delimiter()
        expected = ','
        self.assertEqual(expected, result)
        
    def test_check_header(self):
        result = merge_two_csv_file.StateCensusAnalyser.check_header()
        expected = True
        self.assertEqual(expected, result)

    

if __name__ =='__main__':
    unittest.main()
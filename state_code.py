"""
@Author: Shital Bajait
@Date: 18-02-2022 07:30:00
@Last Modified by: Shital Bajait 
@Last Modified time: 18-02-2022 09:30:00
@Title : Load State CSV File and test cases
"""
from InvalidTypeException import InvalidTypeException
from InvalidTypeException import ExceptionType

import logging

logger = logging.getLogger(__name__)

formatter = logging.Formatter('%(asctime)s: %(message)s')

file_handler = logging.StreamHandler()
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
import csv

class StateCodeAnalyser():
    def state_code():
        """
            Description:
                Function to load StateCensusData file
            Parameter:
                None
            Return:
                None
        """
        with open("StateCode.csv","r") as data:
            statecode = csv.reader(data, delimiter=',')
            for i in statecode:
                logger.error(i)

    def count_number_records():
        """
            Description:
                Function to count number of records
            Parameter:
                None
            Return:
                rows of records
        """
        with open("StateCode.csv") as data:
            statecode = csv.reader(data, delimiter=',')
            return len(list(statecode))

    def check_file():
        """
            Description:
                Function to check file is exist or not
            Parameter:
                None
            Return:
                None
        """
        f = open("StateCode.csv")
        f.close()
        if f :
            return "StateCode.csv"
        else:
            raise InvalidTypeException(ExceptionType.INCORRECT_FILE_TYPE_EXCEPTION.value)

    
    def check_file_extension():
        """
            Description:
                Function to check csv file exists or not
            Parameter:
                None
            Return:
                .csv
        """
        file = "StateCode.csv"
        if file.endswith(".csv"):
            return ".csv"
        else:
            raise InvalidTypeException(ExceptionType.INCORRECT_EXTENSION__EXCEPTION.value)

    def check_delimiter():
        """
            Description:
                Function to check delimiter is correct or not
            Parameter:
                None
            Return:
                delimiter
        """
        with open("StateCode.csv", newline="") as data:
            dialect = csv.Sniffer().sniff(data.read())
            if  not dialect.delimiter == ',':
                raise InvalidTypeException(ExceptionType.INCORRECT_DELIMITER_EXCEPTION .value)
            else:
                return dialect.delimiter
        
    def check_header():
        """
            Description:
                Function to check header is present or not
            Parameter:
                None
            Return:
                .csv
        """
        with open("StateCode.csv") as data:
            headers = csv.Sniffer().has_header(data.read())
            if headers:
                return headers   
            else:
                raise InvalidTypeException(ExceptionType.INCORRECT_HEADER_EXCEPTION.value)

if __name__ == '__main__':
    StateCodeAnalyser.state_code()
    logger.error(StateCodeAnalyser.count_number_records())
                
      
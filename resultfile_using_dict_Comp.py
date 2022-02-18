"""
@Author: Shital Bajait
@Date: 11-02-2022 15:09:00
@Last Modified by: Shital Bajait 
@Last Modified time: 18-02-2022 18:05:00
@Title : Save the new csv file into a Json File using dictionary comprehension
"""
import csv
import json

class CSV_json_new_file():
    def resultfile_csv_convert(csv_path, json_path):
        with open(csv_path, encoding='utf-8') as csvfile:
            csvData = csv.DictReader(csvfile)
            jsonData = {rows['State']: rows for rows in csvData}
        with open(json_path,'w',encoding='utf-8') as jsonfile:
            jsonfile.write(json.dumps(jsonData, indent=5))

        
if __name__ == '__main__':
    csv_path = r'resultfile.csv'
    json_path =r'resultfile_using_dict_compre.json'
    CSV_json_new_file.resultfile_csv_convert(csv_path, json_path)
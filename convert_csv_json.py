"""
@Author: Shital Bajait
@Date: 18-02-2022 22:04:00
@Last Modified by: Shital Bajait 
@Last Modified time: 18-02-2022 22:04:00
@Title : Save the new csv file into a Json File
"""
import csv
import json

class CSV_json_new_file():
    def resultfile_csv_convert(csv_path, json_path):
        jsonData = {}
        with open(csv_path, encoding='utf-8') as csvfile:
            csvData = csv.DictReader(csvfile)
            for rows in csvData:
                key = rows['State']
                jsonData[key] = rows

        with open(json_path,'w',encoding='utf-8') as jsonfile:
            jsonfile.write(json.dumps(jsonData, indent=5))

        
if __name__ == '__main__':
    csv_path = r'resultfile.csv'
    json_path =r'resultfile.json'
    CSV_json_new_file.resultfile_csv_convert(csv_path, json_path)

from inventory_report.reports.simple_report import SimpleReport
import csv
import json


class Inventory:
    @classmethod
    def import_data(cls, filePath, reportType):
        fileData = cls.get_data(filePath)
        if reportType == "simples":
            return SimpleReport.generate(fileData)

    @classmethod
    def get_data(cls, filePath):
        with open(filePath) as file:
            if ".csv" in filePath:
                content = csv.DictReader(file)
                return list(content)
            elif ".json" in filePath:
                content = json.load(file)
                return content

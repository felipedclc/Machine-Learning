
from inventory_report.reports.simple_report import SimpleReport
import csv
import json


class Inventory:
    @classmethod
    def import_data(cls, file_path, report_type):
        file_data = cls.get_data(file_path)
        if report_type == "simples":
            return SimpleReport.generate(file_data)

    @classmethod
    def get_data(cls, file_path):
        with open(file_path) as file:
            if ".csv" in file_path:
                content = csv.DictReader(file)
                return list(content)
            elif ".json" in file_path:
                content = json.load(file)
                return content
            # elif ".xml" in file_path:


from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter
# import csv
# import json
# import xmltodict


class Inventory:
    @classmethod
    def import_data(cls, file_path, report_type):
        file_data = cls.get_data(file_path)
        if report_type == "simples":
            return SimpleReport.generate(file_data)
        elif report_type == "completo":
            return CompleteReport.generate(file_data)

    @classmethod
    def get_data(cls, file_path):
        if ".csv" in file_path:
            return CsvImporter.import_data(file_path)
        elif ".json" in file_path:
            return JsonImporter.import_data(file_path)
        elif ".xml" in file_path:
            return XmlImporter.import_data(file_path)


#     @classmethod
#     def get_data(cls, file_path):
#         with open(file_path) as file:
#             if ".csv" in file_path:
#                 content = csv.DictReader(file)
#                 return list(content)
#             elif ".json" in file_path:
#                 content = json.load(file)
#                 return content
#             elif ".xml" in file_path:
#                 doc = xmltodict.parse(file.read())
#                 content = [
#                     dict(element) for element in doc['dataset']['record']
#                 ]
#                 return content
# https://python-guide-pt-br.readthedocs.io/pt_BR/latest/scenarios/xml.html

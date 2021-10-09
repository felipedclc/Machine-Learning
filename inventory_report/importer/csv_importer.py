from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if ".csv" in file_path:
            with open(file_path) as csv_file:
                content = csv.DictReader(csv_file)
                return list(content)
        else:
            raise ValueError("Arquivo inválido")

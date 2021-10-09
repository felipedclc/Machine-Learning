from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if ".json" in file_path:
            with open(file_path) as json_file:
                content = json.load(json_file)
                return content
        else:
            raise ValueError("Invalid file type")

from inventory_report.importer.importer import Importer
import xmltodict
# https://python-guide-pt-br.readthedocs.io/pt_BR/latest/scenarios/xml.html


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if ".xml" in file_path:
            with open(file_path) as xml_file:
                doc = xmltodict.parse(xml_file.read())
                content = [
                    dict(element) for element in doc['dataset']['record']
                ]
                return content
        else:
            raise ValueError("Arquivo inválido")

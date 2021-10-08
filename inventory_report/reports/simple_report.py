import json
from datetime import date, datetime

DATE_FORMAT = "%Y-%m-%d"


class SimpleReport:
    @staticmethod
    def generate(data):
        manufacture_dates = []
        expirations = []
        companys = []

        today = date.today()

        for row in data:
            manufacture_dates.append(row["data_de_fabricacao"])
            if row["data_de_validade"] > datetime.strftime(today, DATE_FORMAT):
                expirations.append(row["data_de_validade"])
            companys.append(row["nome_da_empresa"])

        comp = max(companys)  # pegando a empresa que mais se repete

        return (
            f"Data de fabricação mais antiga: {min(manufacture_dates)}\n"
            f"Data de validade mais próxima: {min(expirations)}\n"
            f"Empresa com maior quantidade de produtos estocados: {(comp)}\n"
        )


if __name__ == "__main__":

    def read_file(json_file):
        with open(json_file) as inventory_file:
            inventory_list = json.load(inventory_file)
            return [value for value in inventory_list]


# data = read_file("../data/inventory.json")
# print(SimpleReport.generate(data))

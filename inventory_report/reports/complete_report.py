from typing import Counter
from .simple_report import SimpleReport
import json


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        simple_report = SimpleReport.generate(data)
        # simple_report = super().generate(data)

        product_list = [row["nome_da_empresa"] for row in data]
        products_counter = Counter(product_list)

        products_report = "Produtos estocados por empresa: \n"
        for product, count in products_counter.items():
            products_report += f"- {product}: {count}\n"

        return f"{simple_report}\n{products_report}"


if __name__ == "__main__":

    def read_file(json_file):
        with open(json_file) as inventory_file:
            inventory_list = json.load(inventory_file)
            return [value for value in inventory_list]


# data = read_file("../data/inventory.json")
# print(CompleteReport.complete_report(data))

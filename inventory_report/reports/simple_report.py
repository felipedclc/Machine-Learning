import json


class SimpleReport:
    @staticmethod
    def generate(data):
        pass


if __name__ == "__main__":

    def read_file(json_file):
        with open(json_file) as inventory_file:
            inventory_list = json.load(inventory_file)
            return [value for value in inventory_list]


print(read_file("../data/inventory.json"))

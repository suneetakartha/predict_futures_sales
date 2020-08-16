import pandas
import os


class DataReader:
    def __init__(self, directory):
        categories_path = os.path.join(directory, "item_categories.csv")
        self.item_categories = pandas.read_csv(categories_path)
        self.items = pandas.read_csv(os.path.join(directory, "items.csv"))
        self.sales_train = pandas.read_csv(os.path.join(directory, "sales_train.csv"))
        self.shops = pandas.read_csv(os.path.join(directory, "shops.csv"))
        self.test = pandas.read_csv(os.path.join(directory, "test.csv"))

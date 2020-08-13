import pandas
import os

class DataReader:
    def __init__(self, directory):
        self.item_categories = pandas.read_csv(os.path.join(directory, 'item_categories.csv'))
        self.items = pandas.read_csv(os.path.join(directory, 'items.csv'))
        self.sales_train = pandas.read_csv(os.path.join(directory, 'sales_train.csv'))
        self.test = pandas.read_csv(os.path.join(directory, 'test.csv'))

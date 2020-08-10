from predictfuturesales.data_reader import DataReader

reader = DataReader("data/")

def test_init():
    assert reader.item_categories.size == 168
    assert reader.items.size == 66510
    assert reader.sales_train.size == 17615094
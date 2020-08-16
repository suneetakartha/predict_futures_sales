from predictfuturesales.data_reader import DataReader

reader = DataReader("data/")

def test_init():
    assert reader.item_categories.item_category_name.dtype == object
    assert reader.item_categories.item_category_id.dtype == 'int64'
    assert reader.items.item_name.dtype == object
    assert reader.items.item_id.dtype == 'int64'
    assert reader.items.item_category_id.dtype == 'int64'
    assert reader.sales_train.date.dtype == 'O'
    assert reader.sales_train.date_block_num.dtype == 'int64'
    assert reader.sales_train.shop_id.dtype == 'int64'
    assert reader.sales_train.item_id.dtype == 'int64'
    assert reader.sales_train.item_price.dtype == 'float64'
    assert reader.sales_train.item_cnt_day.dtype == 'float64'
  

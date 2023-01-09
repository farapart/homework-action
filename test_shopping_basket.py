import pytest
import shopping_basket
import decimal

def test_update_item_wrong1():
    i1 = shopping_basket.Item("Warburtons", "Toastie", "800g white sliced loaf", decimal.Decimal('1.52'))
    b = shopping_basket.Basket()
    b.add_item(i1, 3)
    b.update_item(i1, -1)
    empty_flag = b.is_empty()
    assert empty_flag == False

def test_update_item_wrong2():
    i1 = shopping_basket.Item("Warburtons", "Toastie", "800g white sliced loaf", decimal.Decimal('1.5'))
    b = shopping_basket.Basket()
    b.add_item(i1, 3)
    b.update_item(i1, 3)
    cost = b.get_total_cost()
    assert cost == 9

def test_whole_process():
    i1 = shopping_basket.Item("Warburtons", "Toastie", "800g white sliced loaf", decimal.Decimal('1.5'))
    i2 = shopping_basket.Item("Flora", "Buttery", "Buttery spread", decimal.Decimal('2'))
    i3 = shopping_basket.Item("forRemove", "xx", "xxxx", decimal.Decimal('100'))
    b = shopping_basket.Basket()
    b.view()
    b.add_item(i1, 2)
    b.add_item(i2)
    b.add_item(i3, 3)
    b.remove_item(i3)
    cost = b.get_total_cost()
    assert cost == 5

if __name__ == '__main__':
    pytest.main(["-s", "test_shopping_basket.py"])

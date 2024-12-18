import pytest
from tests.data_init import TestData
from Warehousing.code.api.models.orders import Orders

@pytest.fixture
def test_base():
    test_data = TestData.mock_data_orders()
    return Orders(root_path="C:/Users/Frank/SCPT-Groep4/Warehousing/data", is_debug=True, debug_data=test_data)

def test_add(test_base):
    new_order = {
        "id": 5,
        "reference": "ORD00005",
        "created_at": "2024-05-01T10:00:00Z",
        "updated_at": "2024-05-01T10:00:00Z"
    }
    initial_length = len(test_base.data)
    test_base.add(new_order)
    assert len(test_base.data) == initial_length + 1
    assert test_base.get_one(5)["reference"] == "ORD00005"

def test_get_all(test_base):
    assert test_base.get_all() == test_base.data

def test_get_one(test_base):
    assert test_base.get_one(1) == test_base.data[0]
    assert test_base.get_one(1)["reference"] == "ORD00001"

def test_update(test_base):
    updated_order = {
        "id": 1,
        "reference": "ORD00001-Updated",
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-20T10:30:00Z"
    }
    test_base.update(1, updated_order)
    assert test_base.get_one(1)["reference"] == "ORD00001-Updated"

def test_delete(test_base):
    initial_length = len(test_base.data)
    test_base.delete(1)
    assert len(test_base.data) == initial_length - 1
    assert test_base.get_one(1) is None

def test_orders_for_shipment(test_base):
    shipment_id = 1
    expected_orders = [order["id"] for order in test_base.data if order["shipment_id"] == shipment_id]
    assert test_base.get_orders_for_shipment(shipment_id) == expected_orders

def test_orders_for_client(test_base):
    client_id = 1
    expected_orders = [order for order in test_base.data if order["ship_to"] == client_id or order["bill_to"] == client_id]
    assert test_base.get_orders_for_client(client_id) == expected_orders

def test_update_items_in_order(test_base):
    order_id = 1
    new_items = [
        {"item_id": "P007435", "amount": 10},
        {"item_id": "P009557", "amount": 5}
    ]
    test_base.update_items_in_order(order_id, new_items)
    updated_order = test_base.get_one(order_id)
    assert updated_order["items"] == new_items
import pytest
from tests.data_init import TestData
from tests.base_test.test_base import BaseTestClass

@pytest.fixture
def shipments_base():
    test_data = TestData.mock_data_clients()
    return BaseTestClass(test_data)

def test_shipments_for_order(shipments_base):
    order_id = 1
    expected_shipments = [shipment for shipment in shipments_base.data if shipment["order_id"] == order_id]
    assert shipments_base.get_shipments_for_order(order_id) == expected_shipments

def test_update_items_in_shipment(shipments_base):
    shipment_id = 1
    new_items = [
        {"item_id": "P007435", "amount": 10},
        {"item_id": "P009557", "amount": 5}
    ]
    shipments_base.update_items_in_shipment(shipment_id, new_items)
    updated_shipment = shipments_base.get_one(shipment_id)
    assert updated_shipment["items"] == new_items
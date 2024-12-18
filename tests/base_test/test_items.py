import pytest
from tests.data_init import TestData
from Warehousing.code.api.models.items import Items

@pytest.fixture
def test_base():
    test_data = TestData.mock_data_items()
    return Items(root_path="C:/Users/Frank/SCPT-Groep4/Warehousing/data", is_debug=True, debug_data=test_data)

def test_add(test_base):
    new_item = {
        "uid": "P000007",  
        "name": "New Item",
        "created_at": "2024-05-01T10:00:00Z",
        "updated_at": "2024-05-01T10:00:00Z"
    }
    initial_length = len(test_base.data)
    test_base.add(new_item)
    assert len(test_base.data) == initial_length + 1
    assert test_base.get_one("P000007")["name"] == "New Item"

def test_get_all(test_base):
    assert test_base.get_all() == test_base.data

def test_get_one(test_base):
    assert test_base.get_one("P000002") == test_base.data[0]
    assert test_base.get_one("P000002")["description"] == "Focused transitional alliance"

def test_update(test_base):
    updated_item = {
        "uid": "P000002",
        "description": "Updated Item",
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-20T10:30:00Z"
    }
    test_base.update("P000002", updated_item)
    assert test_base.get_one("P000002")["description"] == "Updated Item"

def test_delete(test_base):
    initial_length = len(test_base.data)
    test_base.delete("P000002")
    assert len(test_base.data) == initial_length - 1
    assert test_base.get_one("P000002") is None

def test_items_for_item_line(test_base):
    item_line_id = 69
    expected_items = [item["uid"] for item in test_base.data if item["item_line"] == item_line_id]
    assert test_base.get_items_for_item_line(item_line_id) == expected_items

def test_items_for_item_group(test_base):
    item_group_id = 85
    expected_items = [item["uid"] for item in test_base.data if item["item_group"] == item_group_id]
    assert test_base.get_items_for_item_group(item_group_id) == expected_items

def test_items_for_item_type(test_base):
    item_type_id = 39
    expected_items = [item["uid"] for item in test_base.data if item["item_type"] == item_type_id]
    assert test_base.get_items_for_item_type(item_type_id) == expected_items

def test_items_for_supplier(test_base):
    supplier_id = 57
    expected_items = [item for item in test_base.data if item["supplier_id"] == supplier_id]
    assert test_base.get_items_for_supplier(supplier_id) == expected_items
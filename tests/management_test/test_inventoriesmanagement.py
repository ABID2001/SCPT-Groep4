import pytest
from Warehousing.code.mainManagement.InventoriesManagement import InventoriesManagement

@pytest.fixture
def inventories_management():
    handler = None  # Replace with a mock or actual handler as needed
    inventories_data = [
        {
            "id": 1,
            "item_id": "P000001",
            "description": "Face-to-face clear-thinking complexity",
            "item_reference": "ref123",
            "locations": [3211, 24700, 14123],
            "total_on_hand": 100,
            "total_expected": 50,
            "total_ordered": 30,
            "total_allocated": 20,
            "total_available": 80,
            "created_at": "2015-02-19 16:08:24",
            "updated_at": "2015-09-26 06:37:56"
        },
        {
            "id": 2,
            "item_id": "P000002",
            "description": "Another inventory item",
            "item_reference": "ref456",
            "locations": [12345, 67890],
            "total_on_hand": 200,
            "total_expected": 100,
            "total_ordered": 60,
            "total_allocated": 40,
            "total_available": 160,
            "created_at": "2016-03-20 12:00:00",
            "updated_at": "2016-10-15 08:00:00"
        }
    ]
    return InventoriesManagement(handler, inventories_data)

def test_get_all_items(inventories_management):
    expected_data = [
        {
            "id": 1,
            "item_id": "P000001",
            "description": "Face-to-face clear-thinking complexity",
            "item_reference": "ref123",
            "locations": [3211, 24700, 14123],
            "total_on_hand": 100,
            "total_expected": 50,
            "total_ordered": 30,
            "total_allocated": 20,
            "total_available": 80,
            "created_at": "2015-02-19 16:08:24",
            "updated_at": "2015-09-26 06:37:56"
        },
        {
            "id": 2,
            "item_id": "P000002",
            "description": "Another inventory item",
            "item_reference": "ref456",
            "locations": [12345, 67890],
            "total_on_hand": 200,
            "total_expected": 100,
            "total_ordered": 60,
            "total_allocated": 40,
            "total_available": 160,
            "created_at": "2016-03-20 12:00:00",
            "updated_at": "2016-10-15 08:00:00"
        }
    ]
    assert inventories_management.get_all_items() == expected_data

def test_get_item(inventories_management):
    item_id = 1
    expected_item = {
        "id": 1,
        "item_id": "P000001",
        "description": "Face-to-face clear-thinking complexity",
        "item_reference": "ref123",
        "locations": [3211, 24700, 14123],
        "total_on_hand": 100,
        "total_expected": 50,
        "total_ordered": 30,
        "total_allocated": 20,
        "total_available": 80,
        "created_at": "2015-02-19 16:08:24",
        "updated_at": "2015-09-26 06:37:56"
    }
    assert inventories_management.get_item(item_id) == expected_item

def test_add_item(inventories_management):
    new_item = {
        "id": 3,
        "item_id": "P000003",
        "description": "New Inventory Item",
        "item_reference": "newRef123",
        "locations": [12345, 67890],
        "total_on_hand": 100,
        "total_expected": 50,
        "total_ordered": 30,
        "total_allocated": 20,
        "total_available": 80,
        "created_at": "2024-06-01T10:00:00Z",
        "updated_at": "2024-06-01T10:00:00Z"
    }
    initial_length = len(inventories_management.get_all_items())
    inventories_management.add_item(new_item)
    assert len(inventories_management.get_all_items()) == initial_length + 1
    assert inventories_management.get_item(3)["description"] == "New Inventory Item"

def test_update_item(inventories_management):
    updated_item = {
        "id": 1,
        "item_id": "P000001",
        "description": "Updated Inventory Item",
        "item_reference": "updatedRef123",
        "locations": [3211, 24700, 14123, 19538, 31071, 24701, 11606, 11817],
        "total_on_hand": 262,
        "total_expected": 0,
        "total_ordered": 80,
        "total_allocated": 41,
        "total_available": 141,
        "created_at": "2015-02-19 16:08:24",
        "updated_at": "2015-09-26 06:37:56"
    }
    inventories_management.update_item(1, updated_item)
    assert inventories_management.get_item(1)["description"] == "Updated Inventory Item"

def test_delete_item(inventories_management):
    initial_length = len(inventories_management.get_all_items())
    inventories_management.delete_item(1)
    assert len(inventories_management.get_all_items()) == initial_length - 1
    assert inventories_management.get_item(1) is None
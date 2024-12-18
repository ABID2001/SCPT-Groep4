import pytest
from tests.data_init import TestData
from Warehousing.code.api.models.locations import Locations

@pytest.fixture
def test_base():
    test_data = TestData.mock_data_locations()
    return Locations(root_path="C:/Users/Frank/SCPT-Groep4/Warehousing/data", is_debug=True, debug_data=test_data)

def test_add(test_base):
    new_item = {
        "id": 7, 
        "name": "New Location",
        "created_at": "2024-05-01T10:00:00Z",
        "updated_at": "2024-05-01T10:00:00Z"
    }
    initial_length = len(test_base.data)
    test_base.add(new_item)
    assert len(test_base.data) == initial_length + 1
    assert test_base.get_one(7)["name"] == "New Location"

def test_get_all(test_base):
    assert test_base.get_all() == test_base.data

def test_get_one(test_base):
    assert test_base.get_one(1) == test_base.data[0]
    assert test_base.get_one(1)["name"] == "Row: A, Rack: 1, Shelf: 0"

def test_update(test_base):
    updated_item = {
        "id": 1,
        "name": "Updated Location",
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-20T10:30:00Z"
    }
    test_base.update(1, updated_item)
    assert test_base.get_one(1)["name"] == "Updated Location"

def test_delete(test_base):
    initial_length = len(test_base.data)
    test_base.delete(1)
    assert len(test_base.data) == initial_length - 1
    assert test_base.get_one(1) is None

def test_locations_in_warehouse(test_base):
    warehouse_id = 1
    expected_locations = [location for location in test_base.data if location["warehouse_id"] == warehouse_id]
    assert test_base.get_locations_in_warehouse(warehouse_id) == expected_locations
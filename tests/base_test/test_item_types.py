import pytest
from tests.data_init import TestData
from tests.base_test.test_base import BaseTestClass

#pytest tests/base_test/test_item_types.py

@pytest.fixture
def test_base():
    test_data = TestData.mock_data_item_types()
    return BaseTestClass(test_data)

def test_add(test_base):
    new_item = {
        "id": 7,  # Ensure this ID is unique and not already present in the test data
        "name": "New Item Type",
        "created_at": "2024-05-01T10:00:00Z",
        "updated_at": "2024-05-01T10:00:00Z"
    }
    initial_length = len(test_base.data)
    test_base.add(new_item)
    assert len(test_base.data) == initial_length + 1
    assert test_base.get_one(7)["name"] == "New Item Type"

def test_get_all(test_base):
    assert test_base.get_all() == test_base.data

def test_get_one(test_base):
    assert test_base.get_one(1) == test_base.data[0]
    assert test_base.get_one(1)["name"] == "Consumables"

def test_update(test_base):
    updated_item = {
        "id": 1,
        "name": "Updated Item Type",
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-20T10:30:00Z"
    }
    test_base.update(1, updated_item)
    assert test_base.get_one(1)["name"] == "Updated Item Type"

def test_delete(test_base):
    initial_length = len(test_base.data)
    test_base.delete(1)
    assert len(test_base.data) == initial_length - 1
    assert test_base.get_one(1) is None


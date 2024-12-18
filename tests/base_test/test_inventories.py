import pytest
from tests.data_init import TestData
from tests.base_test.test_base import BaseTestClass

#inventories test
#pytest tests/base_test/test_inventories.py

@pytest.fixture
def test_base():
    test_data = TestData.mock_data_inventories()
    return BaseTestClass(test_data)

def test_add(test_base):
    new_item = {
        "id": 5,
        "description": "New Inventory",
        "created_at": "2024-05-01T10:00:00Z",
        "updated_at": "2024-05-01T10:00:00Z"
    }
    initial_length = len(test_base.data)
    test_base.add(new_item)
    assert len(test_base.data) == initial_length + 1
    assert test_base.get_one(5)["description"] == "New Inventory"

def test_get_all(test_base):
    assert test_base.get_all() == test_base.data

def test_get_one(test_base):
    assert test_base.get_one(1) == test_base.data[0]
    assert test_base.get_one(1)["description"] == "Face-to-face clear-thinking complexity"

def test_update(test_base):
    updated_item = {
        "id": 1,
        "description": "Updated Inventory",
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-20T10:30:00Z"
    }
    test_base.update(1, updated_item)
    assert test_base.get_one(1)["description"] == "Updated Inventory"

def test_delete(test_base):
    initial_length = len(test_base.data)
    test_base.delete(1)
    assert len(test_base.data) == initial_length - 1
    assert test_base.get_one(1) is None
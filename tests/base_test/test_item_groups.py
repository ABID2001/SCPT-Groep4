import pytest
from tests.data_init import TestData
from tests.base_test.test_base import BaseTestClass

#pytest tests/base_test/test_item_groups.py

@pytest.fixture
def test_base():
    test_data = TestData.mock_data_item_groups()
    return BaseTestClass(test_data)

def test_add(test_base):
    new_item = {
        "id": 7,
        "name": "New Item Group",
        "created_at": "2024-05-01T10:00:00Z",
        "updated_at": "2024-05-01T10:00:00Z"
    }
    initial_length = len(test_base.data)
    test_base.add(new_item)
    assert len(test_base.data) == initial_length + 1
    assert test_base.get_one(7)["name"] == "New Item Group"

def test_get_all(test_base):
    assert test_base.get_all() == test_base.data

def test_get_one(test_base):
    assert test_base.get_one(0) == test_base.data[0]
    assert test_base.get_one(0)["name"] == "Electronics"

def test_update(test_base):
    updated_item = {
        "id": 0,
        "name": "Updated Item Group",
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-20T10:30:00Z"
    }
    test_base.update(0, updated_item)
    assert test_base.get_one(0)["name"] == "Updated Item Group"

def test_delete(test_base):
    initial_length = len(test_base.data)
    test_base.delete(0)
    assert len(test_base.data) == initial_length - 1
    assert test_base.get_one(0) is None
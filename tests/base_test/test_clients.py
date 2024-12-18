import pytest
from tests.data_init import TestData
from tests.base_test.test_base import BaseTestClass

#clients test
#pytest tests/base_test/test_clients.py
#set PYTHONPATH=C:/Users/Frank/SCPT-Groep4

@pytest.fixture
def test_base():
    test_data = TestData.mock_data_clients()
    return BaseTestClass(test_data)

def test_add(test_base):
    new_item = {
        "id": 5,
        "name": "New Client",
        "address": "123 New St",
        "city": "New City",
        "zip_code": "12345",
        "province": "New State",
        "country": "Newland",
        "contact_name": "New Contact",
        "contact_phone": "123-456-7890",
        "contact_email": "newcontact@newclient.com",
        "created_at": "2024-05-01T10:00:00Z",
        "updated_at": "2024-05-01T10:00:00Z"
    }
    initial_length = len(test_base.data)
    test_base.add(new_item)
    assert len(test_base.data) == initial_length + 1
    assert test_base.get_one(5)["name"] == "New Client"

def test_get_all(test_base):
    assert test_base.get_all() == test_base.data

def test_get_one(test_base):
    assert test_base.get_one(1) == test_base.data[0]
    assert test_base.get_one(1)["name"] == "Alpha Industries"

def test_update(test_base):
    updated_item = {
        "id": 1,
        "name": "Updated Client",
        "address": "123 Updated St",
        "city": "Updated City",
        "zip_code": "54321",
        "province": "Updated State",
        "country": "Updatedland",
        "contact_name": "Updated Contact",
        "contact_phone": "987-654-3210",
        "contact_email": "updatedcontact@updatedclient.com",
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-20T10:30:00Z"
    }
    test_base.update(1, updated_item)
    assert test_base.get_one(1)["name"] == "Updated Client"

def test_delete(test_base):
    initial_length = len(test_base.data)
    test_base.delete(1)
    assert len(test_base.data) == initial_length - 1
    assert test_base.get_one(1) is None
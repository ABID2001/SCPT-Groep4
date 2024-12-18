import pytest
from Warehousing.code.mainManagement.ClientsManagement import ClientsManagement

@pytest.fixture
def clients_management():
    handler = None  # verander dit naar een echte handler indien nodig
    clients_data = [
        {"id": 1, "name": "Client A"},
        {"id": 2, "name": "Client B"}
    ]
    return ClientsManagement(handler, clients_data)

def test_get_all_items(clients_management):
    expected_data = [
        {"id": 1, "name": "Client A"},
        {"id": 2, "name": "Client B"}
    ]
    assert clients_management.get_all_items() == expected_data

def test_get_item(clients_management):
    client_id = 1
    expected_client = {"id": 1, "name": "Client A"}
    assert clients_management.get_item(client_id) == expected_client

def test_add_item(clients_management):
    new_client = {"id": 3, "name": "Client C"}
    clients_management.add_item(new_client)
    assert clients_management.get_item(3) == new_client

def test_update_item(clients_management):
    updated_client = {"id": 1, "name": "Client A Updated"}
    clients_management.update_item(1, updated_client)
    assert clients_management.get_item(1) == updated_client

def test_delete_item(clients_management):
    clients_management.delete_item(1)
    assert clients_management.get_item(1) is None
    assert len(clients_management.get_all_items()) == 1
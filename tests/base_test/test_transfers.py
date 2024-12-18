import pytest
from tests.data_init import TestData
from Warehousing.code.api.models.transfers import Transfers

@pytest.fixture
def transfers_base():
    test_data = TestData.mock_data_transfers()
    return Transfers(root_path="C:/Users/Frank/SCPT-Groep4/Warehousing/data", is_debug=True, debug_data=test_data)

def test_add(transfers_base):
    new_transfer = {
        "id": 5,
        "reference": "TR00005",
        "transfer_from": None,
        "transfer_to": 9229,
        "transfer_status": "Pending",
        "created_at": "2024-05-01T10:00:00Z",
        "updated_at": "2024-05-01T10:00:00Z",
        "items": [
            {"item_id": "P007435", "amount": 10}
        ]
    }
    initial_length = len(transfers_base.data)
    transfers_base.add(new_transfer)
    assert len(transfers_base.data) == initial_length + 1
    assert transfers_base.get_one(5)["reference"] == "TR00005"

def test_get_all(transfers_base):
    assert transfers_base.get_all() == transfers_base.data

def test_get_one(transfers_base):
    assert transfers_base.get_one(1) == transfers_base.data[0]
    assert transfers_base.get_one(1)["reference"] == "TR00001"

def test_update(transfers_base):
    updated_transfer = {
        "id": 1,
        "reference": "TR00001-Updated",
        "transfer_from": None,
        "transfer_to": 9229,
        "transfer_status": "Completed",
        "created_at": "2000-03-11T13:11:14Z",
        "updated_at": "2000-03-12T16:11:14Z",
        "items": [
            {"item_id": "P007435", "amount": 23}
        ]
    }
    transfers_base.update(1, updated_transfer)
    assert transfers_base.get_one(1)["reference"] == "TR00001-Updated"

def test_delete(transfers_base):
    initial_length = len(transfers_base.data)
    transfers_base.delete(1)
    assert len(transfers_base.data) == initial_length - 1
    assert transfers_base.get_one(1) is None

def test_transfers_for_location(transfers_base):
    location_id = 9229
    expected_transfers = [transfer for transfer in transfers_base.data if transfer["transfer_from"] == location_id or transfer["transfer_to"] == location_id]
    assert transfers_base.get_transfers_for_location(location_id) == expected_transfers

def test_update_items_in_transfer(transfers_base):
    transfer_id = 1
    new_items = [
        {"item_id": "P007435", "amount": 10},
        {"item_id": "P009557", "amount": 5}
    ]
    transfers_base.update_items_in_transfer(transfer_id, new_items)
    updated_transfer = transfers_base.get_one(transfer_id)
    assert updated_transfer["items"] == new_items
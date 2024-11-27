import json
from models.base import Base

TRANSFERS = [
    {
        "id": 1,
        "reference": "TRANS001",
        "transfer_from": 1,
        "transfer_to": 2,
        "transfer_status": "Processed",
        "created_at": "2024-05-01T14:00:00Z",
        "updated_at": "2024-05-02T15:00:00Z",
        "items": [
            {
                "item_id": 1,
                "amount": 50
            },
            {
                "item_id": 2,
                "amount": 30
            }
        ]
    },
    {
        "id": 2,
        "reference": "TRANS002",
        "transfer_from": 2,
        "transfer_to": 1,
        "transfer_status": "Scheduled",
        "created_at": "2024-05-03T10:30:00Z",
        "updated_at": "2024-05-04T11:30:00Z",
        "items": [
            {
                "item_id": 1,
                "amount": 20
            },
            {
                "item_id": 2,
                "amount": 40
            }
        ]
    }
]

class Transfers(Base):
    def __init__(self, root_path, is_debug=False):
        super().__init__(root_path, "transfers.json", is_debug, TRANSFERS)

    def get_transfers_for_location(self, location_id):
        result = []
        for x in self.data:
            if x["transfer_from"] == location_id or x["transfer_to"] == location_id:
                result.append(x)
        return result

    def update_items_in_transfer(self, transfer_id, items):
        transfer = self.get_one(transfer_id)
        transfer["items"] = items
        self.update(transfer_id, transfer)
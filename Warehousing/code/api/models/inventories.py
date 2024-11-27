import json
from models.base import Base

INVENTORIES = [
    {
        "id": 1,
        "item_id": 1,
        "description": "High Precision Bearings",
        "item_reference": "REF123",
        "location_id": 1,
        "total_on_hand": 150,
        "total_expected": 200,
        "total_ordered": 50,
        "total_allocated": 100,
        "total_available": 50,
        "created_at": "2024-03-20T10:00:00Z",
        "updated_at": "2024-03-21T11:00:00Z"
    },
    {
        "id": 2,
        "item_id": 1,
        "description": "High Precision Bearings",
        "item_reference": "REF123",
        "location_id": 2,
        "total_on_hand": 150,
        "total_expected": 200,
        "total_ordered": 50,
        "total_allocated": 100,
        "total_available": 50,
        "created_at": "2024-03-20T10:00:00Z",
        "updated_at": "2024-03-21T11:00:00Z"
    },
    {
        "id": 3,
        "item_id": 2,
        "description": "Stainless Steel Bolts",
        "item_reference": "REF456",
        "location_id": 1,
        "total_on_hand": 500,
        "total_expected": 550,
        "total_ordered": 100,
        "total_allocated": 200,
        "total_available": 300,
        "created_at": "2024-04-01T09:00:00Z",
        "updated_at": "2024-04-02T10:00:00Z"
    },
    {
        "id": 4,
        "item_id": 2,
        "description": "Stainless Steel Bolts",
        "item_reference": "REF456",
        "location_id": 2,
        "total_on_hand": 500,
        "total_expected": 550,
        "total_ordered": 100,
        "total_allocated": 200,
        "total_available": 300,
        "created_at": "2024-04-01T09:00:00Z",
        "updated_at": "2024-04-02T10:00:00Z"
    }
]

class Inventories(Base):
    def __init__(self, root_path, is_debug=False):
        super().__init__(root_path, "inventories.json", is_debug, CLIENTS)
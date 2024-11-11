import json
from models.base import Base

WAREHOUSES = [
    {
        "id": 1,
        "code": "WH001",
        "name": "Central Storage",
        "address": "100 Main St",
        "city": "Centerville",
        "zip_code": "90001",
        "province": "Central State",
        "country": "Centralland",
        "contact_name": "Tom Harris",
        "contact_phone": "123-456-7890",
        "contact_email": "tomh@centralstorage.com",
        "created_at": "2024-01-01T12:00:00Z",
        "updated_at": "2024-01-02T12:00:00Z"
    },
    {
        "id": 2,
        "code": "WH002",
        "name": "East Distribution Center",
        "address": "200 East Blvd",
        "city": "Eastville",
        "zip_code": "90002",
        "province": "Eastern State",
        "country": "Eastland",
        "contact_name": "Sara Miller",
        "contact_phone": "987-654-3210",
        "contact_email": "saram@eastdistrib.com",
        "created_at": "2024-02-01T15:00:00Z",
        "updated_at": "2024-02-02T16:00:00Z"
    }
]

class Warehouses(Base):
    def __init__(self, root_path, is_debug=False):
        super().__init__(root_path, "warehouses.json", is_debug, WAREHOUSES)
import json
from models.base import Base

CLIENTS = [
    {
        "id": 1,
        "name": "Alpha Industries",
        "address": "1234 Industrial Way",
        "city": "Techville",
        "zip_code": "90909",
        "province": "TechState",
        "country": "Techland",
        "contact_name": "John Doe",
        "contact_phone": "123-456-7890",
        "contact_email": "johndoe@alphaindustries.com",
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-20T10:30:00Z"
    },
    {
        "id": 2,
        "name": "Beta Corporation",
        "address": "4321 Corporate Blvd",
        "city": "MarketTown",
        "zip_code": "80808",
        "province": "BizState",
        "country": "Bizland",
        "contact_name": "Jane Smith",
        "contact_phone": "321-654-0987",
        "contact_email": "janesmith@betacorp.com",
        "created_at": "2024-02-11T14:20:00Z",
        "updated_at": "2024-02-15T15:25:00Z"
    }
]

class Inventories(Base):
    def __init__(self, root_path, is_debug=False):
        super().__init__(root_path, "inventories.json", is_debug, CLIENTS)
import json
from models.base import Base

LOCATIONS = [
    {
        "id": 1,
        "name": "Warehouse A - Section 1",
        "warehouse_id": 1,
        "description": "Section 1 of Warehouse A",
        "created_at": "2024-01-10T08:30:00Z",
        "updated_at": "2024-01-11T09:00:00Z"
    },
    {
        "id": 2,
        "name": "Warehouse B - Section 2",
        "warehouse_id": 2,
        "description": "Section 2 of Warehouse B",
        "created_at": "2024-02-20T10:00:00Z",
        "updated_at": "2024-02-21T11:20:00Z"
    }
]

class Locations(Base):
    def __init__(self, root_path, is_debug=False):
        super().__init__(root_path, "locations.json", is_debug, LOCATIONS)

    def get_locations_in_warehouse(self, warehouse_id):
        result = []
        for x in self.data:
            if x["warehouse_id"] == warehouse_id:
                result.append(x)
        return result
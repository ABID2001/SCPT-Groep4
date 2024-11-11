import json
from models.base import Base

ITEM_TYPES = [
    {
        "id": 1,
        "name": "Raw Materials",
        "description": "Basic materials used in the production of goods.",
        "created_at": "2024-02-10T08:30:00Z",
        "updated_at": "2024-02-11T09:00:00Z"
    },
    {
        "id": 2,
        "name": "Finished Goods",
        "description": "Products that are ready for sale to customers.",
        "created_at": "2024-04-20T10:00:00Z",
        "updated_at": "2024-04-21T11:20:00Z"
    }
]

class ItemTypes(Base):
    def __init__(self, root_path, is_debug=False):
        super().__init__(root_path, "item_types.json", is_debug, ITEM_TYPES)


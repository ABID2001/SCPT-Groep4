import json
from models.base import Base

ITEM_GROUPS = [
    {
        "id": 1,
        "name": "Electronics",
        "description": "All electronic devices and components.",
        "created_at": "2024-03-10T08:30:00Z",
        "updated_at": "2024-03-11T09:00:00Z"
    },
    {
        "id": 2,
        "name": "Hardware",
        "description": "Tools and hardware supplies.",
        "created_at": "2024-01-20T10:00:00Z",
        "updated_at": "2024-01-21T11:20:00Z"
    }
]

class ItemGroups(Base):
    def __init__(self, root_path, is_debug=False):
        super().__init__(root_path, "item_groups.json", is_debug, ITEM_GROUPS)
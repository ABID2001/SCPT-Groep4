import json
from models.base import Base

ITEM_LINES = [
    {
        "id": 1,
        "name": "Construction Materials",
        "description": "A comprehensive range of building and construction materials including cement, bricks, and tiles.",
        "created_at": "2024-03-05T09:00:00Z",
        "updated_at": "2024-03-06T10:00:00Z"
    },
    {
        "id": 2,
        "name": "Automotive Parts",
        "description": "Parts and accessories for various types of vehicles, focusing on both replacement parts and performance upgrades.",
        "created_at": "2024-05-01T15:00:00Z",
        "updated_at": "2024-05-02T16:30:00Z"
    }
]

class ItemLines(Base):
    def __init__(self, root_path, is_debug=False):
        super().__init__(root_path, "item_lines.json", is_debug, ITEM_LINES)

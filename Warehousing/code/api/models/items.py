import json
from models.base import Base

ITEMS = [
    {
        "id": 1,
        "name": "Item 1",
        "description": "Description for Item 1",
        "item_line_id": 1,
        "item_group_id": 1,
        "item_type_id": 1,
        "supplier_id": 1,
        "supplier_code": "SUP001",
        "supplier_part_number": "SP-2024-ABC",
        "created_at": "2024-01-01T10:00:00Z",
        "updated_at": "2024-01-02T11:00:00Z"
    },
    {
        "id": 2,
        "name": "Item 2",
        "description": "Description for Item 2",
        "item_line_id": 2,
        "item_group_id": 2,
        "item_type_id": 2,
        "supplier_id": 2,
        "supplier_code": "SUP002",
        "supplier_part_number": "HP-2024-XYZ",
        "created_at": "2024-03-20T10:00:00Z",
        "updated_at": "2024-03-20T10:00:00Z"
    }
]

class Items(Base):
    def __init__(self, root_path, is_debug=False):
        super().__init__(root_path, "items.json", is_debug, ITEMS)

    def get_items_for_item_line(self, item_line_id):
        result = []
        for x in self.data:
            if x["item_line_id"] == item_line_id:
                result.append(x["id"])
        return result

    def get_items_for_item_group(self, item_group_id):
        result = []
        for x in self.data:
            if x["item_group_id"] == item_group_id:
                result.append(x["id"])
        return result

    def get_items_for_item_type(self, item_type_id):
        result = []
        for x in self.data:
            if x["item_type_id"] == item_type_id:
                result.append(x["id"])
        return result

    def get_items_for_supplier(self, supplier_id):
        result = []
        for x in self.data:
            if x["supplier_id"] == supplier_id:
                result.append(x)
        return result
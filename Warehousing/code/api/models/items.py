import json
from Warehousing.code.api.models.base import Base

ITEMS = [

]

class Items(Base):
    def __init__(self, root_path, is_debug=False, debug_data=None):
        super().__init__(root_path, "items.json", is_debug, debug_data)

    def get_items_for_item_line(self, item_line_id):
        result = []
        for x in self.data:
            if x["item_line"] == item_line_id:  # Corrected key
                result.append(x["uid"])
        return result

    def get_items_for_item_group(self, item_group_id):
        result = []
        for x in self.data:
            if x["item_group"] == item_group_id:  # Corrected key
                result.append(x["uid"])
        return result

    def get_items_for_item_type(self, item_type_id):
        result = []
        for x in self.data:
            if x["item_type"] == item_type_id:  # Corrected key
                result.append(x["uid"])
        return result

    def get_items_for_supplier(self, supplier_id):
        result = []
        for x in self.data:
            if x["supplier_id"] == supplier_id:
                result.append(x)
        return result
    
    #item_line_id > item_line
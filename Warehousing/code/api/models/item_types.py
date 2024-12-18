import json
from Warehousing.code.api.models.base import Base

class ItemTypes(Base):
    def __init__(self, root_path, is_debug=False, debug_data=None):
        super().__init__(root_path, "item_types.json", is_debug, debug_data)
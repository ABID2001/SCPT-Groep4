import json
from Warehousing.code.api.models.base import Base

LOCATIONS = [

]

class Locations(Base):
    def __init__(self, root_path, is_debug=False, debug_data=None):
        super().__init__(root_path, "locations.json", is_debug, debug_data)

    def get_locations_in_warehouse(self, warehouse_id):
        result = []
        for x in self.data:
            if x["warehouse_id"] == warehouse_id:
                result.append(x)
        return result
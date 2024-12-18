import json
from Warehousing.code.api.models.base import Base

TRANSFERS = [

]

class Transfers(Base):
    def __init__(self, root_path, is_debug=False, debug_data=None):
        super().__init__(root_path, "transfers.json", is_debug, debug_data)

    def get_transfers_for_location(self, location_id):
        result = []
        for x in self.data:
            if x["transfer_from"] == location_id or x["transfer_to"] == location_id:
                result.append(x)
        return result

    def update_items_in_transfer(self, transfer_id, items):
        transfer = self.get_one(transfer_id)
        transfer["items"] = items
        self.update(transfer_id, transfer)
import json
from Warehousing.code.api.models.base import Base
from Warehousing.code.api import model_initializer

SHIPMENTS = [

]

class Shipments(Base):
    def __init__(self, root_path, is_debug=False, debug_data=None):
        super().__init__(root_path, "shipments.json", is_debug, debug_data)

    def get_shipments_for_order(self, order_id):
        result = []
        for x in self.data:
            if x["order_id"] == order_id:
                result.append(x)
        return result

    def update_items_in_shipment(self, shipment_id, items):
        shipment = self.get_one(shipment_id)
        current = shipment["items"]
        for x in current:
            found = False
            for y in items:
                if x["item_id"] == y["item_id"]:
                    found = True
                    break
            if not found:
                inventories = auth_provider.fetch_inventory_pool().get_inventories_for_item(x["item_id"])
                max_ordered = -1
                max_inventory = None
                for z in inventories:
                    if z["total_ordered"] > max_ordered:
                        max_ordered = z["total_ordered"]
                        max_inventory = z
                max_inventory["total_ordered"] -= x["amount"]
                max_inventory["total_expected"] = max_inventory["total_on_hand"] + max_inventory["total_ordered"]
                auth_provider.fetch_inventory_pool().update_inventory(max_inventory["id"], max_inventory)
        for x in current:
            for y in items:
                if x["item_id"] == y["item_id"]:
                    inventories = auth_provider.fetch_inventory_pool().get_inventories_for_item(x["item_id"])
                    max_ordered = -1
                    max_inventory = None
                    for z in inventories:
                        if z["total_ordered"] > max_ordered:
                            max_ordered = z["total_ordered"]
                            max_inventory = z
                    max_inventory["total_ordered"] += y["amount"] - x["amount"]
                    max_inventory["total_expected"] = max_inventory["total_on_hand"] + max_inventory["total_ordered"]
                    auth_provider.fetch_inventory_pool().update_inventory(max_inventory["id"], max_inventory)
        shipment["items"] = items
        self.update(shipment_id, shipment)
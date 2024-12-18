import json
from Warehousing.code.api.models.base import Base

ORDERS = []

class Orders(Base):
    def __init__(self, root_path, is_debug=False, debug_data=None):
        super().__init__(root_path, "orders.json", is_debug, debug_data)

    def get_orders_for_shipment(self, shipment_id):
        result = []
        for x in self.data:
            if x["shipment_id"] == shipment_id:
                result.append(x["id"])
        return result

    def get_orders_for_client(self, client_id):
        result = []
        for x in self.data:
            if x["ship_to"] == client_id or x["bill_to"] == client_id:
                result.append(x)
        return result

    def update_items_in_order(self, order_id, items):
        order = self.get_one(order_id)
        current = order["items"]
        inventories = self.inventories
        for x in current:
            found = False
            for y in items:
                if x["item_id"] == y["item_id"]:
                    found = True
                    break
            if not found:
                invs = inventories.get_inventories_for_item(x["item_id"])
                min_ordered = float('inf')
                min_inventory = None
                for z in invs:
                    if z["total_allocated"] > min_ordered:
                        min_ordered = z["total_allocated"]
                        min_inventory = z
                min_inventory["total_allocated"] -= x["amount"]
                min_inventory["total_expected"] = min_inventory["total_on_hand"] + min_inventory["total_ordered"]
                inventories.update_inventory(min_inventory["id"], min_inventory)
        for x in current:
            for y in items:
                if x["item_id"] == y["item_id"]:
                    invs = inventories.get_inventories_for_item(x["item_id"])
                    min_ordered = float('inf')
                    min_inventory = None
                    for z in invs:
                        if z["total_allocated"] > min_ordered:
                            min_ordered = z["total_allocated"]
                            min_inventory = z
                    min_inventory["total_allocated"] += y["amount"] - x["amount"]
                    min_inventory["total_expected"] = min_inventory["total_on_hand"] + min_inventory["total_ordered"]
                    inventories.update_inventory(min_inventory["id"], min_inventory)
        order["items"] = items
        self.update(order_id, order)
import json
from models.base import Base
from providers import data_provider

ORDERS = [
    {
        "id": 1,
        "order_number": "ORD001",
        "client_id": 1,
        "ship_to": 1,
        "bill_to": 1,
        "order_date": "2024-01-15T09:30:00Z",
        "shipment_id": 1,
        "items": [
            {"item_id": 1, "amount": 10},
            {"item_id": 2, "amount": 5}
        ],
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-20T10:30:00Z"
    },
    {
        "id": 2,
        "order_number": "ORD002",
        "client_id": 2,
        "ship_to": 2,
        "bill_to": 2,
        "order_date": "2024-02-11T14:20:00Z",
        "shipment_id": 2,
        "items": [
            {"item_id": 3, "amount": 20},
            {"item_id": 4, "amount": 15}
        ],
        "created_at": "2024-02-11T14:20:00Z",
        "updated_at": "2024-02-15T15:25:00Z"
    }
]

class Orders(Base):
    def __init__(self, root_path, is_debug=False):
        super().__init__(root_path, "orders.json", is_debug, ORDERS)

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
        for x in current:
            found = False
            for y in items:
                if x["item_id"] == y["item_id"]:
                    found = True
                    break
            if not found:
                inventories = data_provider.fetch_inventory_pool().get_inventories_for_item(x["item_id"])
                min_ordered = float('inf')
                min_inventory = None
                for z in inventories:
                    if z["total_allocated"] > min_ordered:
                        min_ordered = z["total_allocated"]
                        min_inventory = z
                min_inventory["total_allocated"] -= x["amount"]
                min_inventory["total_expected"] = min_inventory["total_on_hand"] + min_inventory["total_ordered"]
                data_provider.fetch_inventory_pool().update_inventory(min_inventory["id"], min_inventory)
        for x in current:
            for y in items:
                if x["item_id"] == y["item_id"]:
                    inventories = data_provider.fetch_inventory_pool().get_inventories_for_item(x["item_id"])
                    min_ordered = float('inf')
                    min_inventory = None
                    for z in inventories:
                        if z["total_allocated"] > min_ordered:
                            min_ordered = z["total_allocated"]
                            min_inventory = z
                    min_inventory["total_allocated"] += y["amount"] - x["amount"]
                    min_inventory["total_expected"] = min_inventory["total_on_hand"] + min_inventory["total_ordered"]
                    data_provider.fetch_inventory_pool().update_inventory(min_inventory["id"], min_inventory)
        order["items"] = items
        self.update(order_id, order)
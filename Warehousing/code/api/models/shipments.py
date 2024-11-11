import json
from models.base import Base
from providers import data_provider

SHIPMENTS = [
    {
        "id": 1,
        "order_id": 1,
        "source_id": 501,
        "order_date": "2024-05-01",
        "request_date": "2024-05-03",
        "shipment_date": "2024-05-05",
        "shipment_type": "Incoming",
        "shipment_status": "Transit",
        "notes": "Express shipment for urgent requirement.",
        "carrier_code": "UPS",
        "carrier_description": "United Parcel Service",
        "service_code": "NextDay",
        "payment_type": "Manual",
        "transfer_mode": "Air",
        "total_package_count": 10,
        "total_package_weight": 200.5,
        "created_at": "2024-05-01T12:00:00Z",
        "updated_at": "2024-05-02T14:00:00Z",
        "items": [
            {
                "item_id": 1,
                "amount": 5
            },
            {
                "item_id": 2,
                "amount": 10
            }
        ]
    },
    {
        "id": 2,
        "order_id": 2,
        "source_id": 502,
        "order_date": "2024-04-28",
        "request_date": "2024-05-01",
        "shipment_date": "2024-05-02",
        "shipment_type": "Outgoing",
        "shipment_status": "Delivered",
        "notes": "Standard shipping, handle with care.",
        "carrier_code": "FEDEX",
        "carrier_description": "Federal Express",
        "service_code": "Ground",
        "payment_type": "Automatic",
        "transfer_mode": "Road",
        "total_package_count": 3,
        "total_package_weight": 45.75,
        "created_at": "2024-04-28T16:30:00Z",
        "updated_at": "2024-05-03T10:00:00Z",
        "items": [
            {
                "item_id": 1,
                "amount": 15
            },
            {
                "item_id": 2,
                "amount": 20
            }
        ]
    }
]

class Shipments(Base):
    def __init__(self, root_path, is_debug=False):
        super().__init__(root_path, "shipments.json", is_debug, SHIPMENTS)

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
                inventories = data_provider.fetch_inventory_pool().get_inventories_for_item(x["item_id"])
                max_ordered = -1
                max_inventory = None
                for z in inventories:
                    if z["total_ordered"] > max_ordered:
                        max_ordered = z["total_ordered"]
                        max_inventory = z
                max_inventory["total_ordered"] -= x["amount"]
                max_inventory["total_expected"] = max_inventory["total_on_hand"] + max_inventory["total_ordered"]
                data_provider.fetch_inventory_pool().update_inventory(max_inventory["id"], max_inventory)
        for x in current:
            for y in items:
                if x["item_id"] == y["item_id"]:
                    inventories = data_provider.fetch_inventory_pool().get_inventories_for_item(x["item_id"])
                    max_ordered = -1
                    max_inventory = None
                    for z in inventories:
                        if z["total_ordered"] > max_ordered:
                            max_ordered = z["total_ordered"]
                            max_inventory = z
                    max_inventory["total_ordered"] += y["amount"] - x["amount"]
                    max_inventory["total_expected"] = max_inventory["total_on_hand"] + max_inventory["total_ordered"]
                    data_provider.fetch_inventory_pool().update_inventory(max_inventory["id"], max_inventory)
        shipment["items"] = items
        self.update(shipment_id, shipment)
import json
from providers import data_provider
from mainManagement.Management import Management

class ShipmentsManagement(Management):
    def __init__(self, handler):
        super().__init__(handler)

    def get_all_items(self):
        return data_provider.fetch_shipment_pool().get_shipments()

    def get_item(self, item_id):
        return data_provider.fetch_shipment_pool().get_shipment(item_id)

    def add_item(self, item_data):
        data_provider.fetch_shipment_pool().add_shipment(item_data)

    def update_item(self, item_id, item_data):
        data_provider.fetch_shipment_pool().update_shipment(item_id, item_data)

    def delete_item(self, item_id):
        data_provider.fetch_shipment_pool().remove_shipment(item_id)
        data_provider.fetch_shipment_pool().save()
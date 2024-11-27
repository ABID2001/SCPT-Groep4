import json
from providers import data_provider
from mainManagement.Management import Management

class InventoriesManagement(Management):
    def __init__(self, handler):
        super().__init__(handler)

    def get_all_items(self):
        return data_provider.fetch_inventory_pool().get_inventories()

    def get_item(self, item_id):
        return data_provider.fetch_inventory_pool().get_inventory(item_id)

    def add_item(self, item_data):
        data_provider.fetch_inventory_pool().add_inventory(item_data)

    def update_item(self, item_id, item_data):
        data_provider.fetch_inventory_pool().update_inventory(item_id, item_data)

    def delete_item(self, item_id):
        data_provider.fetch_inventory_pool().remove_inventory(item_id)
        data_provider.fetch_inventory_pool().save()
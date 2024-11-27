import json
from providers import data_provider
from mainManagement.Management import Management

class ItemsManagement(Management):
    def __init__(self, handler):
        super().__init__(handler)

    def get_all_items(self):
        return data_provider.fetch_item_pool().get_items()

    def get_item(self, item_id):
        return data_provider.fetch_item_pool().get_item(item_id)

    def add_item(self, item_data):
        data_provider.fetch_item_pool().add_item(item_data)

    def update_item(self, item_id, item_data):
        data_provider.fetch_item_pool().update_item(item_id, item_data)

    def delete_item(self, item_id):
        data_provider.fetch_item_pool().remove_item(item_id)
        data_provider.fetch_item_pool().save()
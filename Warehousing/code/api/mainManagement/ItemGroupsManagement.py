import json
from providers import data_provider
from mainManagement.Management import Management

class ItemGroupsManagement(Management):
    def __init__(self, handler):
        super().__init__(handler)

    def get_all_items(self):
        return data_provider.fetch_item_group_pool().get_item_groups()

    def get_item(self, item_id):
        return data_provider.fetch_item_group_pool().get_item_group(item_id)

    def add_item(self, item_data):
        data_provider.fetch_item_group_pool().add_item_group(item_data)

    def update_item(self, item_id, item_data):
        data_provider.fetch_item_group_pool().update_item_group(item_id, item_data)

    def delete_item(self, item_id):
        data_provider.fetch_item_group_pool().remove_item_group(item_id)
        data_provider.fetch_item_group_pool().save()
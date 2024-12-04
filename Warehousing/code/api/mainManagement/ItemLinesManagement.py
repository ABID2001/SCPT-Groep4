import json
from ..providers import data_provider
from .Management import Management

class ItemLinesManagement(Management):
    def __init__(self, handler):
        super().__init__(handler)

    def get_all_items(self):
        return data_provider.fetch_item_line_pool().get_item_lines()

    def get_item(self, item_id):
        return data_provider.fetch_item_line_pool().get_item_line(item_id)

    def add_item(self, item_data):
        data_provider.fetch_item_line_pool().add_item_line(item_data)

    def update_item(self, item_id, item_data):
        data_provider.fetch_item_line_pool().update_item_line(item_id, item_data)

    def delete_item(self, item_id):
        data_provider.fetch_item_line_pool().remove_item_line(item_id)
        data_provider.fetch_item_line_pool().save()
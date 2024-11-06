import json
from providers import data_provider
from mainManagement.Management import Management

class OrdersManagement(Management):
    def __init__(self, handler):
        super().__init__(handler)

    def get_all_items(self):
        return data_provider.fetch_order_pool().get_orders()

    def get_item(self, item_id):
        return data_provider.fetch_order_pool().get_order(item_id)

    def add_item(self, item_data):
        data_provider.fetch_order_pool().add_order(item_data)

    def update_item(self, item_id, item_data):
        data_provider.fetch_order_pool().update_order(item_id, item_data)

    def delete_item(self, item_id):
        data_provider.fetch_order_pool().delete_order(item_id)
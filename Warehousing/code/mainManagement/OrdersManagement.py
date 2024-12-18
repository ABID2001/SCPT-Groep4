from Warehousing.code.mainManagement.BaseManagement import BaseManagement

class OrdersManagement(BaseManagement):
    def __init__(self, handler):
        super().__init__(handler)

    def get_all_items(self):
        return self.data_provider.fetch_order_pool().get_orders()

    def get_item(self, item_id):
        return self.data_provider.fetch_order_pool().get_order(item_id)

    def add_item(self, item_data):
        self.data_provider.fetch_order_pool().add_order(item_data)

    def update_item(self, item_id, item_data):
        self.data_provider.fetch_order_pool().update_order(item_id, item_data)

    def delete_item(self, item_id):
        self.data_provider.fetch_order_pool().delete_order(item_id)
        self.data_provider.fetch_order_pool().save()
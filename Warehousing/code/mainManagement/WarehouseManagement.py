from Warehousing.code.mainManagement.BaseManagement import BaseManagement

class WarehouseManagement(BaseManagement):
    def __init__(self, handler):
        super().__init__(handler)

    def get_all_items(self):
        return self.data_provider.fetch_warehouse_pool().get_warehouses()

    def get_item(self, item_id):
        return self.data_provider.fetch_warehouse_pool().get_warehouse(item_id)

    def add_item(self, item_data):
        self.data_provider.fetch_warehouse_pool().add_warehouse(item_data)

    def update_item(self, item_id, item_data):
        self.data_provider.fetch_warehouse_pool().update_warehouse(item_id, item_data)

    def delete_item(self, item_id):
        self.data_provider.fetch_warehouse_pool().remove_warehouse(item_id)
        self.data_provider.fetch_warehouse_pool().save()
from Warehousing.code.mainManagement.BaseManagement import BaseManagement

class SuppliersManagement(BaseManagement):
    def __init__(self, handler):
        super().__init__(handler)

    def get_all_items(self):
        return self.data_provider.fetch_supplier_pool().get_suppliers()

    def get_item(self, item_id):
        return self.data_provider.fetch_supplier_pool().get_supplier(item_id)

    def add_item(self, item_data):
        self.data_provider.fetch_supplier_pool().add_supplier(item_data)

    def update_item(self, item_id, item_data):
        self.data_provider.fetch_supplier_pool().update_supplier(item_id, item_data)

    def delete_item(self, item_id):
        self.data_provider.fetch_supplier_pool().delete_supplier(item_id)
        self.data_provider.fetch_supplier_pool().save()
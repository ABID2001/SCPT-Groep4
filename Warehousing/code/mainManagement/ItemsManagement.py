from Warehousing.code.mainManagement.BaseManagement import BaseManagement

class ItemsManagement(BaseManagement):
    def __init__(self, handler):
        super().__init__(handler)

    def get_all_items(self):
        return self.data_provider.fetch_item_pool().get_items()

    def get_item(self, item_id):
        return self.data_provider.fetch_item_pool().get_item(item_id)

    def add_item(self, item_data):
        self.data_provider.fetch_item_pool().add_item(item_data)

    def update_item(self, item_id, item_data):
        self.data_provider.fetch_item_pool().update_item(item_id, item_data)

    def delete_item(self, item_id):
        self.data_provider.fetch_item_pool().remove_item(item_id)
        self.data_provider.fetch_item_pool().save()
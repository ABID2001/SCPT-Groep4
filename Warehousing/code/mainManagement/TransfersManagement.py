from Warehousing.code.mainManagement.BaseManagement import BaseManagement

class TransfersManagement(BaseManagement):
    def __init__(self, handler):
        super().__init__(handler)

    def get_all_items(self):
        return self.data_provider.fetch_transfer_pool().get_transfers()

    def get_item(self, item_id):
        return self.data_provider.fetch_transfer_pool().get_transfer(item_id)

    def add_item(self, item_data):
        self.data_provider.fetch_transfer_pool().add_transfer(item_data)

    def update_item(self, item_id, item_data):
        self.data_provider.fetch_transfer_pool().update_transfer(item_id, item_data)

    def delete_item(self, item_id):
        self.data_provider.fetch_transfer_pool().delete_transfer(item_id)
        self.data_provider.fetch_transfer_pool().save()
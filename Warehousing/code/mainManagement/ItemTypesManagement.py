from Warehousing.code.mainManagement.BaseManagement import BaseManagement

class ItemTypesManagement(BaseManagement):
    def __init__(self, handler):
        super().__init__(handler)

    def get_all_items(self):
        return self.data_provider.fetch_item_type_pool().get_item_types()

    def get_item(self, item_id):
        return self.data_provider.fetch_item_type_pool().get_item_type(item_id)

    def add_item(self, item_data):
        self.data_provider.fetch_item_type_pool().add_item_type(item_data)

    def update_item(self, item_id, item_data):
        self.data_provider.fetch_item_type_pool().update_item_type(item_id, item_data)

    def delete_item(self, item_id):
        self.data_provider.fetch_item_type_pool().remove_item_type(item_id)
        self.data_provider.fetch_item_type_pool().save()

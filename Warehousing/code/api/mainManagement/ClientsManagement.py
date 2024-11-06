import json
from providers import data_provider
from mainManagement.Management import Management

class ClientsManagement(Management):
    def __init__(self, handler):
        super().__init__(handler)

    def get_all_items(self):
        return data_provider.fetch_client_pool().get_clients()

    def get_item(self, item_id):
        return data_provider.fetch_client_pool().get_client(item_id)

    def add_item(self, item_data):
        data_provider.fetch_client_pool().add_client(item_data)

    def update_item(self, item_id, item_data):
        data_provider.fetch_client_pool().update_client(item_id, item_data)

    def delete_item(self, item_id):
        data_provider.fetch_client_pool().remove_client(item_id)
        data_provider.fetch_client_pool().save()
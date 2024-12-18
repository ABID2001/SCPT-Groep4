from Warehousing.code.mainManagement.Management import Management

class ClientsManagement(Management):
    def __init__(self, handler, clients_data):
        super().__init__(handler)
        self.clients_data = clients_data

    def get_all_items(self):
        return self.clients_data

    def get_item(self, item_id):
        for client in self.clients_data:
            if client["id"] == item_id:
                return client
        return None

    def add_item(self, item_data):
        self.clients_data.append(item_data)

    def update_item(self, item_id, item_data):
        for i, client in enumerate(self.clients_data):
            if client["id"] == item_id:
                self.clients_data[i] = item_data
                return

    def delete_item(self, item_id):
        self.clients_data = [client for client in self.clients_data if client["id"] != item_id]
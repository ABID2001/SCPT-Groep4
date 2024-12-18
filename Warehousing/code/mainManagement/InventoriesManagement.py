from Warehousing.code.mainManagement.Management import Management

class InventoriesManagement(Management):
    def __init__(self, handler, inventories_data):
        super().__init__(handler)
        self.inventories_data = inventories_data

    def get_all_items(self):
        return self.inventories_data

    def get_item(self, item_id):
        for inventory in self.inventories_data:
            if inventory["id"] == item_id:
                return inventory
        return None

    def add_item(self, item_data):
        self.inventories_data.append(item_data)

    def update_item(self, item_id, item_data):
        for i, inventory in enumerate(self.inventories_data):
            if inventory["id"] == item_id:
                self.inventories_data[i] = item_data
                return

    def delete_item(self, item_id):
        self.inventories_data = [inventory for inventory in self.inventories_data if inventory["id"] != item_id]
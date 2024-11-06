import json
from providers import data_provider

class InventoriesManagement:
    def __init__(self, handler):
        self.handler = handler

    def send_json_response(self, data, status=200):
        self.handler.send_response(status)
        self.handler.send_header("Content-type", "application/json")
        self.handler.end_headers()
        self.handler.wfile.write(json.dumps(data).encode("utf-8"))

    def handle_get_request(self, path):
        paths = len(path)

        if paths == 1:
            inventories = data_provider.fetch_inventory_pool().get_inventories()
            self.send_json_response(inventories)
        elif paths == 2:
            inventory_id = int(path[1])
            inventory = data_provider.fetch_inventory_pool().get_inventory(inventory_id)
            self.send_json_response(inventory)
        else:
            self.handler.send_response(404)
            self.handler.end_headers()

    def handle_post_request(self, path):
        if len(path) == 1:
            content_length = int(self.handler.headers['Content-Length'])
            post_data = self.handler.rfile.read(content_length)
            inventory_data = json.loads(post_data)
            data_provider.fetch_inventory_pool().add_inventory(inventory_data)
            self.send_json_response({"message": "Inventory added successfully"}, 201)
        else:
            self.handler.send_response(404)
            self.handler.end_headers()

    def handle_put_request(self, path):
        if len(path) == 2:
            inventory_id = int(path[1])
            content_length = int(self.handler.headers['Content-Length'])
            put_data = self.handler.rfile.read(content_length)
            inventory_data = json.loads(put_data)
            data_provider.fetch_inventory_pool().update_inventory(inventory_id, inventory_data)
            self.send_json_response({"message": "Inventory updated successfully"})
        else:
            self.handler.send_response(404)
            self.handler.end_headers()

    def handle_delete_request(self, path):
        if len(path) == 2:
            inventory_id = int(path[1])
            data_provider.fetch_inventory_pool().delete_inventory(inventory_id)
            self.send_json_response({"message": "Inventory deleted successfully"})
        else:
            self.handler.send_response(404)
            self.handler.end_headers()
import json
from providers import data_provider
from mainManagement.Management import Management

class OrdersManagement(Management):
    def __init__(self, handler):
        self.handler = handler

    def handle_get_request(self, path):
        paths = len(path)

        if paths == 1:
            orders = data_provider.fetch_order_pool().get_orders()
            self.send_json_response(orders)
        elif paths == 2:
            order_id = int(path[1])
            order = data_provider.fetch_order_pool().get_order(order_id)
            self.send_json_response(order)
        else:
            self.handler.send_response(404)
            self.handler.end_headers()

    def handle_post_request(self, path):
        if len(path) == 1:
            content_length = int(self.handler.headers['Content-Length'])
            post_data = self.handler.rfile.read(content_length)
            order_data = json.loads(post_data)
            data_provider.fetch_order_pool().add_order(order_data)
            self.send_json_response({"message": "Order added successfully"}, 201)
        else:
            self.handler.send_response(404)
            self.handler.end_headers()

    def handle_put_request(self, path):
        if len(path) == 2:
            order_id = int(path[1])
            content_length = int(self.handler.headers['Content-Length'])
            put_data = self.handler.rfile.read(content_length)
            order_data = json.loads(put_data)
            data_provider.fetch_order_pool().update_order(order_id, order_data)
            self.send_json_response({"message": "Order updated successfully"})
        else:
            self.handler.send_response(404)
            self.handler.end_headers()

    def handle_delete_request(self, path):
        if len(path) == 2:
            order_id = int(path[1])
            data_provider.fetch_order_pool().delete_order(order_id)
            self.send_json_response({"message": "Order deleted successfully"})
        else:
            self.handler.send_response(404)
            self.handler.end_headers()
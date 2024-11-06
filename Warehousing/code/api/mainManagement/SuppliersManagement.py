import json
from providers import data_provider

class SuppliersManagement:
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
            suppliers = data_provider.fetch_supplier_pool().get_suppliers()
            self.send_json_response(suppliers)
        elif paths == 2:
            supplier_id = int(path[1])
            supplier = data_provider.fetch_supplier_pool().get_supplier(supplier_id)
            self.send_json_response(supplier)
        else:
            self.handler.send_response(404)
            self.handler.end_headers()

    def handle_post_request(self, path):
        if len(path) == 1:
            content_length = int(self.handler.headers['Content-Length'])
            post_data = self.handler.rfile.read(content_length)
            supplier_data = json.loads(post_data)
            data_provider.fetch_supplier_pool().add_supplier(supplier_data)
            self.send_json_response({"message": "Supplier added successfully"}, 201)
        else:
            self.handler.send_response(404)
            self.handler.end_headers()

    def handle_put_request(self, path):
        if len(path) == 2:
            supplier_id = int(path[1])
            content_length = int(self.handler.headers['Content-Length'])
            put_data = self.handler.rfile.read(content_length)
            supplier_data = json.loads(put_data)
            data_provider.fetch_supplier_pool().update_supplier(supplier_id, supplier_data)
            self.send_json_response({"message": "Supplier updated successfully"})
        else:
            self.handler.send_response(404)
            self.handler.end_headers()

    def handle_delete_request(self, path):
        if len(path) == 2:
            supplier_id = int(path[1])
            data_provider.fetch_supplier_pool().delete_supplier(supplier_id)
            self.send_json_response({"message": "Supplier deleted successfully"})
        else:
            self.handler.send_response(404)
            self.handler.end_headers()
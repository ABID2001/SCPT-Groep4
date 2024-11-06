import json
from providers import data_provider

class TransferManagement:
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
            transfers = data_provider.fetch_transfer_pool().get_transfers()
            self.send_json_response(transfers)
        elif paths == 2:
            transfer_id = int(path[1])
            transfer = data_provider.fetch_transfer_pool().get_transfer(transfer_id)
            self.send_json_response(transfer)
        else:
            self.handler.send_response(404)
            self.handler.end_headers()

    def handle_post_request(self, path):
        if len(path) == 1:
            content_length = int(self.handler.headers['Content-Length'])
            post_data = self.handler.rfile.read(content_length)
            transfer_data = json.loads(post_data)
            data_provider.fetch_transfer_pool().add_transfer(transfer_data)
            self.send_json_response({"message": "Transfer added successfully"}, 201)
        else:
            self.handler.send_response(404)
            self.handler.end_headers()

    def handle_put_request(self, path):
        if len(path) == 2:
            transfer_id = int(path[1])
            content_length = int(self.handler.headers['Content-Length'])
            put_data = self.handler.rfile.read(content_length)
            transfer_data = json.loads(put_data)
            data_provider.fetch_transfer_pool().update_transfer(transfer_id, transfer_data)
            self.send_json_response({"message": "Transfer updated successfully"})
        else:
            self.handler.send_response(404)
            self.handler.end_headers()

    def handle_delete_request(self, path):
        if len(path) == 2:
            transfer_id = int(path[1])
            data_provider.fetch_transfer_pool().delete_transfer(transfer_id)
            self.send_json_response({"message": "Transfer deleted successfully"})
        else:
            self.handler.send_response(404)
            self.handler.end_headers()
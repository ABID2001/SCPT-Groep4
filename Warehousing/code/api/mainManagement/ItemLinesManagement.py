import json
from providers import data_provider

class ItemLinesManagement:
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
            item_lines = data_provider.fetch_item_line_pool().get_item_lines()
            self.send_json_response(item_lines)
        elif paths == 2:
            item_line_id = int(path[1])
            item_line = data_provider.fetch_item_line_pool().get_item_line(item_line_id)
            self.send_json_response(item_line)
        else:
            self.handler.send_response(404)
            self.handler.end_headers()

    def handle_post_request(self, path):
        if len(path) == 1:
            content_length = int(self.handler.headers['Content-Length'])
            post_data = self.handler.rfile.read(content_length)
            item_line_data = json.loads(post_data)
            data_provider.fetch_item_line_pool().add_item_line(item_line_data)
            self.send_json_response({"message": "Item line added successfully"}, 201)
        else:
            self.handler.send_response(404)
            self.handler.end_headers()

    def handle_put_request(self, path):
        if len(path) == 2:
            item_line_id = int(path[1])
            content_length = int(self.handler.headers['Content-Length'])
            put_data = self.handler.rfile.read(content_length)
            item_line_data = json.loads(put_data)
            data_provider.fetch_item_line_pool().update_item_line(item_line_id, item_line_data)
            self.send_json_response({"message": "Item line updated successfully"})
        else:
            self.handler.send_response(404)
            self.handler.end_headers()

    def handle_delete_request(self, path):
        if len(path) == 2:
            item_line_id = int(path[1])
            data_provider.fetch_item_line_pool().delete_item_line(item_line_id)
            self.send_json_response({"message": "Item line deleted successfully"})
        else:
            self.handler.send_response(404)
            self.handler.end_headers()
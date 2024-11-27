from abc import ABC, abstractmethod
import json

class Management(ABC):
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
            items = self.get_all_items()
            self.send_json_response(items)
        elif paths == 2:
            item_id = int(path[1])
            item = self.get_item(item_id)
            self.send_json_response(item)
        else:
            self.handler.send_response(404)
            self.handler.end_headers()

    def handle_post_request(self, path):
        if len(path) == 1:
            content_length = int(self.handler.headers['Content-Length'])
            post_data = self.handler.rfile.read(content_length)
            item_data = json.loads(post_data)
            self.add_item(item_data)
            self.send_json_response({"message": "Item added successfully"}, 201)
        else:
            self.handler.send_response(404)
            self.handler.end_headers()

    def handle_put_request(self, path):
        if len(path) == 2:
            item_id = int(path[1])
            content_length = int(self.handler.headers['Content-Length'])
            put_data = self.handler.rfile.read(content_length)
            item_data = json.loads(put_data)
            self.update_item(item_id, item_data)
            self.send_json_response({"message": "Item updated successfully"})
        else:
            self.handler.send_response(404)
            self.handler.end_headers()

    def handle_delete_request(self, path):
        if len(path) == 2:
            item_id = int(path[1])
            self.delete_item(item_id)
            self.send_json_response({"message": "Item deleted successfully"})
        else:
            self.handler.send_response(404)
            self.handler.end_headers()

    @abstractmethod
    def get_all_items(self):
        pass

    @abstractmethod
    def get_item(self, item_id):
        pass

    @abstractmethod
    def add_item(self, item_data):
        pass

    @abstractmethod
    def update_item(self, item_id, item_data):
        pass

    @abstractmethod
    def delete_item(self, item_id):
        pass






















# from abc import ABC, abstractmethod
# import json

# class Management(ABC):
#     def __init__(self, handler):
#         self.handler = handler

#     def send_json_response(self, data, status=200):
#         self.handler.send_response(status)
#         self.handler.send_header("Content-type", "application/json")
#         self.handler.end_headers()
#         self.handler.wfile.write(json.dumps(data).encode("utf-8"))

#     @abstractmethod
#     def handle_get_request(self, path):
#         pass

#     @abstractmethod
#     def handle_post_request(self, path):
#         pass

#     @abstractmethod
#     def handle_put_request(self, path):
#         pass

#     @abstractmethod
#     def handle_delete_request(self, path):
#         pass
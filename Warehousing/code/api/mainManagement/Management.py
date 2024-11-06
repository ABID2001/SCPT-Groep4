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

    @abstractmethod
    def handle_get_request(self, path):
        pass

    @abstractmethod
    def handle_post_request(self, path):
        pass

    @abstractmethod
    def handle_put_request(self, path):
        pass

    @abstractmethod
    def handle_delete_request(self, path):
        pass
from abc import ABC, abstractmethod
import json
import os
from datetime import datetime

class Base(ABC):
    def __init__(self, root_path, file_name, is_debug=False):
        self.data_path = os.path.join(root_path, file_name)
        self.load(is_debug)

    def get_timestamp(self):
        return datetime.utcnow().isoformat() + "Z"

    def load(self, is_debug, debug_data=None):
        if is_debug and debug_data is not None:
            self.data = debug_data
        else:
            with open(self.data_path, "r") as f:
                self.data = json.load(f)

    def save(self):
        with open(self.data_path, "w") as f:
            json.dump(self.data, f)

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


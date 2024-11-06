import json
from providers import data_provider
from mainManagement.Management import Management

class ItemTypesManagement(Management):
    def __init__(self, handler):
        super().__init__(handler)

    def get_all_items(self):
        return data_provider.fetch_item_types_pool().get_item_types()

    def get_item(self, item_id):
        return data_provider.fetch_item_types_pool().get_item_type(item_id)

    def add_item(self, item_data):
        data_provider.fetch_item_types_pool().add_item_type(item_data)

    def update_item(self, item_id, item_data):
        data_provider.fetch_item_types_pool().update_item_type(item_id, item_data)

    def delete_item(self, item_id):
        data_provider.fetch_item_types_pool().remove_item_type(item_id)
        data_provider.fetch_item_types_pool().save()



# import json
# from providers import data_provider

# class ItemTypesManagement:
#     def __init__(self, handler):
#         self.handler = handler

#     def send_json_response(self, data, status=200):
#         self.handler.send_response(status)
#         self.handler.send_header("Content-type", "application/json")
#         self.handler.end_headers()
#         self.handler.wfile.write(json.dumps(data).encode("utf-8"))

#     def handle_get_request(self, path):
#         paths = len(path)

#         if paths == 1:
#             item_types = data_provider.fetch_item_types_pool().get_item_types()
#             self.send_json_response(item_types)
#         elif paths == 2:
#             item_type_id = int(path[1])
#             item_type = data_provider.fetch_item_types_pool().get_item_type(item_type_id)
#             self.send_json_response(item_type)
#         else:
#             self.handler.send_response(404)
#             self.handler.end_headers()

#     def handle_post_request(self, path):
#         if len(path) == 1:
#             content_length = int(self.handler.headers['Content-Length'])
#             post_data = self.handler.rfile.read(content_length)
#             item_type_data = json.loads(post_data)
#             data_provider.fetch_item_types_pool().add_item_type(item_type_data)
#             self.send_json_response({"message": "Item type added successfully"}, 201)
#         else:
#             self.handler.send_response(404)
#             self.handler.end_headers()

#     def handle_put_request(self, path):
#         if len(path) == 2:
#             item_type_id = int(path[1])
#             content_length = int(self.handler.headers['Content-Length'])
#             put_data = self.handler.rfile.read(content_length)
#             item_type_data = json.loads(put_data)
#             data_provider.fetch_item_types_pool().update_item_type(item_type_id, item_type_data)
#             self.send_json_response({"message": "Item type updated successfully"})
#         else:
#             self.handler.send_response(404)
#             self.handler.end_headers()

#     def handle_delete_request(self, path):
#         if len(path) == 2:
#             item_type_id = int(path[1])
#             data_provider.fetch_item_types_pool().remove_item_type(item_type_id)
#             data_provider.fetch_item_types_pool().save()
#             self.handler.send_response(200)
#             self.handler.end_headers()
#         else:
#             self.handler.send_response(404)
#             self.handler.end_headers()
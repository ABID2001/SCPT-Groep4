import json
from providers import data_provider
from mainManagement.Management import Management

class LocationManagement(Management):
    def __init__(self, handler):
        super().__init__(handler)

    def get_all_items(self):
        return data_provider.fetch_location_pool().get_locations()

    def get_item(self, item_id):
        return data_provider.fetch_location_pool().get_location(item_id)

    def add_item(self, item_data):
        data_provider.fetch_location_pool().add_location(item_data)

    def update_item(self, item_id, item_data):
        data_provider.fetch_location_pool().update_location(item_id, item_data)

    def delete_item(self, item_id):
        data_provider.fetch_location_pool().remove_location(item_id)
        data_provider.fetch_location_pool().save()

# import json
# from providers import data_provider
# from mainManagement.Management import Management

# class LocationManagement(Management):
#     def __init__(self, handler):
#         self.handler = handler

#     def handle_get_request(self, path):
#         paths = len(path)

#         if paths == 1:
#             locations = data_provider.fetch_location_pool().get_locations()
#             self.send_json_response(locations)
#         elif paths == 2:
#             location_id = int(path[1])
#             location = data_provider.fetch_location_pool().get_location(location_id)
#             self.send_json_response(location)
#         else:
#             self.handler.send_response(404)
#             self.handler.end_headers()

#     def handle_post_request(self, path):
#         if len(path) == 1:
#             content_length = int(self.handler.headers['Content-Length'])
#             post_data = self.handler.rfile.read(content_length)
#             location_data = json.loads(post_data)
#             data_provider.fetch_location_pool().add_location(location_data)
#             self.send_json_response({"message": "Location added successfully"}, 201)
#         else:
#             self.handler.send_response(404)
#             self.handler.end_headers()

#     def handle_put_request(self, path):
#         if len(path) == 2:
#             location_id = int(path[1])
#             content_length = int(self.handler.headers['Content-Length'])
#             put_data = self.handler.rfile.read(content_length)
#             location_data = json.loads(put_data)
#             data_provider.fetch_location_pool().update_location(location_id, location_data)
#             self.send_json_response({"message": "Location updated successfully"})
#         else:
#             self.handler.send_response(404)
#             self.handler.end_headers()

#     def handle_delete_request(self, path):
#         if len(path) == 2:
#             location_id = int(path[1])
#             data_provider.fetch_location_pool().remove_location(location_id)
#             data_provider.fetch_location_pool().save()
#             self.handler.send_response(200)
#             self.handler.end_headers()
#         else:
#             self.handler.send_response(404)
#             self.handler.end_headers()
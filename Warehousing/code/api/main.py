import socketserver
import http.server
import json

from providers import auth_provider
from providers import data_provider
from mainManagement import WarehouseManagement
from mainManagement import LocationManagement
from mainManagement import TransfersManagement
from mainManagement import ItemsManagement
from mainManagement import ItemLinesManagement
from mainManagement import ItemGroupsManagement
from mainManagement import ItemTypesManagement
from mainManagement import InventoriesManagement
from mainManagement import SuppliersManagement
from mainManagement import OrdersManagement
from mainManagement import ClientsManagement
from mainManagement import ShipmentsManagement


class ApiRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.handle_request("get")

    def do_POST(self):
        self.handle_request("post")

    def do_PUT(self):
        self.handle_request("put")

    def do_DELETE(self):
        self.handle_request("delete")

    def handle_request(self, method):
        api_key = self.headers.get("API_KEY")
        user = auth_provider.get_user(api_key)
        if user is None:
            self.send_response(401)
            self.end_headers()
        else:
            try:
                path = self.path.split("/")
                if len(path) > 3 and path[1] == "api" and path[2] == "v1":
                    self.handle_version_1(path[3:], user, method)
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(str(e).encode("utf-8"))

    def handle_version_1(self, path, method):
        if path[0] == "clients":
            manager = ClientsManagement(self)
        elif path[0] == "inventories":
            manager = InventoriesManagement(self)
        elif path[0] == "itemgroups":
            manager = ItemGroupsManagement(self)
        elif path[0] == "itemlines":
            manager = ItemLinesManagement(self)
        elif path[0] == "items":
            manager = ItemsManagement(self)
        elif path[0] == "itemtypes":
            manager = ItemTypesManagement(self)
        elif path[0] == "locations":
            manager = LocationManagement(self)
        elif path[0] == "orders":
            manager = OrdersManagement(self)
        elif path[0] == "shipments":
            manager = ShipmentsManagement(self)
        elif path[0] == "suppliers":
            manager = SuppliersManagement(self)
        elif path[0] == "transfers":
            manager = TransfersManagement(self)
        elif path[0] == "warehouses":
            manager = WarehouseManagement(self)
        else:
            self.send_response(404)
            self.end_headers()
            return

        if method == "get":
            manager.handle_get_request(path[1:])
        elif method == "post":
            manager.handle_post_request(path[1:])
        elif method == "put":
            manager.handle_put_request(path[1:])
        elif method == "delete":
            manager.handle_delete_request(path[1:])
        else:
            self.send_response(405)
            self.end_headers()

if __name__ == "__main__":
    PORT = 8000
    server = socketserver.TCPServer(("", PORT), ApiRequestHandler)
    print(f"Serving on port {PORT}")
    server.serve_forever()
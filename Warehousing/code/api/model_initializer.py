from Warehousing.code.api.models.warehouses import Warehouses
from Warehousing.code.api.models.locations import Locations
from Warehousing.code.api.models.transfers import Transfers
from Warehousing.code.api.models.items import Items
from Warehousing.code.api.models.item_lines import ItemLines
from Warehousing.code.api.models.item_groups import ItemGroups
from Warehousing.code.api.models.item_types import ItemTypes
from Warehousing.code.api.models.inventories import Inventories
from Warehousing.code.api.models.suppliers import Suppliers
from Warehousing.code.api.models.orders import Orders
from Warehousing.code.api.models.clients import Clients
from Warehousing.code.api.models.shipments import Shipments

DEBUG = True
ROOT_PATH = "Warehousing/code/data/"

_warehouses = None
_locations = None
_transfers = None
_items = None
_item_lines = None
_item_groups = None
_item_types = None
_inventories = None
_suppliers = None
_orders = None
_shipments = None
_clients = None

def init():
    global _warehouses, _locations, _transfers, _items, _item_lines, _item_groups, _item_types, _inventories, _suppliers, _orders, _clients, _shipments
    _warehouses = Warehouses(ROOT_PATH, DEBUG)
    _locations = Locations(ROOT_PATH, DEBUG)
    _transfers = Transfers(ROOT_PATH, DEBUG)
    _items = Items(ROOT_PATH, DEBUG)
    _item_lines = ItemLines(ROOT_PATH, DEBUG)
    _item_groups = ItemGroups(ROOT_PATH, DEBUG)
    _item_types = ItemTypes(ROOT_PATH, DEBUG)
    _inventories = Inventories(ROOT_PATH, DEBUG)
    _suppliers = Suppliers(ROOT_PATH, DEBUG)
    _orders = Orders(ROOT_PATH, DEBUG)
    _clients = Clients(ROOT_PATH, DEBUG)
    _shipments = Shipments(ROOT_PATH, DEBUG)

def get_warehouses():
    return _warehouses

def get_locations():
    return _locations

def get_transfers():
    return _transfers

def get_items():
    return _items

def get_item_lines():
    return _item_lines

def get_item_groups():
    return _item_groups

def get_item_types():
    return _item_types

def get_inventories():
    return _inventories

def get_suppliers():
    return _suppliers

def get_orders():
    return _orders

def get_clients():
    return _clients

def get_shipments():
    return _shipments
from Warehousing.code.api import model_initializer
from Warehousing.code.mainManagement.Management import Management

class BaseManagement(Management):
    def __init__(self, handler):
        super().__init__(handler)
        model_initializer.init()
        self._warehouses = model_initializer.get_warehouses()
        self._locations = model_initializer.get_locations()
        self._transfers = model_initializer.get_transfers()
        self._items = model_initializer.get_items()
        self._item_lines = model_initializer.get_item_lines()
        self._item_groups = model_initializer.get_item_groups()
        self._item_types = model_initializer.get_item_types()
        self._inventories = model_initializer.get_inventories()
        self._suppliers = model_initializer.get_suppliers()
        self._orders = model_initializer.get_orders()
        self._clients = model_initializer.get_clients()
        self._shipments = model_initializer.get_shipments()
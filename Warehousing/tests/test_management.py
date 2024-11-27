import unittest
from unittest.mock import Mock, patch
from mainManagement import (
    ClientsManagement, InventoriesManagement, ItemGroupsManagement,
    ItemLinesManagement, ItemsManagement, ItemTypesManagement,
    LocationManagement, OrdersManagement, ShipmentsManagement,
    SuppliersManagement, TransfersManagement, WarehouseManagement
)
from providers import data_provider

class TestManagementClass(Management):
    def __init__(self, data):
        self.data = data

    def test_get_all_items(self):
        self.assertEqual(self.get_all_items(), self.data)

    def test_get_item(self, item_id, expected_item):
        self.assertEqual(self.get_item(item_id), expected_item)

    def test_add_item(self, new_item):
        initial_length = len(self.data)
        self.add_item(new_item)
        self.assertEqual(len(self.data), initial_length + 1)
        self.assertEqual(self.get_item(new_item["id"]), new_item)

    def test_update_item(self, item_id, updated_item):
        self.update_item(item_id, updated_item)
        self.assertEqual(self.get_item(item_id), updated_item)

    def test_delete_item(self, item_id):
        initial_length = len(self.data)
        self.delete_item(item_id)
        self.assertEqual(len(self.data), initial_length - 1)
        self.assertIsNone(self.get_item(item_id))

class TestManagement(unittest.TestCase):

    def setUp(self):
        self.handler = Mock()

    def test_clients_management(self):
        manager = ClientsManagement(self.handler)
        with patch.object(data_provider, 'fetch_client_pool') as mock_pool:
            mock_pool.return_value.get_clients.return_value = []
            self.assertEqual(manager.get_all_items(), [])
            mock_pool.return_value.get_client.return_value = {}
            self.assertEqual(manager.get_item(1), {})
            manager.add_item({})
            mock_pool.return_value.add_client.assert_called_once()
            manager.update_item(1, {})
            mock_pool.return_value.update_client.assert_called_once()
            manager.delete_item(1)
            mock_pool.return_value.remove_client.assert_called_once()

    def test_inventories_management(self):
        manager = InventoriesManagement(self.handler)
        with patch.object(data_provider, 'fetch_inventory_pool') as mock_pool:
            mock_pool.return_value.get_inventories.return_value = []
            self.assertEqual(manager.get_all_items(), [])
            mock_pool.return_value.get_inventory.return_value = {}
            self.assertEqual(manager.get_item(1), {})
            manager.add_item({})
            mock_pool.return_value.add_inventory.assert_called_once()
            manager.update_item(1, {})
            mock_pool.return_value.update_inventory.assert_called_once()
            manager.delete_item(1)
            mock_pool.return_value.remove_inventory.assert_called_once()

    def test_item_groups_management(self):
        manager = ItemGroupsManagement(self.handler)
        with patch.object(data_provider, 'fetch_item_group_pool') as mock_pool:
            mock_pool.return_value.get_item_groups.return_value = []
            self.assertEqual(manager.get_all_items(), [])
            mock_pool.return_value.get_item_group.return_value = {}
            self.assertEqual(manager.get_item(1), {})
            manager.add_item({})
            mock_pool.return_value.add_item_group.assert_called_once()
            manager.update_item(1, {})
            mock_pool.return_value.update_item_group.assert_called_once()
            manager.delete_item(1)
            mock_pool.return_value.remove_item_group.assert_called_once()

    def test_item_lines_management(self):
        manager = ItemLinesManagement(self.handler)
        with patch.object(data_provider, 'fetch_item_line_pool') as mock_pool:
            mock_pool.return_value.get_item_lines.return_value = []
            self.assertEqual(manager.get_all_items(), [])
            mock_pool.return_value.get_item_line.return_value = {}
            self.assertEqual(manager.get_item(1), {})
            manager.add_item({})
            mock_pool.return_value.add_item_line.assert_called_once()
            manager.update_item(1, {})
            mock_pool.return_value.update_item_line.assert_called_once()
            manager.delete_item(1)
            mock_pool.return_value.remove_item_line.assert_called_once()

    def test_items_management(self):
        manager = ItemsManagement(self.handler)
        with patch.object(data_provider, 'fetch_item_pool') as mock_pool:
            mock_pool.return_value.get_items.return_value = []
            self.assertEqual(manager.get_all_items(), [])
            mock_pool.return_value.get_item.return_value = {}
            self.assertEqual(manager.get_item(1), {})
            manager.add_item({})
            mock_pool.return_value.add_item.assert_called_once()
            manager.update_item(1, {})
            mock_pool.return_value.update_item.assert_called_once()
            manager.delete_item(1)
            mock_pool.return_value.remove_item.assert_called_once()

    def test_item_types_management(self):
        manager = ItemTypesManagement(self.handler)
        with patch.object(data_provider, 'fetch_item_type_pool') as mock_pool:
            mock_pool.return_value.get_item_types.return_value = []
            self.assertEqual(manager.get_all_items(), [])
            mock_pool.return_value.get_item_type.return_value = {}
            self.assertEqual(manager.get_item(1), {})
            manager.add_item({})
            mock_pool.return_value.add_item_type.assert_called_once()
            manager.update_item(1, {})
            mock_pool.return_value.update_item_type.assert_called_once()
            manager.delete_item(1)
            mock_pool.return_value.remove_item_type.assert_called_once()

    def test_location_management(self):
        manager = LocationManagement(self.handler)
        with patch.object(data_provider, 'fetch_location_pool') as mock_pool:
            mock_pool.return_value.get_locations.return_value = []
            self.assertEqual(manager.get_all_items(), [])
            mock_pool.return_value.get_location.return_value = {}
            self.assertEqual(manager.get_item(1), {})
            manager.add_item({})
            mock_pool.return_value.add_location.assert_called_once()
            manager.update_item(1, {})
            mock_pool.return_value.update_location.assert_called_once()
            manager.delete_item(1)
            mock_pool.return_value.remove_location.assert_called_once()

    def test_orders_management(self):
        manager = OrdersManagement(self.handler)
        with patch.object(data_provider, 'fetch_order_pool') as mock_pool:
            mock_pool.return_value.get_orders.return_value = []
            self.assertEqual(manager.get_all_items(), [])
            mock_pool.return_value.get_order.return_value = {}
            self.assertEqual(manager.get_item(1), {})
            manager.add_item({})
            mock_pool.return_value.add_order.assert_called_once()
            manager.update_item(1, {})
            mock_pool.return_value.update_order.assert_called_once()
            manager.delete_item(1)
            mock_pool.return_value.remove_order.assert_called_once()

    def test_shipments_management(self):
        manager = ShipmentsManagement(self.handler)
        with patch.object(data_provider, 'fetch_shipment_pool') as mock_pool:
            mock_pool.return_value.get_shipments.return_value = []
            self.assertEqual(manager.get_all_items(), [])
            mock_pool.return_value.get_shipment.return_value = {}
            self.assertEqual(manager.get_item(1), {})
            manager.add_item({})
            mock_pool.return_value.add_shipment.assert_called_once()
            manager.update_item(1, {})
            mock_pool.return_value.update_shipment.assert_called_once()
            manager.delete_item(1)
            mock_pool.return_value.remove_shipment.assert_called_once()

    def test_suppliers_management(self):
        manager = SuppliersManagement(self.handler)
        with patch.object(data_provider, 'fetch_supplier_pool') as mock_pool:
            mock_pool.return_value.get_suppliers.return_value = []
            self.assertEqual(manager.get_all_items(), [])
            mock_pool.return_value.get_supplier.return_value = {}
            self.assertEqual(manager.get_item(1), {})
            manager.add_item({})
            mock_pool.return_value.add_supplier.assert_called_once()
            manager.update_item(1, {})
            mock_pool.return_value.update_supplier.assert_called_once()
            manager.delete_item(1)
            mock_pool.return_value.remove_supplier.assert_called_once()

    def test_transfers_management(self):
        manager = TransfersManagement(self.handler)
        with patch.object(data_provider, 'fetch_transfer_pool') as mock_pool:
            mock_pool.return_value.get_transfers.return_value = []
            self.assertEqual(manager.get_all_items(), [])
            mock_pool.return_value.get_transfer.return_value = {}
            self.assertEqual(manager.get_item(1), {})
            manager.add_item({})
            mock_pool.return_value.add_transfer.assert_called_once()
            manager.update_item(1, {})
            mock_pool.return_value.update_transfer.assert_called_once()
            manager.delete_item(1)
            mock_pool.return_value.remove_transfer.assert_called_once()

    def test_warehouse_management(self):
        manager = WarehouseManagement(self.handler)
        with patch.object(data_provider, 'fetch_warehouse_pool') as mock_pool:
            mock_pool.return_value.get_warehouses.return_value = []
            self.assertEqual(manager.get_all_items(), [])
            mock_pool.return_value.get_warehouse.return_value = {}
            self.assertEqual(manager.get_item(1), {})
            manager.add_item({})
            mock_pool.return_value.add_warehouse.assert_called_once()
            manager.update_item(1, {})
            mock_pool.return_value.update_warehouse.assert_called_once()
            manager.delete_item(1)
            mock_pool.return_value.remove_warehouse.assert_called_once()


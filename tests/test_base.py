
import unittest
from datetime import datetime, timezone

from Warehousing.code.api.models.base import Base
from Warehousing.code.api.models.items import Items
from Warehousing.code.api.models.locations import Locations
from Warehousing.code.api.models.orders import Orders
from Warehousing.code.api.models.shipments import Shipments
from Warehousing.code.api.models.transfers import Transfers
from Warehousing.code.api.models.suppliers import Suppliers
from Warehousing.code.api.models.warehouses import Warehouses
from tests.data_init import TestData

'''
cd C:/Users/Frank/SCPT-Groep4
cd C:/Users/Frank/SCPT-Groep4/tests

'''

class TestBaseClass(Base):
    def __init__(self, root_path, file_name, data):
        super().__init__(root_path, file_name, is_debug=True, debug_data=data)
        self.data = data

    def get_timestamp(self):
        return datetime.now(timezone.utc).isoformat(timespec='seconds') + "Z"

class TestBase(unittest.TestCase):
    def setUp(self):
        self.root_path = "C:/Users/Frank/SCPT-Groep4/Warehousing/tests"
        self.file_name = "test_base.json"

    class TestClients(unittest.TestCase):
        def setUp(self):
            self.root_path = "C:/Users/Frank/SCPT-Groep4/Warehousing/tests"
            self.file_name = "test_base.json"
            self.test_data = TestData.test_data_clients()
            self.test_base = TestBaseClass(self.root_path, self.file_name, self.test_data)

        def test_add(self):
            new_item = {
                "id": 5,
                "name": "New Client",
                "address": "123 New St",
                "city": "New City",
                "zip_code": "12345",
                "province": "New State",
                "country": "Newland",
                "contact_name": "New Contact",
                "contact_phone": "123-456-7890",
                "contact_email": "newcontact@newclient.com",
                "created_at": "2024-05-01T10:00:00Z",
                "updated_at": "2024-05-01T10:00:00Z"
            }
            initial_length = len(self.test_base.data)
            self.test_base.add(new_item)
            self.assertEqual(len(self.test_base.data), initial_length + 1)
            self.assertEqual(self.test_base.get_one(5)["name"], "New Client")

        def test_get_all(self):
            self.assertEqual(self.test_base.get_all(), self.test_data)

        def test_get_one(self):
            self.assertEqual(self.test_base.get_one(1), self.test_data[0])
            self.assertEqual(self.test_base.get_one(1)["name"], "Alpha Industries")

        def test_update(self):
            updated_item = {
                "id": 1,
                "name": "Updated Client",
                "address": "123 Updated St",
                "city": "Updated City",
                "zip_code": "54321",
                "province": "Updated State",
                "country": "Updatedland",
                "contact_name": "Updated Contact",
                "contact_phone": "987-654-3210",
                "contact_email": "updatedcontact@updatedclient.com",
                "created_at": "2024-01-15T09:30:00Z",
                "updated_at": "2024-01-20T10:30:00Z"
            }
            self.test_base.update(1, updated_item)
            self.assertEqual(self.test_base.get_one(1)["name"], "Updated Client")

        def test_delete(self):
            initial_length = len(self.test_base.data)
            self.test_base.delete(1)
            self.assertEqual(len(self.test_base.data), initial_length - 1)
            self.assertIsNone(self.test_base.get_one(1))

class TestInventories(unittest.TestCase):
    def setUp(self):
        self.root_path = "C:/Users/Frank/SCPT-Groep4/Warehousing/tests"
        self.file_name = "test_base.json"
        self.test_data = TestData.test_data_inventories()
        self.test_base = TestBaseClass(self.root_path, self.file_name, self.test_data)

    def test_add(self):
        new_item = {
            "id": 5,
            "description": "New Inventory",
            "created_at": "2024-05-01T10:00:00Z",
            "updated_at": "2024-05-01T10:00:00Z"
        }
        initial_length = len(self.test_base.data)
        self.test_base.add(new_item)
        self.assertEqual(len(self.test_base.data), initial_length + 1)
        self.assertEqual(self.test_base.get_one(5)["description"], "New Inventory")

    def test_get_all(self):
        self.assertEqual(self.test_base.get_all(), self.test_data)

    def test_get_one(self):
        self.assertEqual(self.test_base.get_one(1), self.test_data[0])
        self.assertEqual(self.test_base.get_one(1)["description"], "Face-to-face clear-thinking complexity")

    def test_update(self):
        updated_item = {
            "id": 1,
            "description": "Updated Inventory",
            "created_at": "2024-01-15T09:30:00Z",
            "updated_at": "2024-01-20T10:30:00Z"
        }
        self.test_base.update(1, updated_item)
        self.assertEqual(self.test_base.get_one(1)["description"], "Updated Inventory")

    def test_delete(self):
        initial_length = len(self.test_base.data)
        self.test_base.delete(1)
        self.assertEqual(len(self.test_base.data), initial_length - 1)
        self.assertIsNone(self.test_base.get_one(1))

class TestItemGroups(unittest.TestCase):
    def setUp(self):
        self.root_path = "C:/Users/Frank/SCPT-Groep4/Warehousing/tests"
        self.file_name = "test_base.json"
        self.test_data = TestData.test_data_item_groups()
        self.test_base = TestBaseClass(self.root_path, self.file_name, self.test_data)

    def test_add(self):
        new_item = {
            "id": 5,
            "name": "New Item Group",
            "created_at": "2024-05-01T10:00:00Z",
            "updated_at": "2024-05-01T10:00:00Z"
        }
        initial_length = len(self.test_base.data)
        self.test_base.add(new_item)
        self.assertEqual(len(self.test_base.data), initial_length + 1)
        self.assertEqual(self.test_base.get_one(5)["name"], "New Item Group")

    def test_get_all(self):
        self.assertEqual(self.test_base.get_all(), self.test_data)

    def test_get_one(self):
        self.assertEqual(self.test_base.get_one(0), self.test_data[0])
        self.assertEqual(self.test_base.get_one(0)["name"], "Electronics")

    def test_update(self):
        updated_item = {
            "id": 0,
            "name": "Updated Item Group",
            "created_at": "2024-01-15T09:30:00Z",
            "updated_at": "2024-01-20T10:30:00Z"
        }
        self.test_base.update(0, updated_item)
        self.assertEqual(self.test_base.get_one(0)["name"], "Updated Item Group")

    def test_delete(self):
        initial_length = len(self.test_base.data)
        self.test_base.delete(0)
        self.assertEqual(len(self.test_base.data), initial_length - 1)
        self.assertIsNone(self.test_base.get_one(0))

class TestItemLines(unittest.TestCase):
    def setUp(self):
        self.root_path = "C:/Users/Frank/SCPT-Groep4/Warehousing/tests"
        self.file_name = "test_base.json"
        self.test_data = TestData.test_data_item_lines()
        self.test_base = TestBaseClass(self.root_path, self.file_name, self.test_data)

    def test_add(self):
        new_item = {
            "id": 5,
            "name": "New Item Line",
            "created_at": "2024-05-01T10:00:00Z",
            "updated_at": "2024-05-01T10:00:00Z"
        }
        initial_length = len(self.test_base.data)
        self.test_base.add(new_item)
        self.assertEqual(len(self.test_base.data), initial_length + 1)
        self.assertEqual(self.test_base.get_one(5)["name"], "New Item Line")

    def test_get_all(self):
        self.assertEqual(self.test_base.get_all(), self.test_data)

    def test_get_one(self):
        self.assertEqual(self.test_base.get_one(1), self.test_data[0])
        self.assertEqual(self.test_base.get_one(1)["name"], "Electronics")

    def test_update(self):
        updated_item = {
            "id": 1,
            "name": "Updated Item Line",
            "created_at": "2024-01-15T09:30:00Z",
            "updated_at": "2024-01-20T10:30:00Z"
        }
        self.test_base.update(1, updated_item)
        self.assertEqual(self.test_base.get_one(1)["name"], "Updated Item Line")

    def test_delete(self):
        initial_length = len(self.test_base.data)
        self.test_base.delete(1)
        self.assertEqual(len(self.test_base.data), initial_length - 1)
        self.assertIsNone(self.test_base.get_one(1))

class TestItemTypes(unittest.TestCase):
    def setUp(self):
        self.root_path = "C:/Users/Frank/SCPT-Groep4/Warehousing/tests"
        self.file_name = "test_base.json"
        self.test_data = TestData.test_data_item_types()
        self.test_base = TestBaseClass(self.root_path, self.file_name, self.test_data)

    def test_add(self):
        new_item = {
            "id": 5,
            "name": "New Item Type",
            "created_at": "2024-05-01T10:00:00Z",
            "updated_at": "2024-05-01T10:00:00Z"
        }
        initial_length = len(self.test_base.data)
        self.test_base.add(new_item)
        self.assertEqual(len(self.test_base.data), initial_length + 1)
        self.assertEqual(self.test_base.get_one(5)["name"], "New Item Type")

    def test_get_all(self):
        self.assertEqual(self.test_base.get_all(), self.test_data)

    def test_get_one(self):
        self.assertEqual(self.test_base.get_one(1), self.test_data[0])
        self.assertEqual(self.test_base.get_one(1)["name"], "Consumables")

    def test_update(self):
        updated_item = {
            "id": 1,
            "name": "Updated Item Type",
            "created_at": "2024-01-15T09:30:00Z",
            "updated_at": "2024-01-20T10:30:00Z"
        }
        self.test_base.update(1, updated_item)
        self.assertEqual(self.test_base.get_one(1)["name"], "Updated Item Type")

    def test_delete(self):
        initial_length = len(self.test_base.data)
        self.test_base.delete(1)
        self.assertEqual(len(self.test_base.data), initial_length - 1)
        self.assertIsNone(self.test_base.get_one(1))

    def test_items(self):
        self.test_data = TestData.test_data_items()
        test_base = TestBaseClass(self.root_path, self.file_name, self.test_data)
        self.assert_timestamp_close(test_base.get_timestamp(), datetime.now(timezone.utc).isoformat(timespec='seconds') + "Z")
        self.assertEqual(test_base.get_all(), self.test_data)
        self.assertEqual(test_base.get_one("P000002"), self.test_data[0])
        self.assertEqual(test_base.get_one("P000002")["description"], "Focused transitional alliance")

    def test_locations(self):
        self.test_data = TestData.test_data_locations()
        test_base = TestBaseClass(self.root_path, self.file_name, self.test_data)
        self.assert_timestamp_close(test_base.get_timestamp(), datetime.now(timezone.utc).isoformat(timespec='seconds') + "Z")
        self.assertEqual(test_base.get_all(), self.test_data)
        self.assertEqual(test_base.get_one(1), self.test_data[0])
        self.assertEqual(test_base.get_one(1)["name"], "Row: A, Rack: 1, Shelf: 0")

    def test_orders(self):
        self.test_data = TestData.test_data_orders()
        test_base = TestBaseClass(self.root_path, self.file_name, self.test_data)
        self.assert_timestamp_close(test_base.get_timestamp(), datetime.now(timezone.utc).isoformat(timespec='seconds') + "Z")
        self.assertEqual(test_base.get_all(), self.test_data)
        self.assertEqual(test_base.get_one(1), self.test_data[0])
        self.assertEqual(test_base.get_one(1)["reference"], "ORD00001")

    def test_shipments(self):
        self.test_data = TestData.test_data_shipments()
        test_base = TestBaseClass(self.root_path, self.file_name, self.test_data)
        self.assert_timestamp_close(test_base.get_timestamp(), datetime.now(timezone.utc).isoformat(timespec='seconds') + "Z")
        self.assertEqual(test_base.get_all(), self.test_data)
        self.assertEqual(test_base.get_one(1), self.test_data[0])
        self.assertEqual(test_base.get_one(1)["carrier_code"], "DPD")

    def test_suppliers(self):
        self.test_data = TestData.test_data_suppliers()
        test_base = TestBaseClass(self.root_path, self.file_name, self.test_data)
        self.assert_timestamp_close(test_base.get_timestamp(), datetime.now(timezone.utc).isoformat(timespec='seconds') + "Z")
        self.assertEqual(test_base.get_all(), self.test_data)
        self.assertEqual(test_base.get_one(1), self.test_data[0])
        self.assertEqual(test_base.get_one(1)["name"], "Lee, Parks and Johnson")

    def test_transfers(self):
        self.test_data = TestData.test_data_transfers()
        test_base = TestBaseClass(self.root_path, self.file_name, self.test_data)
        self.assert_timestamp_close(test_base.get_timestamp(), datetime.now(timezone.utc).isoformat(timespec='seconds') + "Z")
        self.assertEqual(test_base.get_all(), self.test_data)
        self.assertEqual(test_base.get_one(1), self.test_data[0])
        self.assertEqual(test_base.get_one(1)["reference"], "TR00001")

    def test_warehouses(self):
        self.test_data = TestData.test_data_warehouses()
        test_base = TestBaseClass(self.root_path, self.file_name, self.test_data)
        self.assert_timestamp_close(test_base.get_timestamp(), datetime.now(timezone.utc).isoformat(timespec='seconds') + "Z")
        self.assertEqual(test_base.get_all(), self.test_data)
        self.assertEqual(test_base.get_one(1), self.test_data[0])
        self.assertEqual(test_base.get_one(1)["name"], "Heemskerk cargo hub")

class TestItems(unittest.TestCase):
    def setUp(self):
        self.root_path = "C:/Users/Frank/SCPT-Groep4/Warehousing/tests"
        self.file_name = "test_base.json"
        self.test_data = TestData.test_data_items()
        self.test_base = TestBaseClass(self.root_path, self.file_name, self.test_data)

    def test_add(self):
        new_item = {
            "id": 5,
            "name": "New Item",
            "created_at": "2024-05-01T10:00:00Z",
            "updated_at": "2024-05-01T10:00:00Z"
        }
        initial_length = len(self.test_base.data)
        self.test_base.add(new_item)
        self.assertEqual(len(self.test_base.data), initial_length + 1)
        self.assertEqual(self.test_base.get_one(5)["name"], "New Item")

    def test_get_all(self):
        self.assertEqual(self.test_base.get_all(), self.test_data)

    def test_get_one(self):
        self.assertEqual(self.test_base.get_one(1), self.test_data[0])
        self.assertEqual(self.test_base.get_one(1)["name"], "Item 1")

    def test_update(self):
        updated_item = {
            "id": 1,
            "name": "Updated Item",
            "created_at": "2024-01-15T09:30:00Z",
            "updated_at": "2024-01-20T10:30:00Z"
        }
        self.test_base.update(1, updated_item)
        self.assertEqual(self.test_base.get_one(1)["name"], "Updated Item")

    def test_delete(self):
        initial_length = len(self.test_base.data)
        self.test_base.delete(1)
        self.assertEqual(len(self.test_base.data), initial_length - 1)
        self.assertIsNone(self.test_base.get_one(1))

    def test_items_for_item_line(self):
        self.test_data = TestData.test_data_items()
        items = Items(self.root_path, is_debug=True)
        items.data = self.test_data
        item_line_id = 69
        expected_items = [item["id"] for item in self.test_data if item["item_line_id"] == item_line_id]
        self.assertEqual(items.get_items_for_item_line(item_line_id), expected_items)

    def test_items_for_item_group(self):
        self.test_data = TestData.test_data_items()
        items = Items(self.root_path, is_debug=True)
        items.data = self.test_data
        item_group_id = 85
        expected_items = [item["id"] for item in self.test_data if item["item_group_id"] == item_group_id]
        self.assertEqual(items.get_items_for_item_group(item_group_id), expected_items)

    def test_items_for_item_type(self):
        self.test_data = TestData.test_data_items()
        items = Items(self.root_path, is_debug=True)
        items.data = self.test_data
        item_type_id = 39
        expected_items = [item["id"] for item in self.test_data if item["item_type_id"] == item_type_id]
        self.assertEqual(items.get_items_for_item_type(item_type_id), expected_items)

    def test_items_for_supplier(self):
        self.test_data = TestData.test_data_items()
        items = Items(self.root_path, is_debug=True)
        items.data = self.test_data
        supplier_id = 57
        expected_items = [item for item in self.test_data if item["supplier_id"] == supplier_id]
        self.assertEqual(items.get_items_for_supplier(supplier_id), expected_items)

class TestLocations(unittest.TestCase):
    def setUp(self):
        self.root_path = "C:/Users/Frank/SCPT-Groep4/Warehousing/tests"
        self.file_name = "test_base.json"
        self.test_data = TestData.test_data_locations()
        self.test_base = TestBaseClass(self.root_path, self.file_name, self.test_data)

    def test_add(self):
        new_item = {
            "id": 5,
            "name": "New Location",
            "created_at": "2024-05-01T10:00:00Z",
            "updated_at": "2024-05-01T10:00:00Z"
        }
        initial_length = len(self.test_base.data)
        self.test_base.add(new_item)
        self.assertEqual(len(self.test_base.data), initial_length + 1)
        self.assertEqual(self.test_base.get_one(5)["name"], "New Location")

    def test_get_all(self):
        self.assertEqual(self.test_base.get_all(), self.test_data)

    def test_get_one(self):
        self.assertEqual(self.test_base.get_one(1), self.test_data[0])
        self.assertEqual(self.test_base.get_one(1)["name"], "Location 1")

    def test_update(self):
        updated_item = {
            "id": 1,
            "name": "Updated Location",
            "created_at": "2024-01-15T09:30:00Z",
            "updated_at": "2024-01-20T10:30:00Z"
        }
        self.test_base.update(1, updated_item)
        self.assertEqual(self.test_base.get_one(1)["name"], "Updated Location")

    def test_delete(self):
        initial_length = len(self.test_base.data)
        self.test_base.delete(1)
        self.assertEqual(len(self.test_base.data), initial_length - 1)
        self.assertIsNone(self.test_base.get_one(1))

    def test_locations_in_warehouse(self):
        self.test_data = TestData.test_data_locations()
        locations = Locations(self.root_path, is_debug=True)
        locations.data = self.test_data
        warehouse_id = 1
        expected_locations = [location for location in self.test_data if location["warehouse_id"] == warehouse_id]
        self.assertEqual(locations.get_locations_in_warehouse(warehouse_id), expected_locations)

class TestOrders(unittest.TestCase):
    def setUp(self):
        self.root_path = "C:/Users/Frank/SCPT-Groep4/Warehousing/tests"
        self.file_name = "test_base.json"
        self.test_data = TestData.test_data_orders()
        self.test_base = TestBaseClass(self.root_path, self.file_name, self.test_data)

    def test_add(self):
        new_item = {
            "id": 5,
            "reference": "ORD00005",
            "created_at": "2024-05-01T10:00:00Z",
            "updated_at": "2024-05-01T10:00:00Z"
        }
        initial_length = len(self.test_base.data)
        self.test_base.add(new_item)
        self.assertEqual(len(self.test_base.data), initial_length + 1)
        self.assertEqual(self.test_base.get_one(5)["reference"], "ORD00005")

    def test_get_all(self):
        self.assertEqual(self.test_base.get_all(), self.test_data)

    def test_get_one(self):
        self.assertEqual(self.test_base.get_one(1), self.test_data[0])
        self.assertEqual(self.test_base.get_one(1)["reference"], "ORD00001")

    def test_update(self):
        updated_item = {
            "id": 1,
            "reference": "ORD00001-Updated",
            "created_at": "2024-01-15T09:30:00Z",
            "updated_at": "2024-01-20T10:30:00Z"
        }
        self.test_base.update(1, updated_item)
        self.assertEqual(self.test_base.get_one(1)["reference"], "ORD00001-Updated")

    def test_delete(self):
        initial_length = len(self.test_base.data)
        self.test_base.delete(1)
        self.assertEqual(len(self.test_base.data), initial_length - 1)
        self.assertIsNone(self.test_base.get_one(1))

class TestShipments(unittest.TestCase):
    def setUp(self):
        self.root_path = "C:/Users/Frank/SCPT-Groep4/Warehousing/tests"

    def test_shipments_for_order(self):
        self.test_data = TestData.test_data_shipments()
        shipments = Shipments(self.root_path, is_debug=True)
        shipments.data = self.test_data
        order_id = 1
        expected_shipments = [shipment for shipment in self.test_data if shipment["order_id"] == order_id]
        self.assertEqual(shipments.get_shipments_for_order(order_id), expected_shipments)

    def test_update_items_in_shipment(self):
        self.test_data = TestData.test_data_shipments()
        shipments = Shipments(self.root_path, is_debug=True)
        shipments.data = self.test_data
        shipment_id = 1
        new_items = [
            {"item_id": "P007435", "amount": 10},
            {"item_id": "P009557", "amount": 5}
        ]
        shipments.update_items_in_shipment(shipment_id, new_items)
        updated_shipment = shipments.get_one(shipment_id)
        self.assertEqual(updated_shipment["items"], new_items)

class TestTransfers(unittest.TestCase):
    def setUp(self):
        self.root_path = "C:/Users/Frank/SCPT-Groep4/Warehousing/tests"

    def test_transfers_for_location(self):
        self.test_data = TestData.test_data_transfers()
        transfers = Transfers(self.root_path, is_debug=True)
        transfers.data = self.test_data
        location_id = 1
        expected_transfers = [transfer for transfer in self.test_data if transfer["transfer_from"] == location_id or transfer["transfer_to"] == location_id]
        self.assertEqual(transfers.get_transfers_for_location(location_id), expected_transfers)

    def test_update_items_in_transfer(self):
        self.test_data = TestData.test_data_transfers()
        transfers = Transfers(self.root_path, is_debug=True)
        transfers.data = self.test_data
        transfer_id = 1
        new_items = [
            {"item_id": "P007435", "amount": 10},
            {"item_id": "P009557", "amount": 5}
        ]
        transfers.update_items_in_transfer(transfer_id, new_items)
        updated_transfer = transfers.get_one(transfer_id)
        self.assertEqual(updated_transfer["items"], new_items)

if __name__ == "__main__":
    unittest.main()
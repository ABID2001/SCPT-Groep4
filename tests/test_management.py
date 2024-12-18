import unittest
from unittest.mock import Mock
from Warehousing.code.mainManagement.BaseManagement import BaseManagement
from .data_init import TestData

'''

'''

class TestManagementClass(BaseManagement):
    def __init__(self, handler, data):
        super().__init__(handler)
        self.data = data

    def get_all_items(self):
        return self.data

    def get_item(self, item_id):
        for item in self.data:
            if item.get("id") == item_id or item.get("uid") == item_id:
                return item
        return None

    def add_item(self, item_data):
        self.data.append(item_data)

    def update_item(self, item_id, item_data):
        for i, item in enumerate(self.data):
            if item.get("id") == item_id or item.get("uid") == item_id:
                self.data[i] = item_data
                return

    def delete_item(self, item_id):
        self.data = [item for item in self.data if item.get("id") != item_id and item.get("uid") != item_id]

class TestManagement(unittest.TestCase):

    def setUp(self):
        self.handler = Mock()

    def test_clients_management(self):
        self.test_data = TestData.test_data_clients()
        manager = TestManagementClass(self.handler, self.test_data)
        self.assertEqual(manager.get_all_items(), self.test_data)
        self.assertEqual(manager.get_item(1)["name"], "Alpha Industries")

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
        initial_length = len(manager.data)
        manager.add_item(new_item)
        self.assertEqual(len(manager.data), initial_length + 1)
        self.assertEqual(manager.get_item(5)["name"], "New Client")
        
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
        manager.update_item(1, updated_item)
        self.assertEqual(manager.get_item(1)["name"], "Updated Client")
        

        initial_length = len(manager.data)
        manager.delete_item(1)
        self.assertEqual(len(manager.data), initial_length - 1)
        self.assertIsNone(manager.get_item(1))

    def test_inventories_management(self):
        self.test_data = TestData.test_data_inventories()
        manager = TestManagementClass(self.handler, self.test_data)
        

        self.assertEqual(manager.get_all_items(), self.test_data)
        

        self.assertEqual(manager.get_item(1)["description"], "Face-to-face clear-thinking complexity")
        new_item = {
            "id": 4,
            "item_id": "P000004",
            "description": "New Inventory Item",
            "item_reference": "newRef123",
            "locations": [12345, 67890],
            "total_on_hand": 100,
            "total_expected": 50,
            "total_ordered": 30,
            "total_allocated": 20,
            "total_available": 80,
            "created_at": "2024-06-01T10:00:00Z",
            "updated_at": "2024-06-01T10:00:00Z"
        }
        initial_length = len(manager.data)
        manager.add_item(new_item)
        self.assertEqual(len(manager.data), initial_length + 1)
        self.assertEqual(manager.get_item(4)["description"], "New Inventory Item")
        
        # Test update_item
        updated_item = {
            "id": 1,
            "item_id": "P000001",
            "description": "Updated Inventory Item",
            "item_reference": "updatedRef123",
            "locations": [3211, 24700, 14123, 19538, 31071, 24701, 11606, 11817],
            "total_on_hand": 262,
            "total_expected": 0,
            "total_ordered": 80,
            "total_allocated": 41,
            "total_available": 141,
            "created_at": "2015-02-19 16:08:24",
            "updated_at": "2015-09-26 06:37:56"
        }
        manager.update_item(1, updated_item)
        self.assertEqual(manager.get_item(1)["description"], "Updated Inventory Item")
        initial_length = len(manager.data)
        manager.delete_item(1)
        self.assertEqual(len(manager.data), initial_length - 1)
        self.assertIsNone(manager.get_item(1))

    def test_item_groups_management(self):
        self.test_data = TestData.test_data_item_groups()
        manager = TestManagementClass(self.handler, self.test_data)
        self.assertEqual(manager.get_all_items(), self.test_data)
        self.assertEqual(manager.get_item(0)["name"], "Electronics")
        new_item = {
            "id": 7,
            "name": "New Item Group",
            "description": "",
            "created_at": "2024-09-01T10:00:00Z",
            "updated_at": "2024-09-02T11:00:00Z"
        }
        initial_length = len(manager.data)
        manager.add_item(new_item)
        self.assertEqual(len(manager.data), initial_length + 1)
        self.assertEqual(manager.get_item(7)["name"], "New Item Group")
        updated_item = {
            "id": 0,
            "name": "Updated Item Group",
            "description": "",
            "created_at": "1998-05-15 19:52:53",
            "updated_at": "2000-11-20 08:37:56"
        }
        manager.update_item(0, updated_item)
        self.assertEqual(manager.get_item(0)["name"], "Updated Item Group")
        initial_length = len(manager.data)
        manager.delete_item(0)
        self.assertEqual(len(manager.data), initial_length - 1)
        self.assertIsNone(manager.get_item(0))

    def test_item_lines_management(self):
        self.test_data = TestData.test_data_item_lines()
        manager = TestManagementClass(self.handler, self.test_data)
        self.assertEqual(manager.get_all_items(), self.test_data)
        self.assertEqual(manager.get_item(1)["name"], "Electronics")
        new_item = {
            "id": 7,
            "name": "New Item Line",
            "description": "",
            "created_at": "2024-09-01T10:00:00Z",
            "updated_at": "2024-09-02T11:00:00Z"
        }
        initial_length = len(manager.data)
        manager.add_item(new_item)
        self.assertEqual(len(manager.data), initial_length + 1)
        self.assertEqual(manager.get_item(7)["name"], "New Item Line")
        updated_item = {
            "id": 1,
            "name": "Updated Item Line",
            "description": "",
            "created_at": "2024-01-10 08:30:00",
            "updated_at": "2024-01-11 09:00:00"
        }
        manager.update_item(1, updated_item)
        self.assertEqual(manager.get_item(1)["name"], "Updated Item Line")
        initial_length = len(manager.data)
        manager.delete_item(1)
        self.assertEqual(len(manager.data), initial_length - 1)
        self.assertIsNone(manager.get_item(1))

    def test_item_types_management(self):
        self.test_data = TestData.test_data_item_types()
        manager = TestManagementClass(self.handler, self.test_data)
        self.assertEqual(manager.get_all_items(), self.test_data)
        self.assertEqual(manager.get_item(1)["name"], "Consumables")
        new_item = {
            "id": 7,
            "name": "New Item Type",
            "description": "Description for new item type",
            "created_at": "2024-09-01T10:00:00Z",
            "updated_at": "2024-09-02T11:00:00Z"
        }
        initial_length = len(manager.data)
        manager.add_item(new_item)
        self.assertEqual(len(manager.data), initial_length + 1)
        self.assertEqual(manager.get_item(7)["name"], "New Item Type")
        updated_item = {
            "id": 1,
            "name": "Updated Item Type",
            "description": "Updated description for item type",
            "created_at": "2024-01-15 08:30:00",
            "updated_at": "2024-01-16 09:00:00"
        }
        manager.update_item(1, updated_item)
        self.assertEqual(manager.get_item(1)["name"], "Updated Item Type")
        initial_length = len(manager.data)
        manager.delete_item(1)
        self.assertEqual(len(manager.data), initial_length - 1)
        self.assertIsNone(manager.get_item(1))

    def test_items_management(self):
        self.test_data = TestData.test_data_items()
        manager = TestManagementClass(self.handler, self.test_data)
        self.assertEqual(manager.get_all_items(), self.test_data)
        self.assertEqual(manager.get_item("P000002")["description"], "Focused transitional alliance")
        new_item = {
            "uid": "P000005",
            "code": "newCode123",
            "description": "New Item",
            "short_description": "new",
            "upc_code": "1234567890123",
            "model_number": "newModel123",
            "commodity_code": "newCommodity123",
            "item_line": 14,
            "item_group": 76,
            "item_type": 17,
            "unit_purchase_quantity": 50,
            "unit_order_quantity": 25,
            "pack_order_quantity": 15,
            "supplier_id": 37,
            "supplier_code": "SUP126",
            "supplier_part_number": "newPart123",
            "created_at": "2024-06-01T10:00:00Z",
            "updated_at": "2024-06-01T10:00:00Z"
        }
        initial_length = len(manager.data)
        manager.add_item(new_item)
        self.assertEqual(len(manager.data), initial_length + 1)
        self.assertEqual(manager.get_item("P000005")["description"], "New Item")
        updated_item = {
            "uid": "P000002",
            "code": "nyg48736S",
            "description": "Updated Item",
            "short_description": "updated",
            "upc_code": "9733132830047",
            "model_number": "ck-109684-VFb",
            "commodity_code": "y-20588-owy",
            "item_line": 69,
            "item_group": 85,
            "item_type": 39,
            "unit_purchase_quantity": 10,
            "unit_order_quantity": 15,
            "pack_order_quantity": 23,
            "supplier_id": 57,
            "supplier_code": "SUP312",
            "supplier_part_number": "j-10730-ESk",
            "created_at": "2020-05-31 16:00:08",
            "updated_at": "2020-11-08 12:49:21"
        }
        manager.update_item("P000002", updated_item)
        self.assertEqual(manager.get_item("P000002")["description"], "Updated Item")
        initial_length = len(manager.data)
        manager.delete_item("P000002")
        self.assertEqual(len(manager.data), initial_length - 1)
        self.assertIsNone(manager.get_item("P000002"))

    def test_locations_management(self):
        self.test_data = TestData.test_data_locations()
        manager = TestManagementClass(self.handler, self.test_data)
        self.assertEqual(manager.get_all_items(), self.test_data)
        self.assertEqual(manager.get_item(1)["name"], "Row: A, Rack: 1, Shelf: 0")
        new_item = {
            "id": 7,
            "warehouse_id": 7,
            "code": "G.7.6",
            "name": "Row: G, Rack: 7, Shelf: 6",
            "created_at": "2024-09-01T10:00:00Z",
            "updated_at": "2024-09-02T11:00:00Z"
        }
        initial_length = len(manager.data)
        manager.add_item(new_item)
        self.assertEqual(len(manager.data), initial_length + 1)
        self.assertEqual(manager.get_item(7)["name"], "Row: G, Rack: 7, Shelf: 6")
        updated_item = {
            "id": 1,
            "warehouse_id": 1,
            "code": "A.1.0",
            "name": "Updated Location",
            "created_at": "1992-05-15 03:21:32",
            "updated_at": "1992-05-15 03:21:32"
        }
        manager.update_item(1, updated_item)
        self.assertEqual(manager.get_item(1)["name"], "Updated Location")
        initial_length = len(manager.data)
        manager.delete_item(1)
        self.assertEqual(len(manager.data), initial_length - 1)
        self.assertIsNone(manager.get_item(1))

    def test_orders_management(self):
        self.test_data = TestData.test_data_orders()
        manager = TestManagementClass(self.handler, self.test_data)
        self.assertEqual(manager.get_all_items(), self.test_data)
        self.assertEqual(manager.get_item(1)["reference"], "ORD00001")
        new_item = {
            "id": 3,
            "source_id": 35,
            "order_date": "2024-06-01T10:00:00Z",
            "request_date": "2024-06-05T10:00:00Z",
            "reference": "ORD00003",
            "reference_extra": "Extra reference for order 3.",
            "order_status": "Pending",
            "notes": "Order notes for order 3.",
            "shipping_notes": "Shipping notes for order 3.",
            "picking_notes": "Picking notes for order 3.",
            "warehouse_id": 20,
            "ship_to": None,
            "bill_to": None,
            "shipment_id": 3,
            "total_amount": 15000.00,
            "total_discount": 300.00,
            "total_tax": 600.00,
            "total_surcharge": 150.00,
            "created_at": "2024-06-01T10:00:00Z",
            "updated_at": "2024-06-02T10:00:00Z",
            "items": [
                {
                    "item_id": "P007437",
                    "amount": 10
                },
                {
                    "item_id": "P009559",
                    "amount": 5
                }
            ]
        }
        initial_length = len(manager.data)
        manager.add_item(new_item)
        self.assertEqual(len(manager.data), initial_length + 1)
        self.assertEqual(manager.get_item(3)["reference"], "ORD00003")
        updated_item = {
            "id": 1,
            "source_id": 33,
            "order_date": "2019-04-03T11:33:15Z",
            "request_date": "2019-04-07T11:33:15Z",
            "reference": "ORD00001",
            "reference_extra": "Updated reference extra.",
            "order_status": "Delivered",
            "notes": "Updated notes.",
            "shipping_notes": "Updated shipping notes.",
            "picking_notes": "Updated picking notes.",
            "warehouse_id": 18,
            "ship_to": None,
            "bill_to": None,
            "shipment_id": 1,
            "total_amount": 9905.13,
            "total_discount": 150.77,
            "total_tax": 372.72,
            "total_surcharge": 77.6,
            "created_at": "2019-04-03T11:33:15Z",
            "updated_at": "2019-04-05T07:33:15Z",
            "items": [
                {
                    "item_id": "P007435",
                    "amount": 23
                },
                {
                    "item_id": "P009557",
                    "amount": 1
                }
            ]
        }
        manager.update_item(1, updated_item)
        self.assertEqual(manager.get_item(1)["reference_extra"], "Updated reference extra.")
        initial_length = len(manager.data)
        manager.delete_item(1)
        self.assertEqual(len(manager.data), initial_length - 1)
        self.assertIsNone(manager.get_item(1))
    
    def test_shipments_management(self):
        self.test_data = TestData.test_data_shipments()
        manager = TestManagementClass(self.handler, self.test_data)
        
        # Test get_all_items
        self.assertEqual(manager.get_all_items(), self.test_data)
        
        # Test get_item
        self.assertEqual(manager.get_item(1)["carrier_code"], "DPD")
        
        # Test add_item
        new_item = {
            "id": 3,
            "order_id": 3,
            "source_id": 35,
            "order_date": "2021-06-10",
            "request_date": "2021-06-12",
            "shipment_date": "2021-06-14",
            "shipment_type": "O",
            "shipment_status": "Pending",
            "notes": "Handle with care.",
            "carrier_code": "FedEx",
            "carrier_description": "Federal Express",
            "service_code": "Standard",
            "payment_type": "Automatic",
            "transfer_mode": "Air",
            "total_package_count": 15,
            "total_package_weight": 300.5,
            "created_at": "2021-06-10T12:00:00Z",
            "updated_at": "2021-06-11T14:00:00Z",
            "items": [
                {
                    "item_id": "P007437",
                    "amount": 5
                }
            ]
        }
        initial_length = len(manager.data)
        manager.add_item(new_item)
        self.assertEqual(len(manager.data), initial_length + 1)
        self.assertEqual(manager.get_item(3)["carrier_code"], "FedEx")
        
        # Test update_item
        updated_item = {
            "id": 1,
            "order_id": 1,
            "source_id": 33,
            "order_date": "2000-03-09",
            "request_date": "2000-03-11",
            "shipment_date": "2000-03-13",
            "shipment_type": "I",
            "shipment_status": "Delivered",
            "notes": "Updated notes.",
            "carrier_code": "DPD",
            "carrier_description": "Dynamic Parcel Distribution",
            "service_code": "Fastest",
            "payment_type": "Manual",
            "transfer_mode": "Ground",
            "total_package_count": 31,
            "total_package_weight": 594.42,
            "created_at": "2000-03-10T11:11:14Z",
            "updated_at": "2000-03-11T13:11:14Z",
            "items": [
                {
                    "item_id": "P007435",
                    "amount": 23
                },
                {
                    "item_id": "P009557",
                    "amount": 1
                }
            ]
        }
        manager.update_item(1, updated_item)
        self.assertEqual(manager.get_item(1)["shipment_status"], "Delivered")
        
        # Test delete_item
        initial_length = len(manager.data)
        manager.delete_item(1)
        self.assertEqual(len(manager.data), initial_length - 1)
        self.assertIsNone(manager.get_item(1))

    def test_suppliers_management(self):
        self.test_data = TestData.test_data_suppliers()
        manager = TestManagementClass(self.handler, self.test_data)
        
        # Test get_all_items
        self.assertEqual(manager.get_all_items(), self.test_data)
        
        # Test get_item
        self.assertEqual(manager.get_item(1)["name"], "Lee, Parks and Johnson")
        
        # Test add_item
        new_item = {
            "id": 7,
            "code": "SUP0007",
            "name": "New Supplier",
            "address": "789 New St",
            "address_extra": "Suite 100",
            "city": "New City",
            "zip_code": "12345",
            "province": "New State",
            "country": "Newland",
            "contact_name": "New Contact",
            "phonenumber": "123-456-7890",
            "reference": "NSUP0007",
            "created_at": "2024-06-01 10:00:00",
            "updated_at": "2024-06-01 10:00:00"
        }
        initial_length = len(manager.data)
        manager.add_item(new_item)
        self.assertEqual(len(manager.data), initial_length + 1)
        self.assertEqual(manager.get_item(7)["name"], "New Supplier")
        
        # Test update_item
        updated_item = {
            "id": 1,
            "code": "SUP0001",
            "name": "Updated Supplier",
            "address": "5989 Sullivan Drives",
            "address_extra": "Apt. 996",
            "city": "Port Anitaburgh",
            "zip_code": "91688",
            "province": "Illinois",
            "country": "Czech Republic",
            "contact_name": "Toni Barnett",
            "phonenumber": "363.541.7282x36825",
            "reference": "LPaJ-SUP0001",
            "created_at": "1971-10-20 18:06:17",
            "updated_at": "1985-06-08 00:13:46"
        }
        manager.update_item(1, updated_item)
        self.assertEqual(manager.get_item(1)["name"], "Updated Supplier")
        
        # Test delete_item
        initial_length = len(manager.data)
        manager.delete_item(1)
        self.assertEqual(len(manager.data), initial_length - 1)
        self.assertIsNone(manager.get_item(1))
    
    def test_transfers_management(self):
        self.test_data = TestData.test_data_transfers()
        manager = TestManagementClass(self.handler, self.test_data)
        
        # Test get_all_items
        self.assertEqual(manager.get_all_items(), self.test_data)
        
        # Test get_item
        self.assertEqual(manager.get_item(1)["reference"], "TR00001")
        
        # Test add_item
        new_item = {
            "id": 4,
            "reference": "TR00004",
            "transfer_from": 1234,
            "transfer_to": 5678,
            "transfer_status": "Pending",
            "created_at": "2021-06-10T10:20:30Z",
            "updated_at": "2021-06-11T12:30:45Z",
            "items": [
                {
                    "item_id": "P009559",
                    "amount": 5
                }
            ]
        }
        initial_length = len(manager.data)
        manager.add_item(new_item)
        self.assertEqual(len(manager.data), initial_length + 1)
        self.assertEqual(manager.get_item(4)["reference"], "TR00004")
        
        # Test update_item
        updated_item = {
            "id": 1,
            "reference": "TR00001",
            "transfer_from": None,
            "transfer_to": 9229,
            "transfer_status": "Completed",
            "created_at": "2000-03-11T13:11:14Z",
            "updated_at": "2000-03-12T16:11:14Z",
            "items": [
                {
                    "item_id": "P007435",
                    "amount": 23
                }
            ]
        }
        manager.update_item(1, updated_item)
        self.assertEqual(manager.get_item(1)["transfer_status"], "Completed")
        
        # Test delete_item
        initial_length = len(manager.data)
        manager.delete_item(1)
        self.assertEqual(len(manager.data), initial_length - 1)
        self.assertIsNone(manager.get_item(1))

    def test_warehouses_management(self):
        self.test_data = TestData.test_data_warehouses()
        manager = TestManagementClass(self.handler, self.test_data)
        
        # Test get_all_items
        self.assertEqual(manager.get_all_items(), self.test_data)
        
        # Test get_item
        self.assertEqual(manager.get_item(1)["name"], "Heemskerk cargo hub")
        
        # Test add_item
        new_item = {
            "id": 4,
            "code": "WHS0004",
            "name": "New Warehouse",
            "address": "456 New St",
            "zip": "67890",
            "city": "New City",
            "province": "New State",
            "country": "Newland",
            "contact": {
                "name": "New Contact",
                "phone": "123-456-7890",
                "email": "newcontact@newwarehouse.com"
            },
            "created_at": "2024-06-01 10:00:00",
            "updated_at": "2024-06-01 10:00:00"
        }
        initial_length = len(manager.data)
        manager.add_item(new_item)
        self.assertEqual(len(manager.data), initial_length + 1)
        self.assertEqual(manager.get_item(4)["name"], "New Warehouse")
        
        # Test update_item
        updated_item = {
            "id": 1,
            "code": "YQZZNL56",
            "name": "Updated Warehouse",
            "address": "Karlijndreef 281",
            "zip": "4002 AS",
            "city": "Heemskerk",
            "province": "Friesland",
            "country": "NL",
            "contact": {
                "name": "Fem Keijzer",
                "phone": "(078) 0013363",
                "email": "blamore@example.net"
            },
            "created_at": "1983-04-13 04:59:55",
            "updated_at": "2007-02-08 20:11:00"
        }
        manager.update_item(1, updated_item)
        self.assertEqual(manager.get_item(1)["name"], "Updated Warehouse")
        
        # Test delete_item
        initial_length = len(manager.data)
        manager.delete_item(1)
        self.assertEqual(len(manager.data), initial_length - 1)
        self.assertIsNone(manager.get_item(1))
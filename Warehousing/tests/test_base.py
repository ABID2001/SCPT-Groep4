import unittest
from code.api.models.base import Base
from datetime import datetime
from data_init import TestData

class TestBaseClass(Base):
    def __init__(self, data):
        self.data = data

    def test_get_timestamp(self):
        self.assertEqual(self.get_timestamp(), datetime.utcnow().isoformat() + "Z")

    def test_get_all(self):
        self.assertEqual(self.get_all(), self.data)

    def test_get_one(self, item_id, expected_item):
        self.assertEqual(self.get_one(item_id), expected_item)

    def test_item_attribute(self, item_id, attribute, expected_value):
        item = self.get_one(item_id)
        self.assertIsNotNone(item)
        self.assertEqual(item[attribute], expected_value)

    def test_add_item(self, new_item):
        initial_length = len(self.data)
        self.add(new_item)
        self.assertEqual(len(self.data), initial_length + 1)
        self.assertEqual(self.get_one(new_item["id"]), new_item)

    def test_update_item(self, item_id, updated_item):
        self.update(item_id, updated_item)
        self.assertEqual(self.get_one(item_id), updated_item)

    def test_delete_item(self, item_id):
        initial_length = len(self.data)
        self.delete(item_id)
        self.assertEqual(len(self.data), initial_length - 1)
        self.assertIsNone(self.get_one(item_id))

#zonder unittest.testcase heb je geen toegang tot de test methods.
class TestBase(unittest.TestCase):
    def test_clients(self):
        self.test_data = TestData.test_data_clients()
        test_base = TestBaseClass(self.test_data)
        test_base.test_get_timestamp()
        test_base.test_get_all(self)
        test_base.test_get_one(1, self.test_data[0])
        test_base.test_item_attribute(1, "name", "Alpha Industries")

    def test_inventories(self):
        self.test_data = TestData.test_data_inventories()
        test_base = TestBaseClass(self.test_data)
        test_base.test_get_timestamp()
        test_base.test_get_all(self)
        test_base.test_get_one(1, self.test_data[0])
        test_base.test_item_attribute(1, "description", "Aluminum Sheets")

    def test_item_groups(self):
        self.test_data = TestData.test_data_item_groups()
        test_base = TestBaseClass(self.test_data)
        test_base.test_get_timestamp()
        test_base.test_get_all(self)
        test_base.test_get_one(1, self.test_data[0])
        test_base.test_item_attribute(1, "name", "Furniture")

    def test_item_lines(self):
        self.test_data = TestData.test_data_item_lines()
        test_base = TestBaseClass(self.test_data)
        test_base.test_get_timestamp()
        test_base.test_get_all(self)
        test_base.test_get_one(1, self.test_data[0])
        test_base.test_item_attribute(1, "name", "Electronics")

    def test_item_types(self):
        self.test_data = TestData.test_data_item_types()
        test_base = TestBaseClass(self.test_data)
        test_base.test_get_timestamp()
        test_base.test_get_all(self)
        test_base.test_get_one(1, self.test_data[0])
        test_base.test_item_attribute(1, "name", "Consumables")

    def test_items(self):
        self.test_data = TestData.test_data_items()
        test_base = TestBaseClass(self.test_data)
        test_base.test_get_timestamp()
        test_base.test_get_all(self)
        test_base.test_get_one(1, self.test_data[0])
        test_base.test_item_attribute(1, "name", "Wireless Mouse")

    def test_locations(self):
        self.test_data = TestData.test_data_locations()
        test_base = TestBaseClass(self.test_data)
        test_base.test_get_timestamp()
        test_base.test_get_all(self)
        test_base.test_get_one(1, self.test_data[0])
        test_base.test_item_attribute(1, "name", "Warehouse C - Section 1")

    def test_orders(self):
        self.test_data = TestData.test_data_orders()
        test_base = TestBaseClass(self.test_data)
        test_base.test_get_timestamp()
        test_base.test_get_all(self)
        test_base.test_get_one(1, self.test_data[0])
        test_base.test_item_attribute(1, "order_number", "ORD003")

    def test_shipments(self):
        self.test_data = TestData.test_data_shipments()
        test_base = TestBaseClass(self.test_data)
        test_base.test_get_timestamp()
        test_base.test_get_all(self)
        test_base.test_get_one(1, self.test_data[0])
        test_base.test_item_attribute(1, "shipment_type", "Outgoing")

    def test_suppliers(self):
        self.test_data = TestData.test_data_suppliers()
        test_base = TestBaseClass(self.test_data)
        test_base.test_get_timestamp()
        test_base.test_get_all(self)
        test_base.test_get_one(1, self.test_data[0])
        test_base.test_item_attribute(1, "name", "Tech Supplies Inc.")

    def test_transfers(self):
        self.test_data = TestData.test_data_transfers()
        test_base = TestBaseClass(self.test_data)
        test_base.test_get_timestamp()
        test_base.test_get_all(self)
        test_base.test_get_one(1, self.test_data[0])
        test_base.test_item_attribute(1, "reference", "TRANS003")

    def test_warehouses(self):
        self.test_data = TestData.test_data_warehouses()
        test_base = TestBaseClass(self.test_data)
        test_base.test_get_timestamp()
        test_base.test_get_all(self)
        test_base.test_get_one(1, self.test_data[0])
        test_base.test_item_attribute(1, "name", "North Storage Facility")
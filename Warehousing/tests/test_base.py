import unittest
from datetime import datetime, timezone
from ..code.api.models.base import Base
from .data_init import TestData

'''
cd C:/Users/Frank/SCPT-Groep4
python -m unittest Warehousing/tests/test_base.py
python -m unittest -v Warehousing/tests/test_base.py
'''

class TestBaseClass(Base):
    def __init__(self, root_path, file_name, data):
        super().__init__(root_path, file_name, is_debug=True, debug_data=data)
        self.data = data

    def get_timestamp(self):
        return datetime.now(timezone.utc).isoformat(timespec='seconds') + "Z"

class TestBase(unittest.TestCase):
    def setUp(self):
        self.root_path = "some/root/path"
        self.file_name = "some_file_name"

    def assert_timestamp_close(self, actual, expected, delta=0.01):
        actual_time = datetime.fromisoformat(actual[:-1])
        expected_time = datetime.fromisoformat(expected[:-1])
        self.assertAlmostEqual(actual_time.timestamp(), expected_time.timestamp(), delta=delta)

    def test_clients(self):
        self.test_data = TestData.test_data_clients()
        test_base = TestBaseClass(self.root_path, self.file_name, self.test_data)
        self.assert_timestamp_close(test_base.get_timestamp(), datetime.now(timezone.utc).isoformat(timespec='seconds') + "Z")
        self.assertEqual(test_base.get_all(), self.test_data)
        self.assertEqual(test_base.get_one(1), self.test_data[0])
        self.assertEqual(test_base.get_one(1)["name"], "Alpha Industries")

    def test_inventories(self):
        self.test_data = TestData.test_data_inventories()
        test_base = TestBaseClass(self.root_path, self.file_name, self.test_data)
        self.assert_timestamp_close(test_base.get_timestamp(), datetime.now(timezone.utc).isoformat(timespec='seconds') + "Z")
        self.assertEqual(test_base.get_all(), self.test_data)
        self.assertEqual(test_base.get_one(1), self.test_data[0])
        self.assertEqual(test_base.get_one(1)["description"], "Face-to-face clear-thinking complexity")

    def test_item_groups(self):
        self.test_data = TestData.test_data_item_groups()
        test_base = TestBaseClass(self.root_path, self.file_name, self.test_data)
        self.assert_timestamp_close(test_base.get_timestamp(), datetime.now(timezone.utc).isoformat(timespec='seconds') + "Z")
        self.assertEqual(test_base.get_all(), self.test_data)
        self.assertEqual(test_base.get_one(0), self.test_data[0])
        self.assertEqual(test_base.get_one(0)["name"], "Electronics")

    def test_item_lines(self):
        self.test_data = TestData.test_data_item_lines()
        test_base = TestBaseClass(self.root_path, self.file_name, self.test_data)
        self.assert_timestamp_close(test_base.get_timestamp(), datetime.now(timezone.utc).isoformat(timespec='seconds') + "Z")
        self.assertEqual(test_base.get_all(), self.test_data)
        self.assertEqual(test_base.get_one(1), self.test_data[0])
        self.assertEqual(test_base.get_one(1)["name"], "Electronics")

    def test_item_types(self):
        self.test_data = TestData.test_data_item_types()
        test_base = TestBaseClass(self.root_path, self.file_name, self.test_data)
        self.assert_timestamp_close(test_base.get_timestamp(), datetime.now(timezone.utc).isoformat(timespec='seconds') + "Z")
        self.assertEqual(test_base.get_all(), self.test_data)
        self.assertEqual(test_base.get_one(1), self.test_data[0])
        self.assertEqual(test_base.get_one(1)["name"], "Consumables")

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

if __name__ == "__main__":
    unittest.main()
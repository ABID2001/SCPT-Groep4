import requests

import unittest

'''
python -m unittest -v test_api_integration.py
'''
class TestWarehouseAPI(unittest.TestCase):
    BASE_URL = "http://localhost:8000/api/v1/warehouses"

    def test_get_all_warehouses(self):
        response = requests.get(self.BASE_URL, headers={"API_KEY": "valid_api_key"})
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_warehouse(self):
        warehouse_data = {"name": "New Warehouse"}
        response = requests.post(self.BASE_URL, json=warehouse_data, headers={"API_KEY": "valid_api_key"})
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", response.json())

    def test_update_warehouse(self):
        warehouse_data = {"name": "Updated Warehouse"}
        response = requests.put(f"{self.BASE_URL}/1", json=warehouse_data, headers={"API_KEY": "valid_api_key"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())

    def test_delete_warehouse(self):
        response = requests.delete(f"{self.BASE_URL}/1", headers={"API_KEY": "valid_api_key"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())

if __name__ == "__main__":
    unittest.main()
import json
import os
import sqlite3

def get_connection():
    return sqlite3.connect('data/warehousing.db')


def migrate_clients():
    conn = get_connection()
    cur = conn.cursor()

    with open('data/clients.json') as f:
        clients = json.load(f)
        for client in clients:
            cur.execute(
                "INSERT INTO clients (id, name, address, city, zip_code, province, country, contact_name, contact_phone, contact_email, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    client['id'], client['name'], client['address'], client['city'], client['zip_code'], client['province'], client['country'], client['contact_name'],
                    client.get('contact_Phone', ''),  # Use an empty string as the default value
                    client['contact_Email'], client['created_at'], client['updated_at']
                )
            )

    conn.commit()
    cur.close()
    conn.close()

def migrate_locations():
    conn = get_connection()
    cur = conn.cursor()

    with open('data/locations.json') as f:
        locations = json.load(f)
        for location in locations:
            cur.execute(
                "INSERT INTO locations (warehouse_id, code, name, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
                (location['warehouse_id'], location['code'], location['name'], location['created_at'], location['updated_at'])
            )

    conn.commit()
    cur.close()
    conn.close()

def migrate_items():
    conn = get_connection()
    cur = conn.cursor()

    with open('data/items.json') as f:
        items = json.load(f)
        for item in items:
            cur.execute(
                "INSERT INTO items (uid, code, description, short_description, upc_code, model_number, commodity_code, item_line, item_group, item_type, unit_purchase_quantity, unit_order_quantity, pack_order_quantity, supplier_id, supplier_code, supplier_part_number, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (item['uid'], item['code'], item['description'], item['short_description'], item['upc_code'], item['model_number'], item['commodity_code'], item['item_line'], item['item_group'], item['item_type'], item['unit_purchase_quantity'], item['unit_order_quantity'], item['pack_order_quantity'], item['supplier_id'], item['supplier_code'], item['supplier_part_number'], item['created_at'], item['updated_at'])
            )

    conn.commit()
    cur.close()
    conn.close()

def migrate_suppliers():
    conn = get_connection()
    cur = conn.cursor()

    with open('data/suppliers.json') as f:
        suppliers = json.load(f)
        for supplier in suppliers:
            cur.execute(
                "INSERT INTO suppliers (id, code, name, address, address_extra, city, zip_code, province, country, contact_name, phonenumber, reference, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (supplier['id'], supplier['code'], supplier['name'], supplier['address'], supplier['address_extra'], supplier['city'], supplier['zip_code'], supplier['province'], supplier['country'], supplier['contact_name'], supplier['phonenumber'], supplier['reference'], supplier['created_at'], supplier['updated_at'])
            )

    conn.commit()
    cur.close()
    conn.close()

def migrate_warehouses():
    conn = get_connection()
    cur = conn.cursor()

    with open('data/warehouses.json') as f:
        warehouses = json.load(f)
        for warehouse in warehouses:
            cur.execute(
                "INSERT INTO warehouses (id, code, name, address, city, zip_code, province, country, contact_name, contact_phone, contact_email, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (warehouse['id'], warehouse['code'], warehouse['name'], warehouse['address'], warehouse['city'], warehouse['zip'], warehouse['province'], warehouse['country'], warehouse['contact']['name'], warehouse['contact']['phone'], warehouse['contact']['email'], warehouse['created_at'], warehouse['updated_at'])
            )

    conn.commit()
    cur.close()
    conn.close()

# Run all migrations
#migrate_clients()
#migrate_locations()
#migrate_items()
#migrate_suppliers()
migrate_warehouses()
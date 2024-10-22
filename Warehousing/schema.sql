CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    address TEXT,
    city VARCHAR(255),
    zip_code VARCHAR(50),
    province VARCHAR(255),
    country VARCHAR(255),
    contact_name VARCHAR(255),
    contact_phone VARCHAR(50),
    contact_email VARCHAR(255),
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    warehouse_id INTEGER,
    code VARCHAR(50),
    name VARCHAR(255),
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(id)
);

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    uid VARCHAR(50),
    code VARCHAR(50),
    description TEXT,
    short_description VARCHAR(255),
    upc_code VARCHAR(50),
    model_number VARCHAR(50),
    commodity_code VARCHAR(50),
    item_line VARCHAR(255),
    item_group VARCHAR(255),
    item_type VARCHAR(255),
    unit_purchase_quantity INTEGER,
    unit_order_quantity INTEGER,
    pack_order_quantity INTEGER,
    supplier_id INTEGER,
    supplier_code VARCHAR(50),
    supplier_part_number VARCHAR(50),
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
);

CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    code VARCHAR(50),
    name VARCHAR(255),
    address TEXT,
    address_extra TEXT,
    city VARCHAR(255),
    zip_code VARCHAR(50),
    province VARCHAR(255),
    country VARCHAR(255),
    contact_name VARCHAR(255),
    phonenumber VARCHAR(50),
    reference VARCHAR(50),
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE warehouses (
    id SERIAL PRIMARY KEY,
    code VARCHAR(50),
    name VARCHAR(255),
    address TEXT,
    city VARCHAR(255),
    zip_code VARCHAR(50),
    province VARCHAR(255),
    country VARCHAR(255),
    contact_name VARCHAR(255),
    contact_phone VARCHAR(50),
    contact_email VARCHAR(255),
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);
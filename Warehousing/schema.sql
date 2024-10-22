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
    name VARCHAR(255),
    address TEXT
);

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    price DECIMAL
);

CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    contact_name VARCHAR(255),
    contact_email VARCHAR(255),
    contact_phone VARCHAR(50)
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
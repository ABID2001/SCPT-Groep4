class TestData:
    @staticmethod
    def test_data_clients():
        return [
            {
                "id": 1,
                "name": "Alpha Industries",
                "address": "1234 Industrial Way",
                "city": "Techville",
                "zip_code": "90909",
                "province": "TechState",
                "country": "Techland",
                "contact_name": "John Doe",
                "contact_phone": "123-456-7890",
                "contact_email": "johndoe@alphaindustries.com",
                "created_at": "2024-01-15T09:30:00Z",
                "updated_at": "2024-01-20T10:30:00Z"
            },
            {
                "id": 3,
                "name": "Gamma Enterprises",
                "address": "5678 Business Park",
                "city": "Commerce City",
                "zip_code": "70707",
                "province": "TradeState",
                "country": "Bizland",
                "contact_name": "Alice Johnson",
                "contact_phone": "987-654-3210",
                "contact_email": "alicejohnson@gammaenterprises.com",
                "created_at": "2024-03-05T10:00:00Z",
                "updated_at": "2024-03-10T11:00:00Z"
            }
        ]

    @staticmethod
    def test_data_inventories():
        return [
            {
                "id": 1,
                "item_id": 3,
                "description": "Aluminum Sheets",
                "item_reference": "REF789",
                "location_id": 3,
                "total_on_hand": 300,
                "total_expected": 350,
                "total_ordered": 100,
                "total_allocated": 150,
                "total_available": 200,
                "created_at": "2024-05-01T10:00:00Z",
                "updated_at": "2024-05-02T11:00:00Z"
            },
            {
                "id": 2,
                "item_id": 4,
                "description": "Copper Wires",
                "item_reference": "REF101",
                "location_id": 4,
                "total_on_hand": 400,
                "total_expected": 450,
                "total_ordered": 150,
                "total_allocated": 200,
                "total_available": 250,
                "created_at": "2024-06-01T12:00:00Z",
                "updated_at": "2024-06-02T13:00:00Z"
            },
            {
                "id": 3,
                "item_id": 5,
                "description": "Titanium Screws",
                "item_reference": "REF202",
                "location_id": 5,
                "total_on_hand": 600,
                "total_expected": 650,
                "total_ordered": 200,
                "total_allocated": 300,
                "total_available": 350,
                "created_at": "2024-07-01T14:00:00Z",
                "updated_at": "2024-07-02T15:00:00Z"
            },
            {
                "id": 4,
                "item_id": 6,
                "description": "Plastic Gears",
                "item_reference": "REF303",
                "location_id": 6,
                "total_on_hand": 700,
                "total_expected": 750,
                "total_ordered": 250,
                "total_allocated": 350,
                "total_available": 400,
                "created_at": "2024-08-01T16:00:00Z",
                "updated_at": "2024-08-02T17:00:00Z"
            },
            {
                "id": 5,
                "item_id": 7,
                "description": "Rubber Seals",
                "item_reference": "REF404",
                "location_id": 7,
                "total_on_hand": 800,
                "total_expected": 850,
                "total_ordered": 300,
                "total_allocated": 400,
                "total_available": 450,
                "created_at": "2024-09-01T18:00:00Z",
                "updated_at": "2024-09-02T19:00:00Z"
            },
            {
                "id": 6,
                "item_id": 8,
                "description": "Ceramic Bearings",
                "item_reference": "REF505",
                "location_id": 8,
                "total_on_hand": 900,
                "total_expected": 950,
                "total_ordered": 350,
                "total_allocated": 450,
                "total_available": 500,
                "created_at": "2024-10-01T20:00:00Z",
                "updated_at": "2024-10-02T21:00:00Z"
            }
        ]

    @staticmethod
    def test_data_item_groups():
        return [
            {
                "id": 1,
                "name": "Furniture",
                "description": "All types of furniture including chairs, tables, and sofas.",
                "created_at": "2024-04-10T08:30:00Z",
                "updated_at": "2024-04-11T09:00:00Z"
            },
            {
                "id": 2,
                "name": "Stationery",
                "description": "Office supplies including pens, paper, and notebooks.",
                "created_at": "2024-05-20T10:00:00Z",
                "updated_at": "2024-05-21T11:20:00Z"
            },
            {
                "id": 3,
                "name": "Kitchenware",
                "description": "Utensils and appliances for kitchen use.",
                "created_at": "2024-06-15T12:00:00Z",
                "updated_at": "2024-06-16T13:30:00Z"
            },
            {
                "id": 4,
                "name": "Gardening",
                "description": "Tools and supplies for gardening.",
                "created_at": "2024-07-25T14:00:00Z",
                "updated_at": "2024-07-26T15:45:00Z"
            },
            {
                "id": 5,
                "name": "Toys",
                "description": "Various toys for children of all ages.",
                "created_at": "2024-08-05T16:00:00Z",
                "updated_at": "2024-08-06T17:30:00Z"
            },
            {
                "id": 6,
                "name": "Sports Equipment",
                "description": "Equipment and gear for various sports.",
                "created_at": "2024-09-10T18:00:00Z",
                "updated_at": "2024-09-11T19:00:00Z"
            }
        ]
    
    @staticmethod
    def test_data_item_lines():
        return [
            {
                "id": 1,
                "name": "Electronics",
                "description": "Devices and components including smartphones, laptops, and tablets.",
                "created_at": "2024-01-10T08:30:00Z",
                "updated_at": "2024-01-11T09:00:00Z"
            },
            {
                "id": 2,
                "name": "Furniture",
                "description": "Various types of furniture including chairs, tables, and sofas.",
                "created_at": "2024-02-20T10:00:00Z",
                "updated_at": "2024-02-21T11:20:00Z"
            },
            {
                "id": 3,
                "name": "Clothing",
                "description": "Apparel for men, women, and children including shirts, pants, and jackets.",
                "created_at": "2024-03-15T12:00:00Z",
                "updated_at": "2024-03-16T13:30:00Z"
            },
            {
                "id": 4,
                "name": "Toys",
                "description": "Toys and games for children of all ages.",
                "created_at": "2024-04-25T14:00:00Z",
                "updated_at": "2024-04-26T15:45:00Z"
            },
            {
                "id": 5,
                "name": "Sports Equipment",
                "description": "Equipment and gear for various sports including soccer, basketball, and tennis.",
                "created_at": "2024-05-05T16:00:00Z",
                "updated_at": "2024-05-06T17:30:00Z"
            },
            {
                "id": 6,
                "name": "Kitchenware",
                "description": "Utensils and appliances for kitchen use including pots, pans, and blenders.",
                "created_at": "2024-06-10T18:00:00Z",
                "updated_at": "2024-06-11T19:00:00Z"
            }
        ]
    
    @staticmethod
    def test_data_item_types():
        return [
            {
                "id": 1,
                "name": "Consumables",
                "description": "Items that are intended to be used up and replaced.",
                "created_at": "2024-01-15T08:30:00Z",
                "updated_at": "2024-01-16T09:00:00Z"
            },
            {
                "id": 2,
                "name": "Perishables",
                "description": "Items that have a limited shelf life and can spoil.",
                "created_at": "2024-02-20T10:00:00Z",
                "updated_at": "2024-02-21T11:20:00Z"
            },
            {
                "id": 3,
                "name": "Durables",
                "description": "Items that are intended to last for a long time.",
                "created_at": "2024-03-25T12:00:00Z",
                "updated_at": "2024-03-26T13:30:00Z"
            },
            {
                "id": 4,
                "name": "Luxury Goods",
                "description": "High-end items that are often considered non-essential.",
                "created_at": "2024-04-30T14:00:00Z",
                "updated_at": "2024-05-01T15:45:00Z"
            },
            {
                "id": 5,
                "name": "Industrial Supplies",
                "description": "Items used in manufacturing and industrial processes.",
                "created_at": "2024-06-05T16:00:00Z",
                "updated_at": "2024-06-06T17:30:00Z"
            },
            {
                "id": 6,
                "name": "Office Supplies",
                "description": "Items used in office settings, such as paper, pens, and staplers.",
                "created_at": "2024-07-10T18:00:00Z",
                "updated_at": "2024-07-11T19:00:00Z"
            }
        ]
    
    @staticmethod
    def test_data_items():
        return [
            {
                "id": 1,
                "name": "Wireless Mouse",
                "description": "A high-precision wireless mouse with ergonomic design.",
                "item_line_id": 1,
                "item_group_id": 1,
                "item_type_id": 1,
                "supplier_id": 1,
                "supplier_code": "SUP001",
                "supplier_part_number": "WM-2024-ABC",
                "created_at": "2024-01-10T10:00:00Z",
                "updated_at": "2024-01-11T11:00:00Z"
            },
            {
                "id": 2,
                "name": "Mechanical Keyboard",
                "description": "A durable mechanical keyboard with customizable keys.",
                "item_line_id": 2,
                "item_group_id": 2,
                "item_type_id": 2,
                "supplier_id": 2,
                "supplier_code": "SUP002",
                "supplier_part_number": "MK-2024-XYZ",
                "created_at": "2024-02-20T12:00:00Z",
                "updated_at": "2024-02-21T13:00:00Z"
            },
            {
                "id": 3,
                "name": "Gaming Headset",
                "description": "A surround sound gaming headset with noise-canceling microphone.",
                "item_line_id": 3,
                "item_group_id": 3,
                "item_type_id": 3,
                "supplier_id": 3,
                "supplier_code": "SUP003",
                "supplier_part_number": "GH-2024-DEF",
                "created_at": "2024-03-15T14:00:00Z",
                "updated_at": "2024-03-16T15:00:00Z"
            },
            {
                "id": 4,
                "name": "4K Monitor",
                "description": "A 27-inch 4K monitor with HDR support.",
                "item_line_id": 4,
                "item_group_id": 4,
                "item_type_id": 4,
                "supplier_id": 4,
                "supplier_code": "SUP004",
                "supplier_part_number": "4K-2024-GHI",
                "created_at": "2024-04-10T16:00:00Z",
                "updated_at": "2024-04-11T17:00:00Z"
            },
            {
                "id": 5,
                "name": "External SSD",
                "description": "A portable external SSD with 1TB storage capacity.",
                "item_line_id": 5,
                "item_group_id": 5,
                "item_type_id": 5,
                "supplier_id": 5,
                "supplier_code": "SUP005",
                "supplier_part_number": "SSD-2024-JKL",
                "created_at": "2024-05-05T18:00:00Z",
                "updated_at": "2024-05-06T19:00:00Z"
            },
            {
                "id": 6,
                "name": "Smartphone",
                "description": "A latest-generation smartphone with advanced features.",
                "item_line_id": 6,
                "item_group_id": 6,
                "item_type_id": 6,
                "supplier_id": 6,
                "supplier_code": "SUP006",
                "supplier_part_number": "SP-2024-MNO",
                "created_at": "2024-06-10T20:00:00Z",
                "updated_at": "2024-06-11T21:00:00Z"
            }
        ]
    
    @staticmethod
    def test_data_locations():
        return [
            {
                "id": 1,
                "name": "Warehouse C - Section 1",
                "warehouse_id": 3,
                "description": "Section 1 of Warehouse C",
                "created_at": "2024-03-10T08:30:00Z",
                "updated_at": "2024-03-11T09:00:00Z"
            },
            {
                "id": 2,
                "name": "Warehouse D - Section 2",
                "warehouse_id": 4,
                "description": "Section 2 of Warehouse D",
                "created_at": "2024-04-20T10:00:00Z",
                "updated_at": "2024-04-21T11:20:00Z"
            },
            {
                "id": 3,
                "name": "Warehouse E - Section 3",
                "warehouse_id": 5,
                "description": "Section 3 of Warehouse E",
                "created_at": "2024-05-15T12:00:00Z",
                "updated_at": "2024-05-16T13:30:00Z"
            },
            {
                "id": 4,
                "name": "Warehouse F - Section 4",
                "warehouse_id": 6,
                "description": "Section 4 of Warehouse F",
                "created_at": "2024-06-25T14:00:00Z",
                "updated_at": "2024-06-26T15:45:00Z"
            },
            {
                "id": 5,
                "name": "Warehouse G - Section 5",
                "warehouse_id": 7,
                "description": "Section 5 of Warehouse G",
                "created_at": "2024-07-05T16:00:00Z",
                "updated_at": "2024-07-06T17:30:00Z"
            },
            {
                "id": 6,
                "name": "Warehouse H - Section 6",
                "warehouse_id": 8,
                "description": "Section 6 of Warehouse H",
                "created_at": "2024-08-10T18:00:00Z",
                "updated_at": "2024-08-11T19:00:00Z"
            }
        ]
    
    @staticmethod
    def test_data_orders():
        return [
            {
                "id": 1,
                "order_number": "ORD003",
                "client_id": 3,
                "ship_to": 3,
                "bill_to": 3,
                "order_date": "2024-03-10T09:30:00Z",
                "shipment_id": 3,
                "items": [
                    {"item_id": 5, "amount": 10},
                    {"item_id": 6, "amount": 5}
                ],
                "created_at": "2024-03-10T09:30:00Z",
                "updated_at": "2024-03-15T10:30:00Z"
            },
            {
                "id": 2,
                "order_number": "ORD004",
                "client_id": 4,
                "ship_to": 4,
                "bill_to": 4,
                "order_date": "2024-04-11T14:20:00Z",
                "shipment_id": 4,
                "items": [
                    {"item_id": 7, "amount": 20},
                    {"item_id": 8, "amount": 15}
                ],
                "created_at": "2024-04-11T14:20:00Z",
                "updated_at": "2024-04-15T15:25:00Z"
            },
            {
                "id": 3,
                "order_number": "ORD005",
                "client_id": 5,
                "ship_to": 5,
                "bill_to": 5,
                "order_date": "2024-05-12T10:30:00Z",
                "shipment_id": 5,
                "items": [
                    {"item_id": 9, "amount": 30},
                    {"item_id": 10, "amount": 25}
                ],
                "created_at": "2024-05-12T10:30:00Z",
                "updated_at": "2024-05-17T11:30:00Z"
            },
            {
                "id": 4,
                "order_number": "ORD006",
                "client_id": 6,
                "ship_to": 6,
                "bill_to": 6,
                "order_date": "2024-06-13T11:40:00Z",
                "shipment_id": 6,
                "items": [
                    {"item_id": 11, "amount": 40},
                    {"item_id": 12, "amount": 35}
                ],
                "created_at": "2024-06-13T11:40:00Z",
                "updated_at": "2024-06-18T12:40:00Z"
            },
            {
                "id": 5,
                "order_number": "ORD007",
                "client_id": 7,
                "ship_to": 7,
                "bill_to": 7,
                "order_date": "2024-07-14T12:50:00Z",
                "shipment_id": 7,
                "items": [
                    {"item_id": 13, "amount": 50},
                    {"item_id": 14, "amount": 45}
                ],
                "created_at": "2024-07-14T12:50:00Z",
                "updated_at": "2024-07-19T13:50:00Z"
            },
            {
                "id": 6,
                "order_number": "ORD008",
                "client_id": 8,
                "ship_to": 8,
                "bill_to": 8,
                "order_date": "2024-08-15T13:00:00Z",
                "shipment_id": 8,
                "items": [
                    {"item_id": 15, "amount": 60},
                    {"item_id": 16, "amount": 55}
                ],
                "created_at": "2024-08-15T13:00:00Z",
                "updated_at": "2024-08-20T14:00:00Z"
            }
        ]
    
    @staticmethod
    def test_data_shipments():
        return [
            {
                "id": 1,
                "order_id": 3,
                "source_id": 601,
                "order_date": "2024-06-01",
                "request_date": "2024-06-03",
                "shipment_date": "2024-06-05",
                "shipment_type": "Outgoing",
                "shipment_status": "Delivered",
                "notes": "Standard delivery.",
                "carrier_code": "FEDEX",
                "carrier_description": "Federal Express",
                "service_code": "Ground",
                "payment_type": "Automatic",
                "transfer_mode": "Road",
                "total_package_count": 15,
                "total_package_weight": 300.75,
                "created_at": "2024-06-01T12:00:00Z",
                "updated_at": "2024-06-02T14:00:00Z",
                "items": [
                    {
                        "item_id": 5,
                        "amount": 10
                    },
                    {
                        "item_id": 6,
                        "amount": 20
                    }
                ]
            },
            {
                "id": 2,
                "order_id": 4,
                "source_id": 602,
                "order_date": "2024-07-01",
                "request_date": "2024-07-03",
                "shipment_date": "2024-07-05",
                "shipment_type": "Incoming",
                "shipment_status": "Transit",
                "notes": "Urgent shipment.",
                "carrier_code": "DHL",
                "carrier_description": "DHL Express",
                "service_code": "Express",
                "payment_type": "Manual",
                "transfer_mode": "Air",
                "total_package_count": 20,
                "total_package_weight": 400.5,
                "created_at": "2024-07-01T12:00:00Z",
                "updated_at": "2024-07-02T14:00:00Z",
                "items": [
                    {
                        "item_id": 7,
                        "amount": 15
                    },
                    {
                        "item_id": 8,
                        "amount": 25
                    }
                ]
            },
            {
                "id": 3,
                "order_id": 5,
                "source_id": 603,
                "order_date": "2024-08-01",
                "request_date": "2024-08-03",
                "shipment_date": "2024-08-05",
                "shipment_type": "Outgoing",
                "shipment_status": "Pending",
                "notes": "Handle with care.",
                "carrier_code": "UPS",
                "carrier_description": "United Parcel Service",
                "service_code": "NextDay",
                "payment_type": "Automatic",
                "transfer_mode": "Air",
                "total_package_count": 25,
                "total_package_weight": 500.25,
                "created_at": "2024-08-01T12:00:00Z",
                "updated_at": "2024-08-02T14:00:00Z",
                "items": [
                    {
                        "item_id": 9,
                        "amount": 20
                    },
                    {
                        "item_id": 10,
                        "amount": 30
                    }
                ]
            },
            {
                "id": 4,
                "order_id": 6,
                "source_id": 604,
                "order_date": "2024-09-01",
                "request_date": "2024-09-03",
                "shipment_date": "2024-09-05",
                "shipment_type": "Incoming",
                "shipment_status": "Delivered",
                "notes": "Fragile items.",
                "carrier_code": "FEDEX",
                "carrier_description": "Federal Express",
                "service_code": "Ground",
                "payment_type": "Manual",
                "transfer_mode": "Road",
                "total_package_count": 30,
                "total_package_weight": 600.5,
                "created_at": "2024-09-01T12:00:00Z",
                "updated_at": "2024-09-02T14:00:00Z",
                "items": [
                    {
                        "item_id": 11,
                        "amount": 25
                    },
                    {
                        "item_id": 12,
                        "amount": 35
                    }
                ]
            },
            {
                "id": 5,
                "order_id": 7,
                "source_id": 605,
                "order_date": "2024-10-01",
                "request_date": "2024-10-03",
                "shipment_date": "2024-10-05",
                "shipment_type": "Outgoing",
                "shipment_status": "Transit",
                "notes": "Standard delivery.",
                "carrier_code": "DHL",
                "carrier_description": "DHL Express",
                "service_code": "Express",
                "payment_type": "Automatic",
                "transfer_mode": "Air",
                "total_package_count": 35,
                "total_package_weight": 700.75,
                "created_at": "2024-10-01T12:00:00Z",
                "updated_at": "2024-10-02T14:00:00Z",
                "items": [
                    {
                        "item_id": 13,
                        "amount": 30
                    },
                    {
                        "item_id": 14,
                        "amount": 40
                    }
                ]
            },
            {
                "id": 6,
                "order_id": 8,
                "source_id": 606,
                "order_date": "2024-11-01",
                "request_date": "2024-11-03",
                "shipment_date": "2024-11-05",
                "shipment_type": "Incoming",
                "shipment_status": "Pending",
                "notes": "Handle with care.",
                "carrier_code": "UPS",
                "carrier_description": "United Parcel Service",
                "service_code": "NextDay",
                "payment_type": "Manual",
                "transfer_mode": "Air",
                "total_package_count": 40,
                "total_package_weight": 800.25,
                "created_at": "2024-11-01T12:00:00Z",
                "updated_at": "2024-11-02T14:00:00Z",
                "items": [
                    {
                        "item_id": 15,
                        "amount": 35
                    },
                    {
                        "item_id": 16,
                        "amount": 45
                    }
                ]
            }
        ]
    
    @staticmethod
    def test_data_suppliers():
        return [
            {
                "id": 1,
                "code": "SUP3001",
                "name": "Tech Supplies Inc.",
                "address": "1234 Tech Park",
                "address_extra": "Suite 100",
                "city": "Techville",
                "zip_code": "12345",
                "province": "TechState",
                "country": "Techland",
                "contact_name": "John Doe",
                "contact_phone": "+1234567890",
                "reference": "TSI3001X",
                "created_at": "2024-01-01T08:00:00Z",
                "updated_at": "2024-01-05T09:00:00Z"
            },
            {
                "id": 2,
                "code": "SUP3002",
                "name": "Industrial Components Co.",
                "address": "5678 Industrial Blvd",
                "address_extra": "Building B",
                "city": "Industropolis",
                "zip_code": "67890",
                "province": "IndustryState",
                "country": "Industland",
                "contact_name": "Jane Smith",
                "contact_phone": "+0987654321",
                "reference": "ICC3002Y",
                "created_at": "2024-02-10T10:30:00Z",
                "updated_at": "2024-02-15T11:45:00Z"
            },
            {
                "id": 3,
                "code": "SUP3003",
                "name": "Global Electronics",
                "address": "9101 Electronics Ave",
                "address_extra": "Floor 3",
                "city": "ElectroCity",
                "zip_code": "54321",
                "province": "ElectroState",
                "country": "Electroland",
                "contact_name": "Alice Brown",
                "contact_phone": "+1122334455",
                "reference": "GE3003Z",
                "created_at": "2024-03-20T12:00:00Z",
                "updated_at": "2024-03-25T13:15:00Z"
            },
            {
                "id": 4,
                "code": "SUP3004",
                "name": "Hardware Solutions",
                "address": "1213 Hardware St",
                "address_extra": "Unit 4",
                "city": "Hardwareville",
                "zip_code": "98765",
                "province": "HardwareState",
                "country": "Hardwareland",
                "contact_name": "Bob White",
                "contact_phone": "+5566778899",
                "reference": "HS3004W",
                "created_at": "2024-04-15T14:00:00Z",
                "updated_at": "2024-04-20T15:30:00Z"
            },
            {
                "id": 5,
                "code": "SUP3005",
                "name": "Office Essentials",
                "address": "1415 Office Park",
                "address_extra": "Building C",
                "city": "OfficeCity",
                "zip_code": "11223",
                "province": "OfficeState",
                "country": "Officeland",
                "contact_name": "Charlie Green",
                "contact_phone": "+6677889900",
                "reference": "OE3005V",
                "created_at": "2024-05-10T16:00:00Z",
                "updated_at": "2024-05-15T17:45:00Z"
            },
            {
                "id": 6,
                "code": "SUP3006",
                "name": "Construction Supplies Ltd.",
                "address": "1617 Construction Blvd",
                "address_extra": "Suite 200",
                "city": "ConstructCity",
                "zip_code": "33445",
                "province": "ConstructState",
                "country": "Constructland",
                "contact_name": "Diana Black",
                "contact_phone": "+7788990011",
                "reference": "CSL3006U",
                "created_at": "2024-06-20T18:00:00Z",
                "updated_at": "2024-06-25T19:00:00Z"
            }
        ]
    
    @staticmethod
    def test_data_transfers():
        return [
            {
                "id": 1,
                "reference": "TRANS003",
                "transfer_from": 3,
                "transfer_to": 4,
                "transfer_status": "Processed",
                "created_at": "2024-03-01T14:00:00Z",
                "updated_at": "2024-03-02T15:00:00Z",
                "items": [
                    {
                        "item_id": 3,
                        "amount": 50
                    },
                    {
                        "item_id": 4,
                        "amount": 30
                    }
                ]
            },
            {
                "id": 2,
                "reference": "TRANS004",
                "transfer_from": 4,
                "transfer_to": 5,
                "transfer_status": "Scheduled",
                "created_at": "2024-04-01T10:30:00Z",
                "updated_at": "2024-04-02T11:30:00Z",
                "items": [
                    {
                        "item_id": 5,
                        "amount": 20
                    },
                    {
                        "item_id": 6,
                        "amount": 40
                    }
                ]
            },
            {
                "id": 3,
                "reference": "TRANS005",
                "transfer_from": 5,
                "transfer_to": 6,
                "transfer_status": "In Transit",
                "created_at": "2024-05-01T12:00:00Z",
                "updated_at": "2024-05-02T13:00:00Z",
                "items": [
                    {
                        "item_id": 7,
                        "amount": 60
                    },
                    {
                        "item_id": 8,
                        "amount": 80
                    }
                ]
            },
            {
                "id": 4,
                "reference": "TRANS006",
                "transfer_from": 6,
                "transfer_to": 7,
                "transfer_status": "Pending",
                "created_at": "2024-06-01T14:00:00Z",
                "updated_at": "2024-06-02T15:00:00Z",
                "items": [
                    {
                        "item_id": 9,
                        "amount": 70
                    },
                    {
                        "item_id": 10,
                        "amount": 90
                    }
                ]
            },
            {
                "id": 5,
                "reference": "TRANS007",
                "transfer_from": 7,
                "transfer_to": 8,
                "transfer_status": "Completed",
                "created_at": "2024-07-01T16:00:00Z",
                "updated_at": "2024-07-02T17:00:00Z",
                "items": [
                    {
                        "item_id": 11,
                        "amount": 100
                    },
                    {
                        "item_id": 12,
                        "amount": 120
                    }
                ]
            },
            {
                "id": 6,
                "reference": "TRANS008",
                "transfer_from": 8,
                "transfer_to": 9,
                "transfer_status": "Cancelled",
                "created_at": "2024-08-01T18:00:00Z",
                "updated_at": "2024-08-02T19:00:00Z",
                "items": [
                    {
                        "item_id": 13,
                        "amount": 110
                    },
                    {
                        "item_id": 14,
                        "amount": 130
                    }
                ]
            }
        ]
    
    @staticmethod
    def test_data_warehouses():
        return [
            {
                "id": 1,
                "code": "WH003",
                "name": "North Storage Facility",
                "address": "300 North St",
                "city": "Northville",
                "zip_code": "90003",
                "province": "Northern State",
                "country": "Northland",
                "contact_name": "Alice Johnson",
                "contact_phone": "321-654-9870",
                "contact_email": "alicej@northstorage.com",
                "created_at": "2024-03-01T12:00:00Z",
                "updated_at": "2024-03-02T12:00:00Z"
            },
            {
                "id": 2,
                "code": "WH004",
                "name": "West Distribution Center",
                "address": "400 West Blvd",
                "city": "Westville",
                "zip_code": "90004",
                "province": "Western State",
                "country": "Westland",
                "contact_name": "Bob Brown",
                "contact_phone": "654-321-0987",
                "contact_email": "bobb@westdistrib.com",
                "created_at": "2024-04-01T15:00:00Z",
                "updated_at": "2024-04-02T16:00:00Z"
            },
            {
                "id": 3,
                "code": "WH005",
                "name": "South Storage Facility",
                "address": "500 South St",
                "city": "Southville",
                "zip_code": "90005",
                "province": "Southern State",
                "country": "Southland",
                "contact_name": "Charlie Green",
                "contact_phone": "987-654-3210",
                "contact_email": "charlieg@southstorage.com",
                "created_at": "2024-05-01T12:00:00Z",
                "updated_at": "2024-05-02T12:00:00Z"
            },
            {
                "id": 4,
                "code": "WH006",
                "name": "Central Distribution Hub",
                "address": "600 Central Ave",
                "city": "Central City",
                "zip_code": "90006",
                "province": "Central State",
                "country": "Centralland",
                "contact_name": "Diana White",
                "contact_phone": "123-456-7890",
                "contact_email": "dianaw@centralhub.com",
                "created_at": "2024-06-01T15:00:00Z",
                "updated_at": "2024-06-02T16:00:00Z"
            },
            {
                "id": 5,
                "code": "WH007",
                "name": "East Storage Facility",
                "address": "700 East St",
                "city": "Eastville",
                "zip_code": "90007",
                "province": "Eastern State",
                "country": "Eastland",
                "contact_name": "Eve Black",
                "contact_phone": "321-654-9870",
                "contact_email": "eveb@eaststorage.com",
                "created_at": "2024-07-01T12:00:00Z",
                "updated_at": "2024-07-02T12:00:00Z"
            },
            {
                "id": 6,
                "code": "WH008",
                "name": "West Storage Facility",
                "address": "800 West St",
                "city": "Westville",
                "zip_code": "90008",
                "province": "Western State",
                "country": "Westland",
                "contact_name": "Frank Blue",
                "contact_phone": "654-321-0987",
                "contact_email": "frankb@weststorage.com",
                "created_at": "2024-08-01T15:00:00Z",
                "updated_at": "2024-08-02T16:00:00Z"
            }
        ]

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
                "created_at": "2024-01-15 09:30:00",
                "updated_at": "2024-01-20 10:30:00"
            },
            {
                "id": 2,
                "name": "Williams Ltd",
                "address": "2989 Flores Turnpike Suite 012",
                "city": "Lake Steve",
                "zip_code": "08092",
                "province": "Arkansas",
                "country": "United States",
                "contact_name": "Megan Hayden",
                "contact_phone": "8892853366",
                "contact_email": "qortega@example.net",
                "created_at": "1973-02-24 07:36:32",
                "updated_at": "2014-06-20 17:46:19"
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
                "created_at": "2024-03-05 10:00:00",
                "updated_at": "2024-03-10 11:00:00"
            },
            {
                "id": 4,
                "name": "Raymond Inc",
                "address": "1296 Daniel Road Apt. 349",
                "city": "Pierceview",
                "zip_code": "28301",
                "province": "Colorado",
                "country": "United States",
                "contact_name": "Bryan Clark",
                "contact_phone": "242.732.3483x2573",
                "contact_email": "robertcharles@example.net",
                "created_at": "2010-04-28 02:22:53",
                "updated_at": "2022-02-09 20:22:35"
            }
        ]

    @staticmethod
    def test_data_inventories():
        return [
            {
                "id": 1,
                "item_id": "P000001",
                "description": "Face-to-face clear-thinking complexity",
                "item_reference": "sjQ23408K",
                "locations": [3211, 24700, 14123, 19538, 31071, 24701, 11606, 11817],
                "total_on_hand": 262,
                "total_expected": 0,
                "total_ordered": 80,
                "total_allocated": 41,
                "total_available": 141,
                "created_at": "2015-02-19 16:08:24",
                "updated_at": "2015-09-26 06:37:56"
            },
            {
                "id": 2,
                "item_id": "P000002",
                "description": "Streamlined holistic approach",
                "item_reference": "abC12345X",
                "locations": [1234, 5678, 91011, 121314],
                "total_on_hand": 150,
                "total_expected": 50,
                "total_ordered": 30,
                "total_allocated": 20,
                "total_available": 100,
                "created_at": "2016-03-22 10:15:30",
                "updated_at": "2016-08-15 14:22:10"
            },
            {
                "id": 3,
                "item_id": "P000003",
                "description": "Innovative user-centric solution",
                "item_reference": "xyZ67890L",
                "locations": [1516, 171819, 202122, 232425],
                "total_on_hand": 300,
                "total_expected": 100,
                "total_ordered": 60,
                "total_allocated": 40,
                "total_available": 200,
                "created_at": "2017-05-10 08:30:45",
                "updated_at": "2017-11-20 12:45:55"
            }
        ]

    @staticmethod
    def test_data_item_groups():
        return [
            {
                "id": 0,
                "name": "Electronics",
                "description": "",
                "created_at": "1998-05-15 19:52:53",
                "updated_at": "2000-11-20 08:37:56"
            },
            {
                "id": 1,
                "name": "Furniture",
                "description": "",
                "created_at": "2019-09-22 15:51:07",
                "updated_at": "2022-05-18 13:49:28"
            },
            {
                "id": 2,
                "name": "Stationery",
                "description": "",
                "created_at": "2024-05-20 10:00:00",
                "updated_at": "2024-05-21 11:20:00"
            },
            {
                "id": 3,
                "name": "Kitchenware",
                "description": "",
                "created_at": "2024-06-15 12:00:00",
                "updated_at": "2024-06-16 13:30:00"
            },
            {
                "id": 4,
                "name": "Gardening",
                "description": "",
                "created_at": "2024-07-25 14:00:00",
                "updated_at": "2024-07-26 15:45:00"
            },
            {
                "id": 5,
                "name": "Toys",
                "description": "",
                "created_at": "2024-08-05 16:00:00",
                "updated_at": "2024-08-06 17:30:00"
            },
            {
                "id": 6,
                "name": "Sports Equipment",
                "description": "",
                "created_at": "2024-09-10 18:00:00",
                "updated_at": "2024-09-11 19:00:00"
            }
        ]
    
    @staticmethod
    def test_data_item_lines():
        return [
            {
                "id": 1,
                "name": "Electronics",
                "description": "Devices and components including smartphones, laptops, and tablets.",
                "created_at": "2024-01-10 08:30:00",
                "updated_at": "2024-01-11 09:00:00"
            },
            {
                "id": 2,
                "name": "Furniture",
                "description": "Various types of furniture including chairs, tables, and sofas.",
                "created_at": "2024-02-20 10:00:00",
                "updated_at": "2024-02-21 11:20:00"
            },
            {
                "id": 3,
                "name": "Clothing",
                "description": "Apparel for men, women, and children including shirts, pants, and jackets.",
                "created_at": "2024-03-15 12:00:00",
                "updated_at": "2024-03-16 13:30:00"
            },
            {
                "id": 4,
                "name": "Toys",
                "description": "Toys and games for children of all ages.",
                "created_at": "2024-04-25 14:00:00",
                "updated_at": "2024-04-26 15:45:00"
            },
            {
                "id": 5,
                "name": "Sports Equipment",
                "description": "Equipment and gear for various sports including soccer, basketball, and tennis.",
                "created_at": "2024-05-05 16:00:00",
                "updated_at": "2024-05-06 17:30:00"
            },
            {
                "id": 6,
                "name": "Kitchenware",
                "description": "Utensils and appliances for kitchen use including pots, pans, and blenders.",
                "created_at": "2024-06-10 18:00:00",
                "updated_at": "2024-06-11 19:00:00"
            }
        ]
    
    @staticmethod
    def test_data_item_types():
        return [
            {
                "id": 1,
                "name": "Consumables",
                "description": "Items that are intended to be used up and replaced.",
                "created_at": "2024-01-15 08:30:00",
                "updated_at": "2024-01-16 09:00:00"
            },
            {
                "id": 2,
                "name": "Perishables",
                "description": "Items that have a limited shelf life and can spoil.",
                "created_at": "2024-02-20 10:00:00",
                "updated_at": "2024-02-21 11:20:00"
            },
            {
                "id": 3,
                "name": "Durables",
                "description": "Items that are intended to last for a long time.",
                "created_at": "2024-03-25 12:00:00",
                "updated_at": "2024-03-26 13:30:00"
            },
            {
                "id": 4,
                "name": "Luxury Goods",
                "description": "High-end items that are often considered non-essential.",
                "created_at": "2024-04-30 14:00:00",
                "updated_at": "2024-05-01 15:45:00"
            },
            {
                "id": 5,
                "name": "Industrial Supplies",
                "description": "Items used in manufacturing and industrial processes.",
                "created_at": "2024-06-05 16:00:00",
                "updated_at": "2024-06-06 17:30:00"
            },
            {
                "id": 6,
                "name": "Office Supplies",
                "description": "Items used in office settings, such as paper, pens, and staplers.",
                "created_at": "2024-07-10 18:00:00",
                "updated_at": "2024-07-11 19:00:00"
            }
        ]
    
    @staticmethod
    def test_data_items():
        return [
            {
                "uid": "P000002",
                "code": "nyg48736S",
                "description": "Focused transitional alliance",
                "short_description": "may",
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
            },
            {
                "uid": "P000003",
                "code": "abc12345",
                "description": "High-quality wireless earbuds",
                "short_description": "earbuds",
                "upc_code": "1234567890123",
                "model_number": "EB-2024",
                "commodity_code": "audio123",
                "item_line": 12,
                "item_group": 74,
                "item_type": 15,
                "unit_purchase_quantity": 20,
                "unit_order_quantity": 10,
                "pack_order_quantity": 5,
                "supplier_id": 35,
                "supplier_code": "SUP124",
                "supplier_part_number": "EB-2024-XYZ",
                "created_at": "2021-03-15 10:00:00",
                "updated_at": "2021-09-20 14:00:00"
            },
            {
                "uid": "P000004",
                "code": "xyz98765",
                "description": "Ergonomic office chair",
                "short_description": "chair",
                "upc_code": "9876543210987",
                "model_number": "OC-2024",
                "commodity_code": "furn123",
                "item_line": 13,
                "item_group": 75,
                "item_type": 16,
                "unit_purchase_quantity": 30,
                "unit_order_quantity": 20,
                "pack_order_quantity": 10,
                "supplier_id": 36,
                "supplier_code": "SUP125",
                "supplier_part_number": "OC-2024-ABC",
                "created_at": "2022-01-10 08:30:00",
                "updated_at": "2022-07-15 12:00:00"
            }
        ]
    
    @staticmethod
    def test_data_locations():
        return [
            {
                "id": 1,
                "warehouse_id": 1,
                "code": "A.1.0",
                "name": "Row: A, Rack: 1, Shelf: 0",
                "created_at": "1992-05-15 03:21:32",
                "updated_at": "1992-05-15 03:21:32"
            },
            {
                "id": 2,
                "warehouse_id": 2,
                "code": "B.2.1",
                "name": "Row: B, Rack: 2, Shelf: 1",
                "created_at": "2000-06-20 10:00:00",
                "updated_at": "2000-06-20 10:00:00"
            },
            {
                "id": 3,
                "warehouse_id": 3,
                "code": "C.3.2",
                "name": "Row: C, Rack: 3, Shelf: 2",
                "created_at": "2010-07-25 12:00:00",
                "updated_at": "2010-07-25 12:00:00"
            },
            {
                "id": 4,
                "warehouse_id": 4,
                "code": "D.4.3",
                "name": "Row: D, Rack: 4, Shelf: 3",
                "created_at": "2015-08-30 14:00:00",
                "updated_at": "2015-08-30 14:00:00"
            },
            {
                "id": 5,
                "warehouse_id": 5,
                "code": "E.5.4",
                "name": "Row: E, Rack: 5, Shelf: 4",
                "created_at": "2020-09-15 16:00:00",
                "updated_at": "2020-09-15 16:00:00"
            },
            {
                "id": 6,
                "warehouse_id": 6,
                "code": "F.6.5",
                "name": "Row: F, Rack: 6, Shelf: 5",
                "created_at": "2024-10-10 18:00:00",
                "updated_at": "2024-10-10 18:00:00"
            }
        ]
    
    @staticmethod
    def test_data_orders():
        return [
            {
                "id": 1,
                "source_id": 33,
                "order_date": "2019-04-03T11:33:15Z",
                "request_date": "2019-04-07T11:33:15Z",
                "reference": "ORD00001",
                "reference_extra": "Bedreven arm straffen bureau.",
                "order_status": "Delivered",
                "notes": "Voedsel vijf vork heel.",
                "shipping_notes": "Buurman betalen plaats bewolkt.",
                "picking_notes": "Ademen fijn volgorde scherp aardappel op leren.",
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
                    },
                    {
                        "item_id": "P009553",
                        "amount": 50
                    },
                    {
                        "item_id": "P010015",
                        "amount": 16
                    },
                    {
                        "item_id": "P002084",
                        "amount": 33
                    },
                    {
                        "item_id": "P009663",
                        "amount": 18
                    },
                    {
                        "item_id": "P010125",
                        "amount": 18
                    },
                    {
                        "item_id": "P005768",
                        "amount": 26
                    },
                    {
                        "item_id": "P004051",
                        "amount": 1
                    },
                    {
                        "item_id": "P005026",
                        "amount": 29
                    },
                    {
                        "item_id": "P000726",
                        "amount": 22
                    },
                    {
                        "item_id": "P008107",
                        "amount": 47
                    },
                    {
                        "item_id": "P001598",
                        "amount": 32
                    },
                    {
                        "item_id": "P002855",
                        "amount": 20
                    },
                    {
                        "item_id": "P010404",
                        "amount": 30
                    },
                    {
                        "item_id": "P010446",
                        "amount": 6
                    },
                    {
                        "item_id": "P001517",
                        "amount": 9
                    },
                    {
                        "item_id": "P009265",
                        "amount": 2
                    },
                    {
                        "item_id": "P001108",
                        "amount": 20
                    },
                    {
                        "item_id": "P009110",
                        "amount": 18
                    },
                    {
                        "item_id": "P009686",
                        "amount": 13
                    }
                ]
            },
            {
                "id": 2,
                "source_id": 34,
                "order_date": "2020-05-10T10:20:30Z",
                "request_date": "2020-05-15T10:20:30Z",
                "reference": "ORD00002",
                "reference_extra": "Extra reference for order 2.",
                "order_status": "Pending",
                "notes": "Order notes for order 2.",
                "shipping_notes": "Shipping notes for order 2.",
                "picking_notes": "Picking notes for order 2.",
                "warehouse_id": 19,
                "ship_to": None,
                "bill_to": None,
                "shipment_id": 2,
                "total_amount": 12000.00,
                "total_discount": 200.00,
                "total_tax": 500.00,
                "total_surcharge": 100.00,
                "created_at": "2020-05-10T10:20:30Z",
                "updated_at": "2020-05-12T10:20:30Z",
                "items": [
                    {
                        "item_id": "P007436",
                        "amount": 10
                    },
                    {
                        "item_id": "P009558",
                        "amount": 5
                    },
                    {
                        "item_id": "P009554",
                        "amount": 20
                    },
                    {
                        "item_id": "P010016",
                        "amount": 8
                    },
                    {
                        "item_id": "P002085",
                        "amount": 15
                    },
                    {
                        "item_id": "P009664",
                        "amount": 9
                    },
                    {
                        "item_id": "P010126",
                        "amount": 12
                    },
                    {
                        "item_id": "P005769",
                        "amount": 14
                    },
                    {
                        "item_id": "P004052",
                        "amount": 3
                    },
                    {
                        "item_id": "P005027",
                        "amount": 18
                    },
                    {
                        "item_id": "P000727",
                        "amount": 7
                    },
                    {
                        "item_id": "P008108",
                        "amount": 25
                    },
                    {
                        "item_id": "P001599",
                        "amount": 11
                    },
                    {
                        "item_id": "P002856",
                        "amount": 13
                    },
                    {
                        "item_id": "P010405",
                        "amount": 17
                    },
                    {
                        "item_id": "P010447",
                        "amount": 4
                    },
                    {
                        "item_id": "P001518",
                        "amount": 6
                    },
                    {
                        "item_id": "P009266",
                        "amount": 2
                    },
                    {
                        "item_id": "P001109",
                        "amount": 10
                    },
                    {
                        "item_id": "P009111",
                        "amount": 8
                    },
                    {
                        "item_id": "P009687",
                        "amount": 5
                    }
                ]
            }
        ]
    
    @staticmethod
    def test_data_shipments():
        return [
            {
                "id": 1,
                "order_id": 1,
                "source_id": 33,
                "order_date": "2000-03-09",
                "request_date": "2000-03-11",
                "shipment_date": "2000-03-13",
                "shipment_type": "I",
                "shipment_status": "Pending",
                "notes": "Zee vertrouwen klas rots heet lachen oneven begrijpen.",
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
                    },
                    {
                        "item_id": "P009553",
                        "amount": 50
                    },
                    {
                        "item_id": "P010015",
                        "amount": 16
                    },
                    {
                        "item_id": "P002084",
                        "amount": 33
                    },
                    {
                        "item_id": "P009663",
                        "amount": 18
                    },
                    {
                        "item_id": "P010125",
                        "amount": 18
                    },
                    {
                        "item_id": "P005768",
                        "amount": 26
                    },
                    {
                        "item_id": "P004051",
                        "amount": 1
                    },
                    {
                        "item_id": "P005026",
                        "amount": 29
                    },
                    {
                        "item_id": "P000726",
                        "amount": 22
                    },
                    {
                        "item_id": "P008107",
                        "amount": 47
                    },
                    {
                        "item_id": "P001598",
                        "amount": 32
                    },
                    {
                        "item_id": "P002855",
                        "amount": 20
                    },
                    {
                        "item_id": "P010404",
                        "amount": 30
                    },
                    {
                        "item_id": "P010446",
                        "amount": 6
                    },
                    {
                        "item_id": "P001517",
                        "amount": 9
                    },
                    {
                        "item_id": "P009265",
                        "amount": 2
                    },
                    {
                        "item_id": "P001108",
                        "amount": 20
                    },
                    {
                        "item_id": "P009110",
                        "amount": 18
                    },
                    {
                        "item_id": "P009686",
                        "amount": 13
                    }
                ]
            },
            {
                "id": 2,
                "order_id": 2,
                "source_id": 34,
                "order_date": "2021-05-10",
                "request_date": "2021-05-12",
                "shipment_date": "2021-05-14",
                "shipment_type": "O",
                "shipment_status": "Delivered",
                "notes": "Handle with care.",
                "carrier_code": "UPS",
                "carrier_description": "United Parcel Service",
                "service_code": "NextDay",
                "payment_type": "Automatic",
                "transfer_mode": "Air",
                "total_package_count": 20,
                "total_package_weight": 400.5,
                "created_at": "2021-05-10T12:00:00Z",
                "updated_at": "2021-05-11T14:00:00Z",
                "items": [
                    {
                        "item_id": "P007436",
                        "amount": 10
                    },
                    {
                        "item_id": "P009558",
                        "amount": 5
                    },
                    {
                        "item_id": "P009554",
                        "amount": 20
                    },
                    {
                        "item_id": "P010016",
                        "amount": 8
                    },
                    {
                        "item_id": "P002085",
                        "amount": 15
                    },
                    {
                        "item_id": "P009664",
                        "amount": 9
                    },
                    {
                        "item_id": "P010126",
                        "amount": 12
                    },
                    {
                        "item_id": "P005769",
                        "amount": 14
                    },
                    {
                        "item_id": "P004052",
                        "amount": 3
                    },
                    {
                        "item_id": "P005027",
                        "amount": 18
                    },
                    {
                        "item_id": "P000727",
                        "amount": 7
                    },
                    {
                        "item_id": "P008108",
                        "amount": 25
                    },
                    {
                        "item_id": "P001599",
                        "amount": 11
                    },
                    {
                        "item_id": "P002856",
                        "amount": 13
                    },
                    {
                        "item_id": "P010405",
                        "amount": 17
                    },
                    {
                        "item_id": "P010447",
                        "amount": 4
                    },
                    {
                        "item_id": "P001518",
                        "amount": 6
                    },
                    {
                        "item_id": "P009266",
                        "amount": 2
                    },
                    {
                        "item_id": "P001109",
                        "amount": 10
                    },
                    {
                        "item_id": "P009111",
                        "amount": 8
                    },
                    {
                        "item_id": "P009687",
                        "amount": 5
                    }
                ]
            }
        ]
    
    @staticmethod
    def test_data_suppliers():
        return [
            {
                "id": 1,
                "code": "SUP0001",
                "name": "Lee, Parks and Johnson",
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
            },
            {
                "id": 2,
                "code": "SUP0002",
                "name": "Industrial Components Co.",
                "address": "5678 Industrial Blvd",
                "address_extra": "Building B",
                "city": "Industropolis",
                "zip_code": "67890",
                "province": "IndustryState",
                "country": "Industland",
                "contact_name": "Jane Smith",
                "phonenumber": "+0987654321",
                "reference": "ICC3002Y",
                "created_at": "2024-02-10 10:30:00",
                "updated_at": "2024-02-15 11:45:00"
            },
            {
                "id": 3,
                "code": "SUP0003",
                "name": "Global Electronics",
                "address": "9101 Electronics Ave",
                "address_extra": "Floor 3",
                "city": "ElectroCity",
                "zip_code": "54321",
                "province": "ElectroState",
                "country": "Electroland",
                "contact_name": "Alice Brown",
                "phonenumber": "+1122334455",
                "reference": "GE3003Z",
                "created_at": "2024-03-20 12:00:00",
                "updated_at": "2024-03-25 13:15:00"
            },
            {
                "id": 4,
                "code": "SUP0004",
                "name": "Hardware Solutions",
                "address": "1213 Hardware St",
                "address_extra": "Unit 4",
                "city": "Hardwareville",
                "zip_code": "98765",
                "province": "HardwareState",
                "country": "Hardwareland",
                "contact_name": "Bob White",
                "phonenumber": "+5566778899",
                "reference": "HS3004W",
                "created_at": "2024-04-15 14:00:00",
                "updated_at": "2024-04-20 15:30:00"
            },
            {
                "id": 5,
                "code": "SUP0005",
                "name": "Office Essentials",
                "address": "1415 Office Park",
                "address_extra": "Building C",
                "city": "OfficeCity",
                "zip_code": "11223",
                "province": "OfficeState",
                "country": "Officeland",
                "contact_name": "Charlie Green",
                "phonenumber": "+6677889900",
                "reference": "OE3005V",
                "created_at": "2024-05-10 16:00:00",
                "updated_at": "2024-05-15 17:45:00"
            },
            {
                "id": 6,
                "code": "SUP0006",
                "name": "Construction Supplies Ltd.",
                "address": "1617 Construction Blvd",
                "address_extra": "Suite 200",
                "city": "ConstructCity",
                "zip_code": "33445",
                "province": "ConstructState",
                "country": "Constructland",
                "contact_name": "David Johnson",
                "phonenumber": "+9988776655",
                "reference": "CSL3006X",
                "created_at": "2024-06-20 18:00:00",
                "updated_at": "2024-06-25 19:30:00"
            }
        ]
    
    @staticmethod
    def test_data_transfers():
        return [
            {
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
            },
            {
                "id": 2,
                "reference": "TR00002",
                "transfer_from": 1234,
                "transfer_to": 5678,
                "transfer_status": "Pending",
                "created_at": "2021-05-10T10:20:30Z",
                "updated_at": "2021-05-11T12:30:45Z",
                "items": [
                    {
                        "item_id": "P009558",
                        "amount": 5
                    },
                    {
                        "item_id": "P010016",
                        "amount": 8
                    }
                ]
            },
            {
                "id": 3,
                "reference": "TR00003",
                "transfer_from": 4321,
                "transfer_to": 8765,
                "transfer_status": "In Progress",
                "created_at": "2022-07-15T14:00:00Z",
                "updated_at": "2022-07-16T16:00:00Z",
                "items": [
                    {
                        "item_id": "P002085",
                        "amount": 15
                    },
                    {
                        "item_id": "P009664",
                        "amount": 9
                    }
                ]
            }
        ]
    
    @staticmethod
    def test_data_warehouses():
        return [
            {
                "id": 1,
                "code": "YQZZNL56",
                "name": "Heemskerk cargo hub",
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
            },
            {
                "id": 2,
                "code": "ABCD1234",
                "name": "Amsterdam distribution center",
                "address": "Damrak 1-5",
                "zip": "1012 LG",
                "city": "Amsterdam",
                "province": "Noord-Holland",
                "country": "NL",
                "contact": {
                    "name": "Jan de Vries",
                    "phone": "(020) 1234567",
                    "email": "jan@example.com"
                },
                "created_at": "1990-05-15 10:00:00",
                "updated_at": "2010-06-20 15:30:00"
            },
            {
                "id": 3,
                "code": "EFGH5678",
                "name": "Rotterdam storage facility",
                "address": "Waalhaven Z.z. 12",
                "zip": "3088 HH",
                "city": "Rotterdam",
                "province": "Zuid-Holland",
                "country": "NL",
                "contact": {
                    "name": "Piet Jansen",
                    "phone": "(010) 7654321",
                    "email": "piet@example.com"
                },
                "created_at": "2000-07-20 08:45:00",
                "updated_at": "2015-09-25 12:00:00"
            }
        ]

from Warehousing.code.api.models.base import Base

class Warehouses(Base):
    def __init__(self, root_path, is_debug=False, debug_data=None):
        super().__init__(root_path, "warehouses.json", is_debug, debug_data)

    # Add methods for Warehouses class as needed
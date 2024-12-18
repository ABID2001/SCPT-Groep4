import unittest
from datetime import datetime, timezone
from Warehousing.code.api.models.base import Base

class BaseTestClass(Base):
    def __init__(self, data):
        super().__init__(root_path="", file_name="", is_debug=True, debug_data=data)
        self.data = data
        #de testclasses geven de testdata mee om te self.data in base te vullen

    def get_timestamp(self):
        return datetime.now(timezone.utc).isoformat(timespec='seconds') + "Z"
    
    def save(self):
        #override de normale save methode zodat er niks wordt opgeslagen
        pass
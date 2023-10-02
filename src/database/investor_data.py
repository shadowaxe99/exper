```python
from pymongo import MongoClient
from src.models.investor import InvestorSchema

class InvestorData:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['elysium']
        self.collection = self.db['investors']

    def get_investor(self, investor_id):
        investor_data = self.collection.find_one({"_id": investor_id})
        if investor_data:
            return InvestorSchema().load(investor_data)
        return None

    def save_investor(self, investor):
        investor_data = InvestorSchema().dump(investor)
        result = self.collection.insert_one(investor_data)
        return result.inserted_id

    def update_investor(self, investor_id, investor):
        investor_data = InvestorSchema().dump(investor)
        self.collection.update_one({"_id": investor_id}, {"$set": investor_data})

    def delete_investor(self, investor_id):
        self.collection.delete_one({"_id": investor_id})
```
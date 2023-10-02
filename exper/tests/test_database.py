```python
import unittest
from src.database.db import Database
from src.models.investor import Investor

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = Database()
        self.investor = Investor("Elon Musk", "elon@tesla.com", "Tesla, SpaceX", "Technology")

    def test_add_investor(self):
        self.db.add_investor(self.investor)
        self.assertIn(self.investor, self.db.investors)

    def test_remove_investor(self):
        self.db.add_investor(self.investor)
        self.db.remove_investor(self.investor)
        self.assertNotIn(self.investor, self.db.investors)

    def test_get_investor(self):
        self.db.add_investor(self.investor)
        retrieved_investor = self.db.get_investor("elon@tesla.com")
        self.assertEqual(retrieved_investor, self.investor)

    def test_update_investor(self):
        self.db.add_investor(self.investor)
        updated_investor = Investor("Elon Musk", "elon@tesla.com", "Tesla, SpaceX, Neuralink", "Technology")
        self.db.update_investor(updated_investor)
        retrieved_investor = self.db.get_investor("elon@tesla.com")
        self.assertEqual(retrieved_investor.interests, "Tesla, SpaceX, Neuralink")

if __name__ == '__main__':
    unittest.main()
```
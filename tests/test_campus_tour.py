```python
import unittest
from src.campus_tour import startCampusTour
from src.models.investor import Investor

class TestCampusTour(unittest.TestCase):

    def setUp(self):
        self.investor = Investor("Elon Musk", "Tesla, SpaceX", "elon@tesla.com", "AI, Space Exploration")

    def test_startCampusTour(self):
        response = startCampusTour(self.investor)
        self.assertEqual(response['status'], 'success')
        self.assertTrue('tourDetails' in response)
        self.assertTrue('visitedLocations' in response['tourDetails'])
        self.assertTrue('interactions' in response['tourDetails'])
        self.assertTrue('easterEggsFound' in response['tourDetails'])

if __name__ == '__main__':
    unittest.main()
```
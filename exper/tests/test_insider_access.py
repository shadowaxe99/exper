```python
import unittest
from src.models.insider_access import InsiderAccess

class TestInsiderAccess(unittest.TestCase):

    def setUp(self):
        self.insider_access = InsiderAccess()

    def test_provide_insider_access(self):
        self.insider_access.provide_insider_access()
        self.assertTrue(self.insider_access.insider_access_provided)

    def test_fine_dining(self):
        self.insider_access.fine_dining()
        self.assertTrue(self.insider_access.dining_done)

    def test_undisclosed_projects(self):
        projects = self.insider_access.undisclosed_projects()
        self.assertIsNotNone(projects)

    def test_company_roadmap(self):
        roadmap = self.insider_access.company_roadmap()
        self.assertIsNotNone(roadmap)

    def test_possibilities_of_Elysium_OS(self):
        possibilities = self.insider_access.possibilities_of_Elysium_OS()
        self.assertIsNotNone(possibilities)

    def test_welcome_investor(self):
        self.insider_access.welcome_investor()
        self.assertTrue(self.insider_access.investor_welcomed)

if __name__ == '__main__':
    unittest.main()
```
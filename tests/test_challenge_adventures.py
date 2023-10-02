```python
import unittest
from src.challenge_adventures import startChallengeAdventures
from src.models.adventure import Adventure

class TestChallengeAdventures(unittest.TestCase):

    def setUp(self):
        self.adventureSettings = {
            "maze": {
                "difficulty": "hard",
                "reward": "Elysium Diamond Token"
            },
            "ai_debate": {
                "topic": "Future of AI",
                "reward": "Elysium Platinum Token"
            }
        }
        self.investorProfile = {
            "name": "John Doe",
            "interests": ["AI", "Blockchain", "VR"],
            "background": "Tech Entrepreneur"
        }

    def test_startChallengeAdventures(self):
        adventure = startChallengeAdventures(self.adventureSettings, self.investorProfile)
        self.assertIsInstance(adventure, Adventure)
        self.assertEqual(adventure.investor, self.investorProfile["name"])
        self.assertIn(adventure.reward, ["Elysium Diamond Token", "Elysium Platinum Token"])

if __name__ == '__main__':
    unittest.main()
```
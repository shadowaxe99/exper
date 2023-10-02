```python
import unittest
from src.models.reward import Reward
from src.rewards import giveRewards

class TestRewards(unittest.TestCase):

    def setUp(self):
        self.reward = Reward("Elysium Smart Ring", "Branded smart ring with Elysium OS integration", "Tech")
        self.investorProfile = {
            "name": "John Doe",
            "interests": ["Tech", "Art"],
            "net_worth": 1000000000
        }

    def test_reward_creation(self):
        self.assertEqual(self.reward.name, "Elysium Smart Ring")
        self.assertEqual(self.reward.description, "Branded smart ring with Elysium OS integration")
        self.assertEqual(self.reward.category, "Tech")

    def test_give_rewards(self):
        rewards = giveRewards(self.investorProfile)
        self.assertTrue(any(reward.category in self.investorProfile["interests"] for reward in rewards))

if __name__ == '__main__':
    unittest.main()
```
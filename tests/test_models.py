```python
import unittest
from src.models.investor import Investor
from src.models.experience import Experience
from src.models.reward import Reward
from src.models.adventure import Adventure
from src.models.assistant import Assistant
from src.models.invitation import Invitation
from src.models.onboarding import Onboarding
from src.models.real_world_integration import RealWorldIntegration
from src.models.insider_access import InsiderAccess

class TestModels(unittest.TestCase):

    def setUp(self):
        self.investor = Investor("John Doe", "Tech", "Art")
        self.experience = Experience("VR Journey", "Elysium OS")
        self.reward = Reward("Smart Ring", "Elysium OS")
        self.adventure = Adventure("Decentralized Maze", "AI debates")
        self.assistant = Assistant("AI Assistant", "ML model")
        self.invitation = Invitation("Cryptex Box", "Access Keys")
        self.onboarding = Onboarding("Save the Date", "Cryptex Invitation")
        self.real_world_integration = RealWorldIntegration("Biometrics", "IoT Integration")
        self.insider_access = InsiderAccess("Fine Dining", "Undisclosed Projects")

    def test_investor(self):
        self.assertEqual(self.investor.name, "John Doe")
        self.assertEqual(self.investor.industry, "Tech")
        self.assertEqual(self.investor.interest, "Art")

    def test_experience(self):
        self.assertEqual(self.experience.name, "VR Journey")
        self.assertEqual(self.experience.platform, "Elysium OS")

    def test_reward(self):
        self.assertEqual(self.reward.name, "Smart Ring")
        self.assertEqual(self.reward.brand, "Elysium OS")

    def test_adventure(self):
        self.assertEqual(self.adventure.name, "Decentralized Maze")
        self.assertEqual(self.adventure.theme, "AI debates")

    def test_assistant(self):
        self.assertEqual(self.assistant.name, "AI Assistant")
        self.assertEqual(self.assistant.powered_by, "ML model")

    def test_invitation(self):
        self.assertEqual(self.invitation.type, "Cryptex Box")
        self.assertEqual(self.invitation.contents, "Access Keys")

    def test_onboarding(self):
        self.assertEqual(self.onboarding.message, "Save the Date")
        self.assertEqual(self.onboarding.invitation, "Cryptex Invitation")

    def test_real_world_integration(self):
        self.assertEqual(self.real_world_integration.type, "Biometrics")
        self.assertEqual(self.real_world_integration.integration, "IoT Integration")

    def test_insider_access(self):
        self.assertEqual(self.insider_access.activity, "Fine Dining")
        self.assertEqual(self.insider_access.insights, "Undisclosed Projects")

if __name__ == '__main__':
    unittest.main()
```
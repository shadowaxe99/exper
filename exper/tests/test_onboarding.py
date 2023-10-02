```python
import unittest
from src.onboarding import startOnboarding, createInvestorProfile

class TestOnboarding(unittest.TestCase):

    def setUp(self):
        self.investorProfile = {
            "name": "John Doe",
            "interests": ["AI", "Blockchain", "VR"],
            "background": "Tech Entrepreneur",
            "preferences": {
                "food": "Italian",
                "music": "Classical",
                "art": "Modern"
            }
        }

    def test_create_investor_profile(self):
        profile = createInvestorProfile(self.investorProfile)
        self.assertEqual(profile, self.investorProfile)

    def test_start_onboarding(self):
        onboardingDetails = startOnboarding(self.investorProfile)
        self.assertEqual(onboardingDetails['status'], 'ONBOARDING_COMPLETE')
        self.assertEqual(onboardingDetails['investorProfile'], self.investorProfile)

if __name__ == '__main__':
    unittest.main()
```
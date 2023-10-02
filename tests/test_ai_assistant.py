```python
import unittest
from src.ai_assistant import createAIAssistant
from src.models.assistant import AssistantSchema

class TestAIAssistant(unittest.TestCase):

    def setUp(self):
        self.investorProfile = {
            "name": "John Doe",
            "interests": ["AI", "Blockchain", "VR"],
            "industry": "Technology",
            "net_worth": 1000000000
        }
        self.assistantSettings = {
            "personality": "friendly",
            "knowledge_base": ["AI", "Blockchain", "VR"],
            "language": "English"
        }

    def test_create_ai_assistant(self):
        assistant = createAIAssistant(self.investorProfile, self.assistantSettings)
        self.assertIsInstance(assistant, AssistantSchema)

        # Check if the assistant is personalized for the investor
        self.assertEqual(assistant.name, self.investorProfile["name"])
        self.assertEqual(assistant.interests, self.investorProfile["interests"])
        self.assertEqual(assistant.industry, self.investorProfile["industry"])

        # Check if the assistant settings are correctly applied
        self.assertEqual(assistant.personality, self.assistantSettings["personality"])
        self.assertEqual(assistant.knowledge_base, self.assistantSettings["knowledge_base"])
        self.assertEqual(assistant.language, self.assistantSettings["language"])

if __name__ == '__main__':
    unittest.main()
```
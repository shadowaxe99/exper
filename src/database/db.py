```python
from pymongo import MongoClient
from src.models.investor import InvestorSchema
from src.models.experience import ExperienceSchema
from src.models.reward import RewardSchema
from src.models.adventure import AdventureSchema
from src.models.assistant import AssistantSchema
from src.models.invitation import InvitationSchema
from src.models.onboarding import OnboardingSchema
from src.models.real_world_integration import RealWorldIntegrationSchema
from src.models.insider_access import InsiderAccessSchema

class Database:
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client['elysium_os']

    def save_investor_data(self, investor_data):
        investor = self.db['investors']
        investor.insert_one(InvestorSchema().dump(investor_data))

    def save_experience_data(self, experience_data):
        experience = self.db['experiences']
        experience.insert_one(ExperienceSchema().dump(experience_data))

    def save_reward_data(self, reward_data):
        reward = self.db['rewards']
        reward.insert_one(RewardSchema().dump(reward_data))

    def save_adventure_data(self, adventure_data):
        adventure = self.db['adventures']
        adventure.insert_one(AdventureSchema().dump(adventure_data))

    def save_assistant_data(self, assistant_data):
        assistant = self.db['assistants']
        assistant.insert_one(AssistantSchema().dump(assistant_data))

    def save_invitation_data(self, invitation_data):
        invitation = self.db['invitations']
        invitation.insert_one(InvitationSchema().dump(invitation_data))

    def save_onboarding_data(self, onboarding_data):
        onboarding = self.db['onboarding']
        onboarding.insert_one(OnboardingSchema().dump(onboarding_data))

    def save_real_world_integration_data(self, real_world_integration_data):
        real_world_integration = self.db['real_world_integrations']
        real_world_integration.insert_one(RealWorldIntegrationSchema().dump(real_world_integration_data))

    def save_insider_access_data(self, insider_access_data):
        insider_access = self.db['insider_access']
        insider_access.insert_one(InsiderAccessSchema().dump(insider_access_data))
```
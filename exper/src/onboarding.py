```python
from src.models.onboarding import OnboardingSchema
from src.database.investor_data import get_investor_data
from src.utils import send_message

def start_onboarding(investor_id):
    investor_data = get_investor_data(investor_id)
    onboarding_details = OnboardingSchema().load(investor_data)

    send_message("SAVE_THE_DATE", investor_id)
    send_cryptex_invitation(investor_id, onboarding_details)
    concierge_outreach(investor_id, onboarding_details)
    customize_interactive_elements(investor_id, onboarding_details)

    send_message("ONBOARDING_COMPLETE", investor_id)

def send_cryptex_invitation(investor_id, onboarding_details):
    # Code to send cryptex invitation goes here
    pass

def concierge_outreach(investor_id, onboarding_details):
    # Code to conduct concierge outreach goes here
    pass

def customize_interactive_elements(investor_id, onboarding_details):
    # Code to customize interactive elements based on investor interests goes here
    pass
```
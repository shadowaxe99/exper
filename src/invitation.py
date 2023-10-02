```python
from src.models.invitation import InvitationSchema
from src.constants import INVITATION_SENT

class Invitation:
    def __init__(self, investor):
        self.investor = investor
        self.invitation_details = None

    def create_invitation(self):
        self.invitation_details = InvitationSchema(
            cryptex_box=True,
            vr_headset=True,
            access_keys=True,
            introduction_hologram=True
        )

    def send_invitation(self):
        if self.invitation_details:
            # Code to send the invitation goes here
            print(INVITATION_SENT.format(self.investor.name))
        else:
            print("Invitation not created yet.")

    def check_invitation_status(self):
        if self.invitation_details:
            return True
        else:
            return False
```
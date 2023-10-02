```python
import unittest
from src.invitation import sendInvitation
from src.models.invitation import InvitationSchema

class TestInvitation(unittest.TestCase):

    def setUp(self):
        self.invitation_details = {
            "cryptex_box": True,
            "vr_headset": True,
            "access_keys": True,
            "introduction_hologram": True,
            "premium_packaging": True
        }

    def test_send_invitation(self):
        result = sendInvitation(self.invitation_details)
        self.assertEqual(result, "INVITATION_SENT")

    def test_invitation_schema(self):
        schema = InvitationSchema()
        data = schema.load(self.invitation_details)
        self.assertEqual(data, self.invitation_details)

if __name__ == '__main__':
    unittest.main()
```
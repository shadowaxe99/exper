```python
from mongoengine import Document, StringField, ListField

class Onboarding(Document):
    cryptic_message = StringField(required=True)
    cryptex_invitation = StringField(required=True)
    concierge_outreach = StringField(required=True)
    customization_elements = ListField(StringField(), required=True)

    def __str__(self):
        return f"Onboarding(cryptic_message={self.cryptic_message}, cryptex_invitation={self.cryptex_invitation}, concierge_outreach={self.concierge_outreach}, customization_elements={self.customization_elements})"
```
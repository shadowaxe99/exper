```python
from mongoengine import Document, StringField, ListField, DictField

class Experience(Document):
    investor_id = StringField(required=True)
    experience_settings = DictField(required=True)
    personalized_elements = ListField(StringField(), required=True)
    campus_tour_details = DictField(required=True)
    challenge_adventures = ListField(DictField(), required=True)
    real_world_integrations = ListField(DictField(), required=True)
    luxury_rewards = ListField(DictField(), required=True)
    insider_access = DictField(required=True)

    meta = {
        'indexes': [
            'investor_id'
        ]
    }
```
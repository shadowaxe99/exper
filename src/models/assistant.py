```python
from mongoengine import Document, StringField, IntField, BooleanField

class AssistantSchema(Document):
    name = StringField(required=True, max_length=200)
    personality = StringField(required=True, max_length=200)
    expertise = StringField(required=True, max_length=200)
    trained_model = StringField(required=True, max_length=200)
    conversational_ability = BooleanField(default=False)
    rapport_building = BooleanField(default=False)

    meta = {
        'collection': 'assistant',
        'indexes': ['name']
    }

    def __str__(self):
        return self.name
```
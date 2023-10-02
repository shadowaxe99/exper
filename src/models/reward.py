```python
from mongoengine import Document, StringField, ListField

class Reward(Document):
    meta = {'collection': 'rewardItems'}
    name = StringField(required=True)
    description = StringField(required=True)
    type = StringField(required=True)
    materials = ListField(StringField(), required=True)
    exclusive = StringField(required=True)

    def to_json(self):
        return {
            "name": self.name,
            "description": self.description,
            "type": self.type,
            "materials": self.materials,
            "exclusive": self.exclusive
        }
```
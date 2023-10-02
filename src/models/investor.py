```python
from mongoengine import Document, StringField, ListField, DictField

class Investor(Document):
    name = StringField(required=True)
    net_worth = StringField(required=True)
    interests = ListField(StringField(), required=True)
    background = StringField(required=True)
    preferences = DictField(required=True)
    industry = StringField(required=True)
    status = StringField(required=True)

    def __str__(self):
        return self.name
```
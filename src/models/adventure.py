```python
from mongoengine import Document, StringField, ListField

class Adventure(Document):
    """
    Model representing an interactive challenge adventure in the Elysium OS Investor Experience.
    """
    title = StringField(required=True)
    description = StringField(required=True)
    challenges = ListField(StringField(), required=True)
    easter_eggs = ListField(StringField())
    path_choices = ListField(StringField(), required=True)

    def __str__(self):
        return self.title
```
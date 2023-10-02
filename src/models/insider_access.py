```python
from mongoengine import Document, StringField, ListField

class InsiderAccess(Document):
    dining_with_leadership = StringField(required=True)
    undisclosed_projects = ListField(StringField(), required=True)
    company_roadmap = StringField(required=True)
    possibilities_of_Elysium_OS = StringField(required=True)
    investor_status = StringField(required=True)

    def to_json(self):
        return {
            "dining_with_leadership": self.dining_with_leadership,
            "undisclosed_projects": self.undisclosed_projects,
            "company_roadmap": self.company_roadmap,
            "possibilities_of_Elysium_OS": self.possibilities_of_Elysium_OS,
            "investor_status": self.investor_status
        }
```
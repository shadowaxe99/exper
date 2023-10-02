```python
from mongoengine import Document, StringField

class Invitation(Document):
    cryptex_box = StringField(required=True)
    vr_headset = StringField(required=True)
    access_keys = StringField(required=True)
    introduction_hologram = StringField(required=True)
    packaging = StringField(required=True)

    def __str__(self):
        return f"Cryptex Box: {self.cryptex_box}, VR Headset: {self.vr_headset}, Access Keys: {self.access_keys}, Introduction Hologram: {self.introduction_hologram}, Packaging: {self.packaging}"
```
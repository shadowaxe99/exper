```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from src.models.investor import InvestorSchema

class AIModel:
    def __init__(self, investor_profile: InvestorSchema):
        self.investor_profile = investor_profile
        self.model = self.build_model()

    def build_model(self):
        model = keras.Sequential()
        model.add(layers.Dense(64, activation='relu', input_shape=(len(self.investor_profile),)))
        model.add(layers.Dense(64, activation='relu'))
        model.add(layers.Dense(1))
        model.compile(optimizer='adam', loss='mse', metrics=['mae', 'mse'])
        return model

    def train_model(self, data, labels, epochs=10):
        self.model.fit(data, labels, epochs=epochs)

    def predict(self, input_data):
        return self.model.predict(input_data)

def create_ai_model(investor_profile: InvestorSchema):
    ai_model = AIModel(investor_profile)
    return ai_model
```
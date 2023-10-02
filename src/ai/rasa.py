```python
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.utils.endpoints import ClientResponseError, EndpointConfig

from src.models.assistant import AssistantSchema
from src.database.investor_data import get_investor_profile

# Load trained model
interpreter = RasaNLUInterpreter('models/nlu/default/investorassistant')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('models/dialogue', interpreter=interpreter, action_endpoint=action_endpoint)

def create_assistant(investor_id):
    investor_profile = get_investor_profile(investor_id)
    assistant_settings = AssistantSchema().load(investor_profile)
    
    return assistant_settings

def handle_message(investor_id, message):
    assistant = create_assistant(investor_id)
    responses = agent.handle_text(message)
    
    for response in responses:
        assistant.send_message(response["text"])
        
    return responses

def train_assistant(investor_id):
    assistant = create_assistant(investor_id)
    training_data = assistant.get_training_data()
    
    agent.train(training_data)
    
    return agent
```
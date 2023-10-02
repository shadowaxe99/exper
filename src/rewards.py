```python
from src.models.reward import RewardSchema
from src.database.db import db_session

rewardItems = []

class Reward:
    def __init__(self, name, description, type, material, design):
        self.name = name
        self.description = description
        self.type = type
        self.material = material
        self.design = design

    def create_reward(self):
        new_reward = RewardSchema(name=self.name, description=self.description, type=self.type, material=self.material, design=self.design)
        db_session.add(new_reward)
        db_session.commit()

    def get_rewards(self):
        rewards = RewardSchema.query.all()
        for reward in rewards:
            rewardItems.append({
                "name": reward.name,
                "description": reward.description,
                "type": reward.type,
                "material": reward.material,
                "design": reward.design
            })
        return rewardItems

def giveRewards(investor):
    reward = Reward("Elysium Smart Ring", "A smart ring with integrated Elysium OS", "Tech", "Gold", "Intricate")
    reward.create_reward()
    investor.rewards.append(reward)
    return investor
```
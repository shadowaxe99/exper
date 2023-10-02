```python
import omniverse as ov

class OmniverseVR:
    def __init__(self, investor_profile, experience_settings):
        self.investor_profile = investor_profile
        self.experience_settings = experience_settings
        self.simulation = None

    def create_simulation(self):
        self.simulation = ov.create_simulation(self.investor_profile, self.experience_settings)

    def start_simulation(self):
        if self.simulation is not None:
            self.simulation.start()

    def stop_simulation(self):
        if self.simulation is not None:
            self.simulation.stop()

    def update_simulation_settings(self, new_settings):
        self.experience_settings = new_settings
        self.simulation.update_settings(new_settings)

    def get_simulation_status(self):
        if self.simulation is not None:
            return self.simulation.get_status()
        else:
            return "Simulation not created yet."

def create_vr_experience(investor_profile, experience_settings):
    vr = OmniverseVR(investor_profile, experience_settings)
    vr.create_simulation()
    return vr
```
```python
import unityengine as unity

class UnityVR:
    def __init__(self, investor_profile, experience_settings):
        self.investor_profile = investor_profile
        self.experience_settings = experience_settings
        self.vr_environment = unity.GameObject("VR Environment")

    def create_vr_environment(self):
        self.vr_environment.AddComponent(unity.Camera)
        self.vr_environment.AddComponent(unity.AudioListener)

    def customize_vr_environment(self):
        self.vr_environment.transform.position = unity.Vector3(0, 0, 0)
        self.vr_environment.transform.rotation = unity.Quaternion.identity

        if self.investor_profile['preferences']['lighting']:
            light = self.vr_environment.AddComponent(unity.Light)
            light.type = unity.LightType.Sun

        if self.investor_profile['preferences']['sound']:
            audio_source = self.vr_environment.AddComponent(unity.AudioSource)
            audio_source.clip = unity.Resources.Load("Sounds/Background")

    def start_vr_experience(self):
        self.create_vr_environment()
        self.customize_vr_environment()

        unity.Application.LoadLevel("VR Experience")

    def end_vr_experience(self):
        unity.Application.Quit()
```
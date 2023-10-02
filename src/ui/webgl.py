```python
import webgl

class WebGLRenderer:
    def __init__(self):
        self.renderer = webgl.WebGLRenderer()

    def create_scene(self):
        self.scene = webgl.Scene()

    def create_camera(self):
        self.camera = webgl.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000)

    def create_light(self):
        self.light = webgl.AmbientLight(0x404040)
        self.scene.add(self.light)

    def create_object(self, object_data):
        geometry = webgl.BoxGeometry(object_data['width'], object_data['height'], object_data['depth'])
        material = webgl.MeshBasicMaterial({color: object_data['color']})
        cube = webgl.Mesh(geometry, material)
        self.scene.add(cube)

    def render_scene(self):
        self.renderer.render(self.scene, self.camera)

    def animate(self):
        requestAnimationFrame(self.animate)
        self.render_scene()

    def start(self):
        self.create_scene()
        self.create_camera()
        self.create_light()
        self.animate()

def create_experience(experience_settings):
    renderer = WebGLRenderer()
    for object_data in experience_settings['objects']:
        renderer.create_object(object_data)
    renderer.start()
```
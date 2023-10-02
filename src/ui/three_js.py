```python
import three

def create_3D_environment():
    scene = three.Scene()
    camera = three.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000)
    renderer = three.WebGLRenderer()
    renderer.setSize(window.innerWidth, window.innerHeight)
    document.body.appendChild(renderer.domElement)
    return scene, camera, renderer

def add_lighting(scene):
    ambient_light = three.AmbientLight(0x404040)
    scene.add(ambient_light)
    directional_light = three.DirectionalLight(0xffffff)
    directional_light.position.set(1, 1, 1).normalize()
    scene.add(directional_light)

def create_3D_model(scene, model_path):
    loader = three.GLTFLoader()
    loader.load(model_path, function (gltf) {
        scene.add(gltf.scene)
    }, undefined, function (error) {
        console.error(error)
    })

def animate(renderer, scene, camera):
    def render():
        renderer.render(scene, camera)
    animate_id = requestAnimationFrame(render)

def stop_animation(animate_id):
    cancelAnimationFrame(animate_id)

def create_VR_experience(model_path):
    scene, camera, renderer = create_3D_environment()
    add_lighting(scene)
    create_3D_model(scene, model_path)
    animate_id = animate(renderer, scene, camera)
    return animate_id

def end_VR_experience(animate_id):
    stop_animation(animate_id)
```

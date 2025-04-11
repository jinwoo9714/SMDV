from ursina import *
import random

app = Ursina()

# Sol de la ville
grass = Entity(
    model='plane',
    scale=(100, 1, 100),
    texture='grass',
    texture_scale=(50, 50),
    collider='box'
)
grass.y = -0.5  # Le plan est ainsi positionné de sorte que y=0 corresponde à la surface du sol.

# Charger des textures rétro
textures = ["brick", "wood", "metal", "concrete"]


# Générer des maisons variées
def create_house(x, z):
    height = random.uniform(2, 3)
    house = Entity(
        model='cube',
        scale=(random.uniform(2, 3), height, random.uniform(2, 3)),
        position=(x, height / 2, z),
        texture=random.choice(textures),
        color=color.random_color(),
        collider='box'
    )
    return house

# Route centrale
road_width = 10
road = Entity(
    model='plane',
    scale=(100, 1, road_width),
    color=color.dark_gray,
    collider='box'
)
road.position = (0, -0.49, 0)


# Placer plusieurs maisons
for i in range(-10, 10, 8):
    for j in range(-10, 10, 8):
        create_house(i, j)

# Éclairage rétro
light = PointLight(position=(0, 10, 0), color=color.white)
EditorCamera(position=(0, 2, -10))  # Caméra positionnée à 2 unités au-dessus du sol


app.run()

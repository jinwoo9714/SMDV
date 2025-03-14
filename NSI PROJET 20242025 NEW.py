from ursina import *
import random

app = Ursina()

# Charger des textures rétro
textures = ["brick", "wood", "metal", "concrete"]

# Sol de la ville
Entity(model='plane', scale=(50, 1, 50), texture='grass', collider='box')

# Générer des maisons variées
def create_house(x, z):
    height = random.uniform(2, 4)
    house = Entity(
        model='cube',
        scale=(random.uniform(2, 3), height, random.uniform(2, 3)),
        position=(x, height / 2, z),
        texture=random.choice(textures),
        color=color.random_color(),
        collider='box'
    )
    return house

# Placer plusieurs maisons
for i in range(-10, 10, 4):
    for j in range(-10, 10, 4):
        create_house(i, j)

# Éclairage rétro
light = PointLight(position=(0, 10, 0), color=color.orange)
EditorCamera(position=(0, 2, -10))  # Caméra positionnée à 2 unités au-dessus du sol


app.run()
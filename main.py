# Importation des bibliothèques
from ursina import * 
from pygame import *
from time import * 

# créer une fenêtre
app = Ursina()

# La plupart des choses dans Ursina sont des entités. EntitéC'est une chose que vous placez dans le monde.
# Vous pouvez les considérer comme des GameObjects dans Unity ou des Actors dans Unreal.
# Le premier paramètre nous indique l'Entité Le modèle sera un modèle d'appelé 'cube'.
# Ursina inclut quelques modèles de base comment 'cube','sphère' et 'quadruple'.

# le paramètre suivant nous indique que la couleur du modèle doit être orange.

#'Échelle_et=2'nous indique quelle doit être la taille de l'entité sur l'axe vertical, quelle doit être sa hauteur.
# Dans Ursina, x positif est à droite, y positif est en haut et z positif est en avant.
player = Entity(model='cube', scale_y=2)

# Créer une fonction appelée 'mise à jour'.
# Ceci sera automatiquement appelé par le moteur à chaque image.


def update():
    player.x += held_keys['d']
    player.x -= held_keys['a']

# Cette partie fera bouger le joueur vers la gauche ou la droite en fonction de nos entrées.
# Pour vérifier quelles touches sont maintenues enfoncées, nous pouvons consulter le dictionnaire held_keys.
#0ImpressPages et signifie pressé.
# Time.dt est simplement le temps écoulé depuis la dernière image. En multipliant par cela, le
# joueur se déplacera à la même vitesse quelle que soit la vitesse à laquelle le jeu se déroule.


def input(key):
    if key == 'space':
        player.y += 1
        invoke(setattr, player, 'y', player.y-1, delay=.25)


# commencer à exécuter le jeu
app.run()

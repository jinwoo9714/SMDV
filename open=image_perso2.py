import pygame
import tkinter as tk

# Initialiser Pygame
pygame.init()

# Définir la taille de la fenêtre
window_width = 1500
window_height = 1000
screen = pygame.display.set_mode((window_width, window_height))


# Charger l'image
image = pygame.image.load("aveugle.png")

# Obtenir les dimensions de l'image
image_width = 0
image_height =0 

# Position de l'image en bas à droite
x_pos = window_width - image_width - 10  # Décalage de 10 pixels depuis le bord droit
y_pos = window_height - image_height - 10  # Décalage de 10 pixels depuis le bas

# Définir la couleur de fond (par exemple, noir)
screen.fill((0, 0, 0))

# Afficher l'image à la position spécifiée
screen.blit(image, (800,200 ))

# Rafraîchir l'écran
pygame.display.update()

# Boucle pour garder la fenêtre ouverte
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quitter Pygame
pygame.quit()



import pygame
import sys


# Initialisation de Pygame
pygame.init()


# Paramètres de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Énigme du Prisme")

# Chargement de l'image du prisme
prisme_image = pygame.image.load("prisme1.2.jpg")
prisme_image = pygame.transform.scale(prisme_image, (100, 100))  # Ajuste la taille

# Position initiale du prisme
prisme_x, prisme_y = 350, 250  
vitesse = 5  # Vitesse de déplacement

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (100, 100, 100)

# Variables de jeu
prisme_angle = 0  # Angle du prisme
lumiere_couleur = WHITE  # Couleur de la lumière projetée
font = pygame.font.Font(None, 28)
dialogues = [
    "Elias : Cet atelier est plongé dans l'obscurité...",
    "Maître Léo : Regarde ce prisme. Il peut révéler des couleurs cachées.",
    "Elias : Comment puis-je l’utiliser ?",
    "Maître Léo : Oriente-le correctement et observe ce qui se passe.",
    "Elias (pensif) : Peut-être que je dois viser un certain angle..."
]
dialogue_index = 0
    

# Boucle de jeu
running = True
while running:
    screen.fill((0,0,0))

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                prisme_angle += 5
            elif event.key == pygame.K_LEFT:
                prisme_angle -= 5
            elif event.key == pygame.K_SPACE and dialogue_index < len(dialogues) - 1:
                dialogue_index += 1
                
                # Récupérer les touches appuyées
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:  # Déplacer à gauche
        prisme_x -= vitesse
    if keys[pygame.K_RIGHT]:  # Déplacer à droite
        prisme_x += vitesse
    if keys[pygame.K_UP]:  # Monter
        prisme_y -= vitesse
    if keys[pygame.K_DOWN]:  # Descendre
        prisme_y += vitesse

    # Définir la couleur de la lumière en fonction de l'angle
    if 40 <= prisme_angle <= 50:
        lumiere_couleur = RED
    else:
        lumiere_couleur = WHITE

    # Dessiner le prisme (rectangle gris)
    rectangle = pygame.draw.rect(screen, GREY, (350, 250, 100, 100))

    # Dessiner la lumière projetée
    pygame.draw.polygon(screen, lumiere_couleur, [(450, 300), (600, 250), (600, 350)])

    # Affichage du dialogue
    text_surface = font.render(dialogues[dialogue_index], True, WHITE)
    screen.blit(text_surface, (50, 500))
    screen.blit(prisme_image, (prisme_x, prisme_y))     # Affichage aux coordonnées (350, 250)

    
    # Mise à jour de l'affichage
    pygame.display.flip()
    pygame.time.delay(50)

    if prisme_image == rectangle:
        screen.blit(prisme_image, (50, 500))
        dialogues2 = [
            "Elias : Quelle que chose est apparut !...",
            "Maitre Léo : Qu'est ce que c'est ? ...",
            "Regarde bien...",
            "Elias : Oui je croit le voir...",
            "C'est...",
            "C'est la couleur rouge"
    ]
        print("Couleur rouge obtenue")
    dialogue2_index = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                prisme_angle += 5
            elif event.key == pygame.K_LEFT:
                prisme_angle -= 5
            elif event.key == pygame.K_SPACE and dialogue_index < len(dialogues) - 1:
                dialogue_index += 1

'''pygame.quit()
sys.exit()'''



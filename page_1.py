from ursina import *

app = Ursina()  # Créer une instance du moteur

class Game(Entity):  # Ne pas hériter de Ursina
    def __init__(self):
        super().__init__()

        self.background = Entity(
            model='quad',  # Une simple surface plane
            texture='background.jpg',  # Le fichier image
            scale=(16, 9),  # Ajuste la taille pour remplir l'écran
            z=1  # Place l'image derrière le reste
        )
        self.background.fade_in(duration=2)


        # Titre
        self.title = Text(
            text="LES COULEURS DU DESTIN",
            position=(0, 0.3),
            origin=(0, 0),
            scale=2,
            color=color.yellow
        )

        # Bouton "Jouer"
        self.play_button = Button(
            text="Jouer",
            position=(0, -0.1),
            scale=(0.2, 0.1),
            color=color.azure,
            on_click=self.start_game
        )

        # Liste de dialogues
        self.dialogues = [
            "Bienvenue Elias, ton voyage commence ici...",#trouver un nom pour le royaume
            "Chaque couleur de ton œuvre représente une émotion.",#changer le reste des phrases
            "Trouve-les toutes pour découvrir ton destin.",
            "Es-tu prêt à relever ce défi ?"
        ]
        self.dialogue_index = 0
        
        
        # Texte de dialogue (caché au début)
        self.dialogue_text = Text(
            text=self.dialogues[self.dialogue_index],
            position=(0, 0),
            origin=(0, 0),
            scale=2,
            wordwrap=40
        )
        self.dialogue_text.disable()  # Caché au début

    def start_game(self):
        """Lance le jeu en masquant le titre et le bouton, puis affiche le dialogue"""
        self.title.disable()
        self.play_button.disable()
        self.dialogue_text.enable()

    def input(self, key):
        """Gère l'appui sur la barre d'espace pour avancer dans le dialogue"""
        if key == "space" and self.dialogue_text.enabled:
            self.dialogue_index += 1
            if self.dialogue_index < len(self.dialogues):
                self.dialogue_text.text = self.dialogues[self.dialogue_index]
            else:
                self.dialogue_text.disable()  # Fin du dialogue

# Instancier le jeu
game = Game()
app.run()

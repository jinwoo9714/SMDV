
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
window.title = "Les Couleurs du Destin"
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
camera.orthographic = True
camera.fov = 10

class Game(Entity):
    def __init__(self):
        super().__init__()

        self.background = Entity(
            model='quad',
            texture='background.jpg',
            scale=(16, 9),
            z=1
        )

        self.title = Text(
            text="LES COULEURS DU DESTIN",
            position=(0, 0.3),
            origin=(0, 0),
            scale=2,
            color=color.yellow
        )

        self.play_button = Button(
            text="Jouer",
            position=(0, -0.1),
            scale=(0.2, 0.1),
            color=color.azure,
            on_click=self.start_game
        )

        self.intro_dialogues = [
            "Bienvenue Elias, ton voyage commence ici...",
            "Chaque couleur de ton œuvre représente une émotion.",
            "Trouve-les toutes pour découvrir ton destin.",
            "Es-tu prêt à relever ce défi ?"
        ]
        self.dialogue_index = 0

        self.dialogue_text = Text(
            text=self.intro_dialogues[self.dialogue_index],
            position=(0, -0.4),
            origin=(0, 0),
            scale=1.5,
            wordwrap=40,
            color=color.white
        )
        self.dialogue_text.disable()

        self.prisme_scene = False
        self.next_scene_ready = False
        self.prisme_angle = 0
        self.prisme = None
        self.lumiere = None

        self.prisme_dialogues = [
            "Elias : Cet atelier est plongé dans l'obscurité...",
            "Maître Léo : Regarde ce prisme. Il peut révéler des couleurs cachées.",
            "Elias : Comment puis-je l’utiliser ?",
            "Maître Léo : Oriente-le correctement et observe ce qui se passe.",
            "Elias (pensif) : Peut-être que je dois viser un certain angle...",
            "C’est... la couleur rouge !"
        ]

        self.final_dialogues = [
            "Maître Léo : Tu as découvert la première couleur, Elias.",
            "Elias : Je sens que d'autres couleurs m'attendent.",
            "Maître Léo : En avant, vers la lumière intérieure..."
        ]

    def start_game(self):
        self.title.disable()
        self.play_button.disable()
        self.dialogue_text.enable()

    def input(self, key):
        if key == "space" and self.dialogue_text.enabled:
            self.dialogue_index += 1
            if not self.prisme_scene and self.dialogue_index < len(self.intro_dialogues):
                self.dialogue_text.text = self.intro_dialogues[self.dialogue_index]
            elif not self.prisme_scene:
                self.start_prisme_scene()

            elif self.prisme_scene and not self.next_scene_ready:
                if self.dialogue_index < len(self.prisme_dialogues):
                    self.dialogue_text.text = self.prisme_dialogues[self.dialogue_index]

            elif self.next_scene_ready:
                if self.dialogue_index < len(self.final_dialogues):
                    self.dialogue_text.text = self.final_dialogues[self.dialogue_index]

        if self.prisme_scene and not self.next_scene_ready:
            if key == "right arrow":
                self.prisme.x += 0.2
                self.prisme_angle += 5
                self.prisme.rotation_z = self.prisme_angle
                self.check_angle()
            elif key == "left arrow":
                self.prisme.x -= 0.2
                self.prisme_angle -= 5
                self.prisme.rotation_z = self.prisme_angle
                self.check_angle()
            elif key == "up arrow":
                self.prisme.y += 0.2
            elif key == "down arrow":
                self.prisme.y -= 0.2

    def start_prisme_scene(self):
        self.prisme_scene = True
        self.dialogue_index = 0
        self.dialogue_text.text = self.prisme_dialogues[self.dialogue_index]
        self.background.texture = None
        self.background.color = color.black

        self.prisme = Entity(
            model='quad',
            texture='white_cube',
            color=color.gray,
            scale=(1, 1),
            position=(-3, 0),
            collider='box'
        )

        self.lumiere = Entity(
            model=Mesh(vertices=[Vec3(1, 0), Vec3(4, 1.5), Vec3(4, -1.5)], mode='triangle'),
            color=color.white,
            position=self.prisme.position + Vec3(1.1, 0, 0)
        )

    def check_angle(self):
        # Le carré devient rouge uniquement à 90°
        if 89 <= self.prisme_angle <= 91:
            self.prisme.color = color.red
            self.lumiere.color = color.red
            if self.dialogue_index < len(self.prisme_dialogues) - 1:
                self.dialogue_index = len(self.prisme_dialogues) - 1
                self.dialogue_text.text = self.prisme_dialogues[self.dialogue_index]
                self.next_scene_ready = True
                print("Couleur rouge obtenue à 90°")
        else:
            self.lumiere.color = color.white
            self.prisme.color = color.gray

game = Game()
app.run()

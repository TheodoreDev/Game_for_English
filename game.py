import pygame
import pytmx
import pyscroll

from dialogues import DialogBox, LocBox
from map import MapManager
from player import Player
from player import Entity

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((900, 700))
        pygame.display.set_caption("jeu de voyage dans le temps")

        self.player = Player()
        self.map_manager = MapManager(self.screen, self.player)

        self.dialog_box = DialogBox()
        self.location_box = LocBox(self.screen, self.player)

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_z]:
            self.player.move_up()
            self.player.speed = 2

        elif pressed[pygame.K_s]:
            self.player.move_down()
            self.player.speed = 2

        elif pressed[pygame.K_d]:
            self.player.move_right()
            self.player.speed = 2

        elif pressed[pygame.K_q]:
            self.player.move_left()
            self.player.speed = 2

    def update(self):
        self.map_manager.update()
        if self.map_manager.current_map == "Tempo Forest":
            self.location_box.text = "Tempo Forest"
        elif self.map_manager.current_map == "ville":
            self.location_box.text = "         City"

    def run(self):

        clock = pygame.time.Clock()

        print("début")

        running = True

        while running:

            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            self.location_box.render(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(64)


    pygame.quit()

import pygame

from map import MapManager

class DialogBox:

    def __init__(self):
        self.box = pygame.image.load('image/dialogue/dialog_box.png')

    def render(self, screen):
        screen.blit(self.box, (0, 0))

class LocBox:

    X_POSITION = 15
    Y_POSITION = 15

    def __init__(self, screen, player):
        self.box = pygame.image.load('image/dialogue/New Piskel (1).png')
        self.box = pygame.transform.scale(self.box, (200, 70))
        self.text = ""
        self.txt_pos = ""
        self.font = pygame.font.Font("image/dialogue/dialog_font.ttf", 20)
        self.screen = screen
        self.player = player
        self.map_manager = MapManager(self.screen, self.player)

    def render(self, screen):
        screen.blit(self.box, (self.X_POSITION, self.Y_POSITION))
        text = self.font.render(self.text, False, (0, 0, 0))
        screen.blit(text, (self.X_POSITION + 10, self.Y_POSITION + 20))

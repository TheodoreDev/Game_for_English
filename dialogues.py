import pygame

class DialogBox1:

    X_POSITION = 180
    Y_POSITION = 590

    def __init__(self):
        self.box = pygame.image.load('image/dialogue/dialog_box.png')
        self.box = pygame.transform.scale(self.box, (550, 100))
        self.texts = ["Hey", "Where am I ?", "What is this world ?", "I must find someone ...", "... to ask him what's going on."]
        self.text_index = 0
        self.letter_index = 0
        self.font = pygame.font.Font("image/dialogue/dialog_font.ttf", 18)
        self.reading = True
        self.dialogue_num = 0

    def render(self, screen):
        if self.reading:
            if self.dialogue_num == 0:
                self.letter_index += 1
                if self.letter_index >= len(self.texts[self.text_index]):
                    self.letter_index = self.letter_index
                screen.blit(self.box, (self.X_POSITION, self.Y_POSITION))
                text = self.font.render(self.texts[self.text_index][0:self.letter_index], False, (0, 0, 0))
                screen.blit(text, (self.X_POSITION + 40, self.Y_POSITION + 20))

    def next_text(self):
        self.text_index += 1
        self.letter_index = 0

        if self.text_index >= len(self.texts):
            self.reading = False
            self.dialogue_num = 1

class DialogBox2:

    X_POSITION = 180
    Y_POSITION = 590

    def __init__(self):
        self.box = pygame.image.load('image/dialogue/dialog_box.png')
        self.box = pygame.transform.scale(self.box, (550, 100))
        self.texts = ["Hey", "Where am I ?", "What is this world ?", "I must find someone ...", "... to ask him what's going on.", "fsdef"]
        self.text_index = 0
        self.letter_index = 0
        self.font = pygame.font.Font("image/dialogue/dialog_font.ttf", 18)
        self.reading = False
        self.dialog1 = DialogBox1()
        self.dialogue_num = 1

    def execute(self):
        if self.reading == False:
            self.reading = True
            self.text_index = 0


    def render(self, screen):
        if self.reading:
            if self.dialogue_num == 1:
                self.letter_index += 1
                if self.letter_index >= len(self.texts[self.text_index]):
                    self.letter_index = self.letter_index
                screen.blit(self.box, (self.X_POSITION, self.Y_POSITION))
                text = self.font.render(self.texts[self.text_index][0:self.letter_index], False, (0, 0, 0))
                screen.blit(text, (self.X_POSITION + 40, self.Y_POSITION + 20))

    def next_text(self):
        self.text_index += 1
        self.letter_index = 0

        if self.text_index >= len(self.texts):
            self.reading = False
            self.dialogue_num = 2

class DialogBoxNPC:

    X_POSITION = 180
    Y_POSITION = 590
    def __init__(self):
        self.box = pygame.image.load('image/dialogue/dialog_box.png')
        self.box = pygame.transform.scale(self.box, (550, 100))
        self.texts = []
        self.text_index = 0
        self.letter_index = 0
        self.font = pygame.font.Font("image/dialogue/dialog_font.ttf", 18)
        self.reading = False
        self.dialog_read = False

    def execute(self, dialog=[]):
        if self.reading:
            self.next_text()
        else:
            self.reading = True
            self.text_index = 0
            self.texts = dialog

    def render(self, screen):
        if self.reading:
            self.letter_index += 1
            if self.letter_index >= len(self.texts[self.text_index]):
                self.letter_index = self.letter_index
            screen.blit(self.box, (self.X_POSITION, self.Y_POSITION))
            text = self.font.render(self.texts[self.text_index][0:self.letter_index], False, (0, 0, 0))
            screen.blit(text, (self.X_POSITION + 40, self.Y_POSITION + 20))
        if self.dialog_read == True:
            self.texts = ["Go find shoes in a fields ",
                          "next to the city,",
                          "A screwdriver in the tool shop of the city,",
                          "And a car in the parking of the city"]

    def next_text(self):
        self.text_index += 1
        self.letter_index = 0

        if self.text_index >= len(self.texts):
            self.reading = False
            self.dialog_read = True


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

    def render(self, screen):
        screen.blit(self.box, (self.X_POSITION, self.Y_POSITION))
        text = self.font.render(self.text, False, (0, 0, 0))
        screen.blit(text, (self.X_POSITION + 10, self.Y_POSITION + 20))

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

    def __init__(self, dialogBox1):
        self.box = pygame.image.load('image/dialogue/dialog_box.png')
        self.box = pygame.transform.scale(self.box, (550, 100))
        self.texts = ["Oh !", "I see a new type of path", "Maybe this is the way to go to the city.", "Let's go and we will see."]
        self.text_index = 0
        self.letter_index = 0
        self.font = pygame.font.Font("image/dialogue/dialog_font.ttf", 18)
        self.reading = False
        self.dialog1 = dialogBox1
        self.dialogue_num = 0

    def execute(self):
        if self.reading == False:
            self.reading = True
            self.text_index = 0


    def render(self, screen):
        if self.reading:
            if self.dialog1.dialogue_num == 1:
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

class DialogBox3:

    X_POSITION = 180
    Y_POSITION = 590

    def __init__(self, dialogBox2):
        self.box = pygame.image.load('image/dialogue/dialog_box.png')
        self.box = pygame.transform.scale(self.box, (550, 100))
        self.texts = ["Ok now I'm sure the city isn't far,", "I see the field.", "But I never saw this type of path before", "I have to be careful,", "I don't know this place", "I'll go explore."]
        self.text_index = 0
        self.letter_index = 0
        self.font = pygame.font.Font("image/dialogue/dialog_font.ttf", 18)
        self.reading = False
        self.dialog2 = dialogBox2
        self.dialogue_num = 0

    def execute(self):
        if self.reading == False:
            self.reading = True
            self.text_index = 0

    def render(self, screen):
        if self.reading:
            if self.dialog2.dialogue_num == 2:
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
            self.dialogue_num = 3

class DialogBox4:

    X_POSITION = 180
    Y_POSITION = 590

    def __init__(self, dialogBox3):
        self.box = pygame.image.load('image/dialogue/dialog_box.png')
        self.box = pygame.transform.scale(self.box, (550, 100))
        self.texts = ["Wow ...", "The city of the year 2023,", "It's beautiful and impressive !", "It's magic."]
        self.text_index = 0
        self.letter_index = 0
        self.font = pygame.font.Font("image/dialogue/dialog_font.ttf", 18)
        self.reading = False
        self.dialog3 = dialogBox3
        self.dialogue_num = 0

    def execute(self):
        if self.reading == False:
            self.reading = True
            self.text_index = 0

    def render(self, screen):
        if self.reading:
            if self.dialog3.dialogue_num == 3:
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
            self.dialogue_num = 4

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
            if self.dialog_read:
                self.texts = ["Go find shoes in a field ",
                              "next to the city,",
                              "A screwdriver in the tool shop of the city,",
                              "And a car in the parking of the city.",
                              "The city is in the south."]

    def next_text(self):
        self.text_index += 1
        self.letter_index = 0

        if self.text_index >= len(self.texts):
            self.reading = False
            self.dialog_read = True

class DialogBoxNPC2:

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

    def next_text(self):
        self.text_index += 1
        self.letter_index = 0

        if self.text_index >= len(self.texts):
            self.reading = False

class DialogBoxNPCobj:

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

    def next_text(self):
        self.text_index += 1
        self.letter_index = 0

        if self.text_index >= len(self.texts):
            self.reading = False

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

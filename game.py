import pygame
import pytmx
import pyscroll
import time

from dialogues import *
from map import MapManager
from player import Player
from player import Entity

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((900, 700))
        pygame.display.set_caption("jeu de voyage dans le temps")

        self.player = Player()
        self.dialog_box = DialogBox1()
        self.dialog_box2 = DialogBox2(self.dialog_box)
        self.dialog_box3 = DialogBox3(self.dialog_box2)
        self.dialog_box4 = DialogBox4(self.dialog_box3)
        self.dialog_box_npc2 = DialogBoxNPC2()
        self.dialog_box_obj = DialogBoxNPCobj()
        self.dialog_box_npc = DialogBoxNPC(self.dialog_box_obj)
        self.map_manager = MapManager(self.screen, self.player, self.dialog_box_npc, self.dialog_box_npc2, self.dialog_box_obj, self.dialog_box, self.dialog_box2, self.dialog_box3, self.dialog_box4)
        self.location_box = LocBox(self.screen, self.player)
        self.inventory_box = InventoryBox(self.dialog_box_obj)
        self.win_box = WinBox()

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
        elif self.map_manager.current_map == "parking":
            self.location_box.text = "     Parking"
        elif self.map_manager.current_map == "tool_shop":
            self.location_box.text = "DIY tool shop"
        self.map_manager.check_dialogBox_collision(self.dialog_box2)
        self.map_manager.check_dialogBox3_collision(self.dialog_box3)
        self.map_manager.check_dialogBox4_collision(self.dialog_box4)
        if self.dialog_box_obj.dialog_read_camaro == True and self.dialog_box_obj.dialog_read_bosch == False and self.dialog_box_obj.dialog_read_shoes == False:
            self.inventory_box.name = "HUD_obj1"
        elif self.dialog_box_obj.dialog_read_camaro == True and self.dialog_box_obj.dialog_read_bosch == True and self.dialog_box_obj.dialog_read_shoes == False:
            self.inventory_box.name = "HUD_obj2"
        elif self.dialog_box_obj.dialog_read_camaro == True and self.dialog_box_obj.dialog_read_bosch == False and self.dialog_box_obj.dialog_read_shoes == True:
            self.inventory_box.name = "HUD_obj2-2"
        elif self.dialog_box_obj.dialog_read_camaro == False and self.dialog_box_obj.dialog_read_bosch == True and self.dialog_box_obj.dialog_read_shoes == False:
            self.inventory_box.name = "HUD_obj1-2"
        elif self.dialog_box_obj.dialog_read_camaro == False and self.dialog_box_obj.dialog_read_bosch == True and self.dialog_box_obj.dialog_read_shoes == True:
            self.inventory_box.name = "HUD_obj2-3"
        elif self.dialog_box_obj.dialog_read_camaro == False and self.dialog_box_obj.dialog_read_bosch == False and self.dialog_box_obj.dialog_read_shoes == True:
            self.inventory_box.name = "HUD_obj1-3"
        elif self.dialog_box_obj.dialog_read_camaro == True and self.dialog_box_obj.dialog_read_bosch == True and self.dialog_box_obj.dialog_read_shoes == True:
            self.inventory_box.name = "HUD_obj3"
        else:
            self.inventory_box.name = "HUD_obj0"
        if self.dialog_box_obj.dialog_read_camaro == True and self.dialog_box_obj.dialog_read_bosch == True and self.dialog_box_obj.dialog_read_shoes == True:
            self.dialog_box_npc.texts = ["Wow !!",
                                         "You got all the objects.",
                                         "Now, I can repair the portal,",
                                         "And you can go back in your origin world !"]
        elif self.dialog_box_npc.dialog_read == True:
            self.dialog_box_npc.texts = ["Go find shoes in a field ",
                                         "next to the city,",
                                         "A green screwdriver in the tool shop of the city,",
                                         "And a car in the parking of the city.",
                                         "The city is in the south."]

    def run(self):

        clock = pygame.time.Clock()

        print("début")

        running = True

        while running:

            self.player.save_location()
            if self.dialog_box_npc.end == False:
                if self.dialog_box_npc.reading == False and self.dialog_box_npc2.reading == False and self.dialog_box_obj.reading == False and self.dialog_box.reading == False and self.dialog_box2.reading == False and self.dialog_box3.reading == False and self.dialog_box4.reading == False:
                    self.handle_input()
            self.update()
            self.map_manager.draw()
            self.dialog_box.render(self.screen)
            self.dialog_box2.render(self.screen)
            self.dialog_box3.render(self.screen)
            self.dialog_box4.render(self.screen)
            self.dialog_box_npc.render(self.screen)
            self.dialog_box_npc2.render(self.screen)
            self.dialog_box_obj.render(self.screen)
            if self.dialog_box_npc.dialog_read == True:
                self.location_box.render(self.screen)
                self.inventory_box.render(self.screen)
            if self.dialog_box_npc.end == True:
                self.win_box.render(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.dialog_box.reading:
                            self.dialog_box.next_text()
                        if self.dialog_box2.reading:
                            self.dialog_box2.next_text()
                        if self.dialog_box3.reading:
                            self.dialog_box3.next_text()
                        if self.dialog_box4.reading:
                            self.dialog_box4.next_text()
                        self.map_manager.check_npc_collision(self.dialog_box_npc, self.dialog_box_npc2, self.dialog_box_obj)
                        self.map_manager.check_dialogBoxNPC_collision(self.dialog_box_npc2)

            clock.tick(64)


    pygame.quit()
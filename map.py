from dataclasses import dataclass

import pygame
import pytmx
import pyscroll

import player
from player import NPC
from dialogues import DialogBox1, DialogBoxNPC, DialogBox2


@dataclass
class Portal:
    from_world: str
    origin_point: str
    target_world: str
    teleport_point: str


@dataclass
class HiddenBox:
    box_hidden_name: str
    world: str


@dataclass
class DialogsBoxs2:
    dialogs_boxs2_name: str
    world: str


@dataclass
class Map:
    name: str
    walls: list[pygame.Rect]
    group: pyscroll.PyscrollGroup
    tmx_data: pytmx.TiledMap
    portals: list[Portal]
    npcs: list[NPC]
    hidden_box: list[HiddenBox]
    dialogs_boxs2: list[DialogsBoxs2]


class MapManager:
    def __init__(self, screen, player, dialogBoxNPC, dialogBox, dialogBox2):
        self.maps = dict()
        self.screen = screen
        self.player = player
        self.dialog_box = dialogBox
        self.dialog_box2 = dialogBox2
        self.dialog_box_npc = dialogBoxNPC
        self.current_map = "Tempo Forest"
        self.player_loc = "Tempo Forest"

        self.register_map("Tempo Forest", portals=[
            Portal(from_world="Tempo Forest", origin_point="enter_ville", target_world="ville",
                   teleport_point="spawn_ville")
        ], npcs=[
            NPC("paul", nb_points=4, speed=1, dialog=["Hello",
                                                      "I saw you coming out of the portal.",
                                                      "How are you ?",
                                                      "I'm fine, thanks",
                                                      "Where are we ?",
                                                      "We are on the Earth, in 2023. Why ?",
                                                      "WHAT !! We are in 2023 ?",
                                                      "Yes.",
                                                      "Okay, calm down.",
                                                      "If you want, I can repair the portal",
                                                      "You can do this for me ?",
                                                      "Sure ...",
                                                      "Just, I need a little help.",
                                                      "Everything you want !",
                                                      "Ok, go find shoes in a fields ",
                                                      "next to the city,",
                                                      "A screwdriver in the tool shop of the city,",
                                                      "And a car in the parking of the city",
                                                      "Ok"])
        ], hidden_box=[
            HiddenBox(box_hidden_name="buisson", world="Tempo Forest"),
        ], dialogs_boxs2=[
            DialogsBoxs2(dialogs_boxs2_name="dialogue2", world="Tempo Forest")
        ])
        self.register_map("ville", portals=[
            Portal(from_world="ville", origin_point="enter_Tempo-Forest", target_world="Tempo Forest",
                   teleport_point="spawn_Tempo-Forest")
        ], npcs=[
            NPC("camaro1", nb_points=4, speed=5, dialog=["VROOMMMM"]),
            NPC("camaro2", nb_points=4, speed=5, dialog=["VROOMMMM"])
        ], hidden_box=[
            HiddenBox(box_hidden_name="wheat", world="ville"),
        ])

        self.teleport_player("player")
        self.teleport_npcs()

    def check_npc_collision(self, dialog_box_npc):
        for sprite in self.get_group().sprites():
            if self.dialog_box.reading == False:
                if sprite.feet.colliderect(self.player.rect) and type(sprite) is NPC:
                    dialog_box_npc.execute(sprite.dialog)
                    print("ok")

    def check_dialogBox_collision(self, dialog_box2):
        for dialogs in self.get_map().dialogs_boxs2:
            if dialogs.world == self.current_map:
                point = self.get_object(dialogs.dialogs_boxs2_name)
                rect = pygame.Rect(point.x, point.y, point.width, point.height)
                if self.player.feet.colliderect(rect):
                    dialog_box2.execute()

    def check_collision(self):
        for portal in self.get_map().portals:
            if portal.from_world == self.current_map:
                point = self.get_object(portal.origin_point)
                rect = pygame.Rect(point.x, point.y, point.width, point.height)
                if self.player.feet.colliderect(rect):
                    print("collid ok")
                    if self.dialog_box_npc.dialog_read == True:
                        print("past ok")
                        copy_portal = portal
                        self.current_map = portal.target_world
                        self.teleport_player(copy_portal.teleport_point)
                    else:
                        print("no")

        for sprite in self.get_group().sprites():
            if type(sprite) is NPC:
                if sprite.feet.colliderect(self.player.rect):
                    sprite.speed = 0
                else:
                    if sprite.name == "camaro1" or sprite.name == "camaro2":
                        sprite.speed = 5
                    elif sprite.name == "paul":
                        sprite.speed = 1
            if sprite.feet.collidelist(self.get_walls()) > -1:
                sprite.move_back()

        for hiddens in self.get_map().hidden_box:
            if hiddens.world == self.current_map:
                point = self.get_object(hiddens.box_hidden_name)
                rect = pygame.Rect(point.x, point.y, point.width, point.height)
                if self.player.feet.colliderect(rect):
                    self.player.hide = True
                else:
                    self.player.hide = False

    def teleport_player(self, name):
        point = self.get_object(name)
        self.player.position[0] = point.x
        self.player.position[1] = point.y
        self.player.save_location()

    def register_map(self, name, portals=[], npcs=[], hidden_box=[], dialogs_boxs2=[]):
        tmx_data = pytmx.util_pygame.load_pygame(f"map/carte (.tmx)/{name}.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 3

        walls = []
        loc = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            if obj.type == "lieu":
                loc.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        group.add(self.player)

        for npc in npcs:
            group.add(npc)

        self.maps[name] = Map(name, walls, group, tmx_data, portals, npcs, hidden_box, dialogs_boxs2)

    def get_map(self):
        return self.maps[self.current_map]

    def get_group(self):
        return self.get_map().group

    def get_walls(self):
        return self.get_map().walls

    def get_object(self, name):
        return self.get_map().tmx_data.get_object_by_name(name)

    def get_loc(self):
        return self.get_map().name

    def teleport_npcs(self):
        for map in self.maps:
            map_data = self.maps[map]
            npcs = map_data.npcs

            for npc in npcs:
                npc.load_points(map_data.tmx_data)
                npc.teleport_spawn()

    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)

    def update(self):
        self.get_group().update()
        self.check_collision()

        for npc in self.get_map().npcs:
            npc.move()

import pygame

from animation import AnimateSprite


class Entity(AnimateSprite):
    def __init__(self, name, x, y):
        super().__init__(name)
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
        self.hide = False

    def save_location(self): self.old_position = self.position.copy()

    def move_right(self):
        if self.hide == True:
            self.change_animation("right_hide")
        else:
            self.change_animation("right")
        self.position[0] += self.speed

    def move_left(self):
        if self.hide == True:
            self.change_animation("left_hide")
        else:
            self.change_animation("left")
        self.position[0] -= self.speed

    def move_up(self):
        if self.hide == True:
            self.change_animation("up_hide")
        else:
            self.change_animation("up")
        self.position[1] -= self.speed

    def move_down(self):
        if self.hide == True:
            self.change_animation("down_hide")
        else:
            self.change_animation("down")
        self.position[1] += self.speed

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

class Player(Entity):
    def __init__(self):
        super().__init__("planche cendrillon de face", 0, 0)

class NPC(Entity):
    def __init__(self, name, nb_points, speed, dialog):
        super().__init__(name, 0, 0)
        self.nb_points = nb_points
        self.points = []
        self.name = name
        self.speed = speed
        self.dialog = dialog
        self.current_point = 0
        self.hidecar = 0

    def move(self):
        current_point = self.current_point
        target_point = self.current_point + 1

        if target_point >= self.nb_points:
            target_point = 0
            self.hidecar = 1

        current_rect = self.points[current_point]
        target_rect = self.points[target_point]

        if current_rect.y < target_rect.y and abs(current_rect.x - target_rect.x) < 3:
            self.move_down()
            if self.hidecar == 0:
                self.speed = 30

        elif current_rect.y > target_rect.y and abs(current_rect.x - target_rect.x) < 3:
            self.move_up()
            if self.hidecar == 0:
                self.speed = 30

        elif current_rect.x > target_rect.x and abs(current_rect.y - target_rect.y) < 3:
            self.move_left()
            if self.hidecar == 0:
                self.change_animation("left_hide")
                self.speed = 30

        elif current_rect.x < target_rect.x and abs(current_rect.y - target_rect.y) < 3:
            self.move_right()
            if self.hidecar == 0:
                self.change_animation("right_hide")
                self.speed = 30

        if self.rect.colliderect(target_rect):
            self.current_point = target_point

    def teleport_spawn(self):
        location = self.points[self.current_point]
        self.position[0] = location.x
        self.position[1] = location.y
        self.save_location()

    def load_points(self, tmx_data):
        for num in range(1, self.nb_points+1):
            point = tmx_data.get_object_by_name(f"{self.name}_path{num}")
            rect = pygame.Rect(point.x, point.y, point.width, point.height)
            self.points.append(rect)

import pygame

class AnimateSprite(pygame.sprite.Sprite) :
    def __init__(self, name):
        super().__init__()
        self.spite_sheet = pygame.image.load(f'image/player-PNJ/{name}.png')
        self.animation_index = 0
        self.clock = 0
        self.images = {
            'down': self.get_images(0),
            'left': self.get_images(0),
            'right': self.get_images(0),
            'up': self.get_images(32)
        }
        self.speed = 2

    def change_animation(self, name):
        self.image = self.images[name][self.animation_index]
        self.image.set_colorkey((0, 0, 0))
        self.clock += self.speed * 12
        if self.clock >= 100:

            self.animation_index += 1

            if self.animation_index >= len(self.images[name]):
                self.animation_index = 0

            self.clock = 0

    def get_images(self, y):
        images = []

        for i in range(0, 7):
            x = i*32
            image = self.get_image(x, y)
            images.append(image)

        return images

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.spite_sheet, (0, 0), (x, y, 32, 32))
        return image
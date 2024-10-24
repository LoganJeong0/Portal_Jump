import pygame
class cdoor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        image = pygame.image.load("citydoor.png")
        image_size = image.get_size()
        new_size = image_size[0] / 3.5, image_size[1] / 3.5
        self.image_size = new_size
        self.image = image
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.image = pygame.transform.scale(self.image, (self.image_size[0], self.image_size[1]))

    def set_location(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


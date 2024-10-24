import pygame
class treeleft(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        image = pygame.image.load("treeL.png")
        image_size = image.get_size()
        new_size = image_size[0] * 2.5, image_size[1] * 2.5
        new_rect = image_size[0] * 2, image_size[1] * 2
        self.rect_size = new_rect
        self.image_size = new_size
        self.image = image
        self.rect = pygame.Rect(self.x, self.y, self.rect_size[0], self.rect_size[1])
        self.image = pygame.transform.scale(self.image, (self.image_size[0], self.image_size[1]))

    def set_location(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

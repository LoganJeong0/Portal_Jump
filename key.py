import pygame
class Key(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image_list = ("key1.png" , "key2.png" , "key3.png" , "key4.png" , "key5.png" , "key6.png" , "key7.png" , "key8.png" ,)
        image = pygame.image.load(self.image_list[0])
        image_size = image.get_size()
        new_size = image_size[0] * .75, image_size[1] * .75
        rect_size = image_size[0] * 0, image_size[1] * 0
        self.image_size = new_size
        self.new_rect_size = rect_size
        self.image = image
        self.rect = pygame.Rect(self.x, self.y, self.new_rect_size[0], self.new_rect_size[1])
        self.image = pygame.transform.scale(self.image, (self.image_size[0], self.image_size[1]))
        self.delta = 6
        self.index = 0


    def animate(self):
      image = pygame.image.load(self.image_list[self.index])
      image_size = image.get_size()
      new_size = image_size[0] * .75, image_size[1] * .75
      self.image_size = new_size
      self.image = image
      self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
      self.image = pygame.transform.scale(self.image, (self.image_size[0], self.image_size[1]))
      self.index += 1
      if self.index > 7:
        self.index = 0


import pygame
class player(pygame.sprite.Sprite):

   def __init__(self, x, y):
       super().__init__()
       self.x = x
       self.y = y
       self.image_list = ("characterspriteR1.png" , "characterspriteR2.png" , "characterspriteR3.png" ,
                          "characterspriteL1.png" , "characterspriteL2.png" , "characterspriteL3.png")
       image = pygame.image.load(self.image_list[0])
       image_size = image.get_size()
       new_size = image_size[0] * 2, image_size[1] * 2
       rect_size = image_size[0] * 0, image_size[1] * 0
       self.image_size = new_size
       self.new_rect_size = rect_size
       self.image = image
       self.rect = pygame.Rect(self.x, self.y, self.new_rect_size[0], self.new_rect_size[1])
       self.image = pygame.transform.scale(self.image, (self.image_size[0], self.image_size[1]))
       self.delta = 6
       self.index = 0
       self.index2 = 3
      # self.grav = 1


   def move_direction(self, d):
       if d == "right":
           self.x = self.x + self.delta
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
       if d == "left":
           self.x = self.x - self.delta
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
       if d == "down":
           self.y = self.y + self.delta
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
       if d == "up":
           self.y = self.y - self.delta
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


   def switch_animation_right(self):
     image = pygame.image.load(self.image_list[self.index])
     image_size = image.get_size()
     new_size = image_size[0] * 2, image_size[1] * 2
     self.image_size = new_size
     self.image = image
     self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
     self.image = pygame.transform.scale(self.image, (self.image_size[0], self.image_size[1]))
     self.index += 1
     if self.index > 2:
       self.index = 0


   def switch_animation_left(self):
     image = pygame.image.load(self.image_list[self.index2])
     image_size = image.get_size()
     new_size = image_size[0] * 2, image_size[1] * 2
     self.image_size = new_size
     self.image = image
     self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
     self.image = pygame.transform.scale(self.image, (self.image_size[0], self.image_size[1]))
     self.index2 += 1
     if self.index2 > 5:
       self.index2 = 3






import pygame
from blueportal import BluePortal
from redportal import RedPortal
from player_sprite import player
from citytileL import cityleft
from citytileM import citymid
from citytileR import cityright
from lose import lose_screen
from citydoor import cdoor
from key import Key
from treetileR import treeright
from treetileL import treeleft
from treetileM import treemid
from win import win_screen

def blit_city():
   screen.blit(city_left1.image, city_left1.rect)
   screen.blit(city_right1.image, city_right1.rect)
   screen.blit(city_mid1.image, city_mid1.rect)
   screen.blit(city_mid2.image, city_mid2.rect)
   screen.blit(city_right2.image, city_right2.rect)
   screen.blit(city_left2.image, city_left2.rect)
   screen.blit(city_left3.image, city_left3.rect)
   screen.blit(city_right3.image, city_right3.rect)
   screen.blit(city_left4.image, city_left4.rect)




def blit_tree():
   screen.blit(tree_left1.image, tree_left1.rect)
   screen.blit(tree_right1.image, tree_right1.rect)
   screen.blit(tree_mid1.image, tree_mid1.rect)
   screen.blit(tree_left2.image, tree_left2.rect)
   screen.blit(tree_right2.image, tree_right2.rect)
   screen.blit(tree_mid2.image, tree_mid2.rect)
   screen.blit(tree_left3.image, tree_left3.rect)
   screen.blit(tree_right3.image, tree_right3.rect)
   screen.blit(tree_left4.image, tree_left4.rect)
   screen.blit(tree_right4.image, tree_right4.rect)
   screen.blit(tree_mid3.image, tree_mid3.rect)


def bg_scale(scale, scale2, image):
 bg = pygame.image.load(image)
 size = bg.get_size()
 new_size = (size[0] / scale, size[1] / scale2)
 bg = pygame.transform.scale(bg, new_size)
 return bg




# set up pygame modules
pygame.init()
pygame.font.init()
r = 0
b = 0
g = 0




# set up variables for the display
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
bg = bg_scale(1.2, 1.2, "bgcity.png")
city = True
jump = False
animR1 = True
change_bg = False
in_air = False
death = False
blit_map_c = True
have_key = False
win = False


char = player(15, 300)
bp = BluePortal(1000, 1000)
rp = RedPortal(400, 75)
city_door = cdoor(800, 75)
gold_key = Key(400, 430)
loser = lose_screen(280, 200)
win_text = win_screen(225, 125)


#C platform 1
city_left1 = cityleft(15, 447)
city_mid1 = citymid(115, 446)
city_right1 = cityright(215, 446)


#C platform 2
city_right2 = cityright(425, 300)
city_left2 = cityleft(325, 301)


#C platform 3
city_right3 = cityright(185, 100)
city_left3 = cityleft(85, 101)


#C platform 4
city_left4 = cityleft(700, 201)
city_mid2 = citymid(800, 200)


#T platform 1
tree_left1 = treeleft(300, 190)
tree_mid1 = treemid(375, 190)
tree_right1 = treeright(450, 190)


#T platform 2
tree_left2 = treeleft(550, 380)
tree_mid2 = treemid(625, 380)
tree_right2 = treeright(700, 380)

#T platform 3
tree_left3 = treeleft(335, 500)
tree_right3 = treeright(415, 500)

#T platform 4
tree_left4 = treeleft(50, 380)
tree_mid3 = treemid(125, 380)
tree_right4 = treeright(200, 380)


velocity = 20
jump_height = velocity
gravity = 1
frame = 0
clock = pygame.time.Clock()

sprite_group = pygame.sprite.Group()
sprite_group.add(city_left1, city_mid1, city_right2, city_right1, city_left2, city_right3, city_left3, city_left4, city_mid2)
run = True

# -------- Main Program Loop -----------
while run:
 clock.tick(60)


 for event in pygame.event.get():
     if event.type == pygame.QUIT:
         run = False


 if death == False and win == False:
     if frame % 10 == 0:
         gold_key.animate()


     collided_sprites = pygame.sprite.spritecollide(char, sprite_group, False)
     if len(collided_sprites) == 0 and jump == False:
         in_air = True

     else:
         in_air = False




     keys = pygame.key.get_pressed()
     if keys[pygame.K_d]:
         char.move_direction("right")
         if frame % 10 == 0:
             char.switch_animation_right()
     if keys[pygame.K_a]:
         char.move_direction("left")
         if frame % 10 == 0:
             char.switch_animation_left()
     if keys[pygame.K_SPACE] and in_air == False:
         jump = True
     if pygame.Rect.colliderect(char.rect, rp.rect) and keys[pygame.K_e]:
         bp.set_location(370, 0)
         rp.set_location(1000, 1000)
         char.x = bp.x
         char.y = bp.y + 20
         char.rect = pygame.Rect(char.x, char.y, char.image_size[0],
                                        char.image_size[1])
         city = not city
         change_bg = True
         blit_map_c = False
         sprite_group = pygame.sprite.Group()
         sprite_group.add(tree_left1, tree_right1, tree_mid1, tree_left2, tree_right2, tree_mid2, tree_left3, tree_right3, tree_left4, tree_right4, tree_mid3)




     if pygame.Rect.colliderect(char.rect, bp.rect) and keys[pygame.K_f]:
         bp.set_location(1000, 1000)
         rp.set_location(400, 75)
         char.x = rp.x
         char.y = rp.y + 20
         char.rect = pygame.Rect(char.x, char.y, char.image_size[0],
                                        char.image_size[1])
         city = not city
         change_bg = True
         blit_map_c = True
         sprite_group = pygame.sprite.Group()
         sprite_group.add(city_left1, city_mid1, city_right2, city_right1, city_left2, city_right3, city_left3,
                          city_left4, city_mid2)

     if jump:
         char.y -= velocity
         velocity -= gravity
         if velocity < 0:
             jump = False
             velocity = jump_height
         char.rect = pygame.Rect(char.x, char.y, char.image_size[0],
                                        char.image_size[1])

     if in_air:
         char.y += 10
         char.rect = pygame.Rect(char.x, char.y, char.image_size[0],
                                        char.image_size[1])

     if pygame.Rect.colliderect(char.rect, gold_key.rect):
         have_key = True

     if pygame.Rect.colliderect(char.rect, city_door.rect) and keys[pygame.K_e] and have_key == True:
         win = True

     if change_bg:
         if city:
             bg = bg_scale(1.2, 1.2, "bgcity.png")
         else:
             bg = bg_scale(.77, 0.62, "bgtree.jpg")
         change_bg = False


     if char.y > 1000:
         death = True

     screen.blit(bg, (0, 0))
     screen.blit(bp.image, bp.rect)
     screen.blit(rp.image, rp.rect)
     if blit_map_c:
         screen.blit(city_door.image, city_door.rect)
     screen.blit(char.image, char.rect)
     if blit_map_c:
       blit_city()
     if blit_map_c == False:
       if have_key == False:
            screen.blit(gold_key.image, gold_key.rect)
       blit_tree()
     pygame.display.update()
     frame += 1


 if death == True:
     screen.fill((36, 36, 36))
     screen. blit(loser.image, loser.rect)
     pygame.display.update()

 if win == True:
     screen.fill((0, 0, 0))
     screen.blit(win_text.image, win_text.rect)
     pygame.display.update()




pygame.quit()

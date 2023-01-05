import pygame
import random
import spells
from random import randint

pygame.init()
pygame.time.set_timer(pygame.USEREVENT,2000)
W , H=600,500

# Set the window size
window_size = (W,H)
BLACK=(0,0,0)
WHITE = (255,255,255)
# Create the window
screen = pygame.display.set_mode(window_size)
background_image = pygame.image.load('image/background.jpg')
# Set the window size and title
pygame.display.set_caption('Number Field')
# Load the images
image1 = pygame.image.load('image/wex.png')
# Get the current size of the image
width, height = image1.get_size()
# Scale the image to half its size
scaled_image = pygame.transform.scale(image1, (width // 4, height // 4))
image2 = pygame.image.load('image/exort.png')
# Get the current size of the image
width, height = image2.get_size()
# Scale the image to half its size
scaled_image2 = pygame.transform.scale(image2, (width // 4, height // 4))
image3 = pygame.image.load('image/quas.png')
# Get the current size of the image
width, height = image3.get_size()
# Scale the image to half its size
scaled_image3 = pygame.transform.scale(image3, (width // 4, height // 4))
# Create a list to store the images
images = [scaled_image, scaled_image2, scaled_image3]
screen.blit(background_image, (-650, -200))
# This function adds an image to the list and updates the display
def add_image(img):
  try:
      images.pop(0)
  except IndexError:
    pass
  images.append(img)
  update_display()
def update_display():
  for i, img in enumerate(images):
    screen.blit(img, (-60 + i * 170, 370))
  pygame.display.flip()  # Update the display

# Set the window title and icon
pygame.display.set_caption("Invoker Game")
pygame.display.set_icon(pygame.image.load('image/invoke.jpg'))



# Load the background image


# Set the running variable to True
running = True
image1 = pygame.image.load('image/quas.png')
image2 = pygame.image.load('image/wex.png')
speed = 1
FPS=60
speels_images = ['alacrity.jpg','chaos_meteor.jpg','cold_snap.jpg','deafening_blast.jpg','EMP.jpg','forge_spirit.jpg','ghost_walk.jpg','ice_wall.jpg','sun_strike.jpg','tornado.jpg']
speels_surf = [pygame.image.load('image/'+path).convert_alpha()for path in speels_images]

def createBall(group):
    indx = randint(0, len(speels_surf)-1)
    x = randint(20, W-20)
    speed = randint(1, 4)
    return spells.Spell(x, speed, speels_surf[indx], group)




clock=pygame.time.Clock()
spelles = pygame.sprite.Group()


# Run the game loop
while True:
    screen.fill((255, 255, 255))
    screen.blit(background_image, (-640, -220))
    update_display()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            createBall(spelles)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                add_image(scaled_image)
            elif event.key == pygame.K_e:
                add_image(scaled_image2)
            elif event.key == pygame.K_q:
                add_image(scaled_image3)
            elif event.key == pygame.K_SPACE:
                createBall(spelles, scaled_image)
                createBall(spelles, scaled_image2)
                createBall(spelles, scaled_image3)
                if len(images) == 3:
                  selected_spell = spells.create_spell(images, scaled_image, scaled_image2, scaled_image3)
                  images = []
                  update_display()



    # Draw the rectangles and circles
    pygame.draw.line(screen, BLACK, (600, 370), (1, 370))
    spelles.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
    spelles.update(H)

# Quit pygame
pygame.quit()

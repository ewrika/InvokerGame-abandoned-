import pygame



class Spell(pygame.sprite.Sprite):
    def __init__(self,x,speed,surf,group):
        pygame.sprite.Sprite.__init__(self)
        self.image=surf
        self.rect=self.image.get_rect(center=(x,0))
        self.speed = speed
        self.add(group)

    def update(self,*args):
        if self.rect.y < args[0] - 250:
            self.rect.y += self.speed
        else:
            self.kill()

def create_spell(images, scaled_image, scaled_image2, scaled_image3):
    # Create a dictionary that maps the images to their corresponding elements
    elements = {scaled_image: 'Quas', scaled_image2: 'Wex', scaled_image3: 'Exort'}

    # Get the elements of the spell
    quas, wex, exort = [elements[img] for img in images]

    # Return the selected spell based on the elements
    if quas == 'Quas' and wex == 'Wex' and exort == 'Exort':
        return 'deafening_blast.jpg'

    elif quas == 'Quas' and wex == 'Wex' and exort == 'Quas':
        return 'cold_snap.jpg'
    elif quas == 'Quas' and wex == 'Exort' and exort == 'Exort':
        return 'forge_spirit.jpg'
    elif quas == 'Quas' and wex == 'Exort' and exort == 'Quas':
        return 'tornado.jpg'
    elif quas == 'Wex' and wex == 'Wex' and exort == 'Exort':
        return 'alacrity.jpg'
    elif quas == 'Wex' and wex == 'Wex' and exort == 'Quas':
        return 'ghost_walk.jpg'
    elif quas == 'Wex' and wex == 'Exort' and exort == 'Exort':
        return 'chaos_meteor.jpg'
    elif quas == 'Wex' and wex == 'Exort' and exort == 'Quas':
        return 'sun_strike.jpg'
    elif quas == 'Exort' and wex == 'Wex' and exort == 'Exort':
        return 'EMP.jpg'
    elif quas == 'Exort' and wex == 'Wex' and exort == 'Quas':
        return 'ice_wall.jpg'
    else:
        return 'Invalid Spell'
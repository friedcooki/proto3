import pygame
from pygame.sprite import Sprite
import math

pygame.init() #inisialises pygame
#screen dimentions
screenDimention :tuple[int,int] = (1920,1080)
#make the screen
screen = pygame.display.set_mode(screenDimention)
#setfps
clock = pygame.time.Clock()

#game var:
run:bool = True
events = pygame.event.get()

#coord
tableTopCorner: tuple[int,int] = (150,80)

#images
tableIMG = pygame.image.load("table.png").convert_alpha() #makes tableIMG hold the image of the cue table
tableIMG = pygame.transform.scale(tableIMG, (int(tableIMG.get_width() * 1.3),int(tableIMG.get_height() * 1.3))) #scales that image up so that it takes up more of the screen

class Ball(pygame.sprite.Sprite):
    def __init__(self,image:str):
        """
        Constructor for my Ball class
        Args:
            image: name of the image you want displayed in files
        Returns:
            None
        """
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png(image)#load_png() returns both the image and rect of a png hence the self.image, self.rect

    def calcNewPos(self,vector):
        """
        method to calculate the balls new position after a force is applied
        Args:
            vector: tuple - holds the angle and magnitude of a force
        Returns:
            rect.move(dx,dy) - used to move the rect to the right spot in a different method
        """
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle), z*math.sin(angle))
        return rect.move(dx,dy)


    def update(self,vector):
        """
        Updates the rect of the image after calculating its new position
        Args:
            vector - direction and magnitude of the force applied
        Returns:
            None
        """
        newpos = self.calcNewPos(self.rect,self.vector)
        self.rect = newpos
        



#game loop
while run:
    #fills the screen in
    screen.fill((255,255,255))
    #draws the pool table
    screen.blit(tableIMG,tableTopCorner)
    #event loop
    for event in events:
        #check for pressing the close button windows
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    #updates the display
    pygame.display.update()
    #sets the fps to 60
    clock.tick(60)
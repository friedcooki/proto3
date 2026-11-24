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
    def __init__(self,image:str,x:int,y:int,scale:float):
        """
        Constructor for my Ball class
        Args:
            image: name of the image you want displayed in files
            x - the x coordinate of the ball
            y - the y coordinate of the ball
            scale - what to scale the image by
        Returns: 
            None
        """
        pygame.sprite.Sprite.__init__(self)
        self.scale = scale
        self.image = pygame.image.load(image).convert_alpha()  #loads the png
        self.image = pygame.transform.scale(self.image,(int(self.image.get_width() * self.scale),int(self.image.get_height()*self.scale))) #scales the image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(self.x,self.y)) #gets the rect of the image

    def calcNewPos(self,vector):
        """
        method to calculate the balls new position after a force is applied
        Args:
            vector: tuple - holds the angle and magnitude of a force
        Returns:
            rect.move(dx,dy) - used to move the rect to the right spot in a different method
        """
        (angle,z) = vector #unpacks the vector tuple
        (dx,dy) = (z*math.cos(angle), z*math.sin(angle)) #finds the change in y and x
        return rect.move(dx,dy) #moves the rect by the change in x and y


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
    def draw(self):
        self.add(playBalls)
        ret = pygame.sprite.LayeredUpdates.draw(self,screen)
#ball images
redImg = "redBall.png"
yellowImg = "yellowBall.png"

#red ball objects
Red1 = Ball(redImg,450,560,0.15)
Red2 = Ball(redImg,550,520,0.15)
Red3 = Ball(redImg,600,500,0.15)
#yellow ball objects
Yellow1 = Ball(yellowImg,500,540,0.09)
Yellow2 = Ball(yellowImg,400,580,0.09)
#ball sprite groups
playBalls = pygame.sprite.Group()
playBalls.add(Red1,Red2,Red3,Yellow1,Yellow2)
pygame.sprite.Sprite.visible = True

#game loop
while run:
    #fills the screen in
    screen.fill((255,255,255))
    #draws the pool table
    screen.blit(tableIMG,tableTopCorner)

    #draws the ball's group
    playBalls.draw(screen)

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
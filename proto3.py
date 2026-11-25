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
        
class Cue():
    def __init__(self,pos,scale):
        self.image = pygame.image.load("cue.png").convert_alpha()
        self.scale = scale
        self.image = pygame.transform.scale(self.image,(int(self.image.get_width()*self.scale),int(self.image.get_height()*self.scale)))
        #look at coding with russ
        self.angle = 0 #radians
        
#ball images
redImg = "redBall.png"
yellowImg = "yellowBall.png"
blackImg = "blackBall.png"
whiteImg = "cue.png"
#red ball objects
Red1 = Ball(redImg,495,560,0.15)
Red2 = Ball(redImg,565,520,0.15)
Red3 = Ball(redImg,600,500,0.15)
Red4 = Ball(redImg,460,490,0.15)
Red5 = Ball(redImg,495,470,0.15)
Red6 = Ball(redImg,530,450,0.15)
Red7 = Ball(redImg,460,400,0.15)
#yellow ball objects
Yellow1 = Ball(yellowImg,530,540,0.09)
Yellow2 = Ball(yellowImg,460,580,0.09)
Yellow3 = Ball(yellowImg,460,535,0.09)
Yellow4 = Ball(yellowImg,495,515,0.09)
Yellow5 = Ball(yellowImg,565,475,0.09)
Yellow6 = Ball(yellowImg,460,445,0.09)
Yellow7 = Ball(yellowImg,495,425,0.09)
#black ball object
Black1 = Ball(blackImg,530,495,0.042)
#cue ball object
White1 = Ball(whiteImg,1400,500,0.1)

#ball sprite groups
playBalls = pygame.sprite.Group()
interactBall=pygame.sprite.Group()
playBalls.add(Red1,Red2,Red3,Yellow1,Yellow2,Yellow3,Yellow4,Black1,Yellow5,Red4,Red5,Red6,Yellow6,Yellow7,Red7)
interactBall.add(White1)

pygame.sprite.Sprite.visible = True

#game loop
while run:
    #fills the screen in
    screen.fill((255,255,255))
    #draws the pool table
    screen.blit(tableIMG,tableTopCorner)

    #draws the ball's group
    playBalls.draw(screen)
    interactBall.draw(screen)

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
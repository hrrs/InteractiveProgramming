import pygame, sys
from pygame import *

class Player(object):
    '''
    Player's snake object handling head position and direction, body part position and order, and moving and drawing its parts.
    '''

    def __init__(self,pos,direction):

        self.pos = pos
        self.direction = direction
        self.size = 20
        self.body = []

        ### Colors
        self.PURPLE = (128,0,128)
        self.BLUE = (128,128,255)


    def __repr__(self):

        return 'Head position: '+str(self.pos)+' direction: '+str(self.direction)

    def step(self):
        '''
        Advances the player's snake one move forward.
        '''
        if len(self.body)>0:
            self.body.pop(0)
            self.body.append(self.pos)
        direction = self.direction
        size = self.size
        self.pos = (self.pos[0]+direction[0]*size,self.pos[1]+direction[1]*size)

    def draw(self,surface):
        '''
        Draws the player's snake on the surface given.
        '''
        pygame.draw.circle(surface,self.PURPLE,self.pos,int(self.size/2))
        for n in self.body:
            pygame.draw.circle(surface,self.BLUE,n,int(self.size/2))

    def grow(self):
        '''
        Extends the length of the body by adding an element at the current head position.
        '''
        self.body.append(self.pos)

screen_size = (640, 480)
screen_center = (int(screen_size[0]/2),int(screen_size[1]/2))

### Initiallizes the game environment
pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Head Movement')
clock = pygame.time.Clock()
#for some reason the font part doesn't work on Harris's computer
#pygame.font.init()

### Directions
STAY = (0,0)
UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)

### Colors
BLACK = (0,0,0)
GREEN = (0,255,0)

### Adds player(s)
p1 = Player((320,240),STAY)

### Position of fruit
fruit = ()

myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('You lost', False, (0, 0, 0))

### Runtime script
running = True
while running:

    clock.tick(5) # Controls play speed
    screen.fill(BLACK)

    # Get keyboard input
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_LEFT : p1.direction = LEFT
            if event.key == K_RIGHT : p1.direction = RIGHT
            if event.key == K_UP : p1.direction = UP
            if event.key == K_DOWN : p1.direction = DOWN
            if event.key == K_g : p1.grow()

        # Quit if window closed
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            pygame.display.update()

    if p1.pos[0] <= 0 or p1.pos[0] >= screen_size[1]:
        screen.blit(textsurface,(0,0))
        running = False
    if p1.pos[0] <= 0 or p1.pos[1] >= 480:
        running = False



    # Act and render
    p1.draw(screen)
    p1.step()
    pygame.display.update()

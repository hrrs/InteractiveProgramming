import pygame, sys
from pygame import *

class Player(object):
    '''
    Player's snake object handling head position and direction, body part position and order, and moving and drawing its parts.
    '''

    def __init__(self,x,y,direction):
        
        self.pos = x, y
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


pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Head Movement')

### Directions
UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)

HEAD_WIDTH = 30
HEAD_HEIGHT = 30
headSpeedX = 1
p1head = Player(320,240,UP)
HEAD_COLOR = pygame.color.Color("red")
clock = pygame.time.Clock()

#pygame.font.init()
#myfont = pygame.font.SysFont('Comic Sans MS', 30)
#textsurface = myfont.render('You lost', False, (0, 0, 0))

direction = (0,0) #right, down
running = True
while running:
    # Clear screen with black color
    clock.tick(5)
    screen.fill( (0,0,0) )     #screen.fill(BLACK)

    # Get keyboard input
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                p1head.direction = LEFT
                #p1head.left = p1head.left - headSpeedX * 10
            if event.key == K_RIGHT:
                p1head.direction = RIGHT
                #p1head.left = p1head.left + headSpeedX * 10
            if event.key == K_UP:
                p1head.direction = UP
                #p1head.top = p1head.top - headSpeedX * 10
            if event.key == K_DOWN:
                p1head.direction = DOWN
                #p1head.top = p1head.top + headSpeedX * 10
            if event.key == K_g:
                p1head.grow()
        '''
        if p1head.left <= 0 or p1head.left >= 640:
            #screen.blit(textsurface,(0,0))
            running = False
        if p1head.top <= 0 or p1head.top >= 480:
            running = False
        '''    
        if event.type == QUIT:                                         #write this one indent out to quit!
            pygame.quit()
            sys.exit()
            pygame.display.update()

    p1head.draw(screen)
    p1head.step()

    pygame.display.update()

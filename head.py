import pygame, sys
from pygame import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Head Movement')

class Head(object):

    def __init__(self,x,y,direction):
        
        self.x = x
        self.y = y
        self.direction = direction
        self.size = 30
        self.speed = 10
        self.sprite = pygame.Rect(x,y,self.size,self.size)

    def __repr__(self):

        return 'Head position: ('+str(self.x)+','+str(self.y)+') direction: '+str(direction)

    def step():
        '''
        pos = sprite.center
        vel = self.direction
        self.sprite.center = sprite.center[0]+self.direction[0]*self.speed
        '''
    pass

### Directions
UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)

HEAD_WIDTH = 30
HEAD_HEIGHT = 30
headSpeedX = 1
# p1head = pygame.Rect(320, 240, HEAD_WIDTH, HEAD_HEIGHT)
p1head = Head(320,240,UP)
HEAD_COLOR = pygame.color.Color("red")
clock = pygame.time.Clock()

#pygame.font.init()
#myfont = pygame.font.SysFont('Comic Sans MS', 30)
#textsurface = myfont.render('You lost', False, (0, 0, 0))

direction = (0,0) #right, down
running = True
while running:
    # clear screen with black color
    clock.tick(30)
    screen.fill( (0,0,0) )     #screen.fill(BLACK)
    p1head.x = p1head.x + headSpeedX*direction[0]
    p1head.y = p1head.y + headSpeedX*direction[1]
    # p1head.left = p1head.left + headSpeedX*direction[0]
    # p1head.top = p1head.top + headSpeedX*direction[1]
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                direction = LEFT
                #p1head.left = p1head.left - headSpeedX * 10
            if event.key == K_RIGHT:
                direction = RIGHT
                #p1head.left = p1head.left + headSpeedX * 10
            if event.key == K_UP:
                direction = UP
                #p1head.top = p1head.top - headSpeedX * 10
            if event.key == K_DOWN:
                direction = DOWN
                #p1head.top = p1head.top + headSpeedX * 10
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

    # draw the paddle
    p1head.sprite.center = p1head.x,p1head.y
    screen.fill( HEAD_COLOR, p1head.sprite );

    pygame.display.update()

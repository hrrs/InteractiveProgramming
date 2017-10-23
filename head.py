import pygame, sys
from pygame import *
import random

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
        PURPLE = (128,0,128)
        BLUE = (128,128,255)

        self.head_color = PURPLE
        self.body_color = BLUE


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
        for n in self.body:
            pygame.draw.circle(surface,self.body_color,n,int(self.size/2))
        pygame.draw.circle(surface,self.head_color,self.pos,int(self.size/2))

    def grow(self):
        '''
        Extends the length of the body by adding an element at the current head position.
        '''
        self.body.append(self.pos)

def final_screen():
    text1 = font.render("GAME OVER", True, WHITE)
    text2 = font.render("YOUR SCORE", True, WHITE)
    text3 = font.render(str(len(p1.body)), True, WHITE)

    screen.blit(text1, (180, screen_size[1]/2-100))
    screen.blit(text2, (150, screen_size[1]/2))
    screen.blit(text3, (280, screen_size[1]/2+100))
    pygame.display.update()

    pygame.time.wait(5000)
    running = False

    pygame.quit()
    sys.exit()


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
WHITE = (255,255,255)
RED = (255, 0, 0)

### Adds player(s)
p1 = Player((280,240),STAY)
p2 = Player((360,240),STAY)
p2.body_color = WHITE
p2.head_color = GREEN

### Position of fruit
x_fruit = random.randrange(20, 620, 20)
y_fruit = random.randrange(20, 460, 20)
fruit = (x_fruit, y_fruit)

### Adding font and size for text in game
font = pygame.font.SysFont("Lucida Sans Typewriter", 50)
speed = 3
### Runtime script
running = True
while running:

    clock.tick(speed) # Controls play speed
    screen.fill(BLACK)

    if (p1.pos[0], p1.pos[1]) in p1.body:
        final_screen()

    if (p1.pos) == fruit:
        p1.grow()
        x_fruit = random.randrange(20, 620, 20)
        y_fruit = random.randrange(20, 460, 20)
        fruit = (x_fruit, y_fruit)
        if len(p1.body) in (2,4,7,10):
            speed = speed + 1

    if (p2.pos) in p2.body:
        final_screen()

    if (p2.pos) == fruit:
        p2.grow()
        x_fruit = random.randrange(20, 620, 20)
        y_fruit = random.randrange(20, 460, 20)
        fruit = (x_fruit, y_fruit)
        if len(p2.body) in (2,4,7,10):
            speed = speed + 1


    # Get keyboard input
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_LEFT and p1.direction != RIGHT : p1.direction = LEFT
            if event.key == K_RIGHT and p1.direction != LEFT : p1.direction = RIGHT
            if event.key == K_UP and p1.direction != DOWN : p1.direction = UP
            if event.key == K_DOWN and p1.direction != UP : p1.direction = DOWN

            if event.key == K_a and p2.direction != RIGHT : p2.direction = LEFT
            if event.key == K_d and p2.direction != LEFT : p2.direction = RIGHT
            if event.key == K_w and p2.direction != DOWN : p2.direction = UP
            if event.key == K_s and p2.direction != UP : p2.direction = DOWN

            if event.key == K_g : p1.grow()

        # Quit if window closed
        if event.type == QUIT:
            print('game ended')
            pygame.quit()
            sys.exit()
            pygame.display.update()

    if p1.pos[0] <= 0 or p1.pos[0] >= screen_size[0]:
        final_screen()

    if p1.pos[1] <= 0 or p1.pos[1] >= screen_size[1]:
        final_screen()

    if p2.pos[0] <= 0 or p2.pos[0] >= screen_size[0]:
        final_screen()

    if p2.pos[1] <= 0 or p2.pos[1] >= screen_size[1]:
        final_screen()

    if running == True:
        # Act and render
        p1.step()
        p1.draw(screen)

        p2.step()
        p2.draw(screen)
        pygame.draw.circle(screen, RED, [x_fruit, y_fruit], 10)

    pygame.display.update()

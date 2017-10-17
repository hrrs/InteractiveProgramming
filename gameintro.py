# Import the pygame library and initialise the game engine
import pygame
pygame.init()
# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My First Game')
# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop

    # --- Game logic should go here

    # --- Drawing code should go here
    # First, clear the screen to white. 
    screen.fill(WHITE)
    #The you can draw different shapes and lines or add text to your background stage.
    pygame.draw.rect(screen, RED, [55, 200, 100, 70],0)
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    pygame.draw.ellipse(screen, BLACK, [20,20,250,100], 2)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
    # --- Limit to 60 frames per second
    clock.tick(60)

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()







'''import sys, pygame
pygame.init()

size = width, height = 640, 480
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
    	speed[1] = speed[1]+1

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    '''
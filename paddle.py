import pygame, sys
from pygame import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Paddle Movement')


PADDLE_WIDTH = 10
PADDLE_HEIGHT = 10
paddleSpeedX = 1
p1Paddle = pygame.Rect(10, 430, PADDLE_WIDTH, PADDLE_HEIGHT)
PADDLE_COLOR = pygame.color.Color("red")

while True:
    # clear screen with black color
    screen.fill( (0,0,0) )

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                p1Paddle.left = p1Paddle.left - paddleSpeedX * 10
            if event.key == K_RIGHT:
                p1Paddle.left = p1Paddle.left + paddleSpeedX * 10
            if event.key == K_UP:
                p1Paddle.top = p1Paddle.top - paddleSpeedX * 10
            if event.key == K_DOWN:
                p1Paddle.top = p1Paddle.top + paddleSpeedX * 10
        if event.type == QUIT:                                         #write this one indent out to quit!
            pygame.quit()
            sys.exit()
            pygame.display.update()

    # draw the paddle
    screen.fill( PADDLE_COLOR, p1Paddle );

    pygame.display.update()

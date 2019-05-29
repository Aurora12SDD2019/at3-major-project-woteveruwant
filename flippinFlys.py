""" Main Loop for the game Flippin Flys.
Flippin Flys is an arcarde game where the main objective is the reach the highest
score possible, it is family friendly and very enjoyable.
It has a seperate file for all of its modules.
"""

__author__ = "Tynan Matthews"
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "tynan.matthews@education.nsw.gov.au"
__status__ = "Alpha"

#dependencies
import pygame as P # accesses pygame files
import sys  # to communicate with windows
from mods import *


# pygame setup - only runs once
P.init()  # starts the game engine
clock = P.time.Clock()  # creates clock to limit frames per second
loopRate = 60  # sets max speed of main loop
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 1200, 700  # sets size of screen/window
screen = P.display.set_mode(SCREENSIZE)  # creates window and game screen
P.display.set_caption("Flippin Flys")
# set variables for some colours if you wnat them RGB (0-255)
white = (255, 255, 255)
black = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 0)

rectangle = 'rect'
fly = Sprite(555,315,25,80,80)
gravity = gravity_sim('earth')
vertAcc = 0
horAcc = 0
gr = GameRun()
"""
provides a buffer that prevents the game starting before the first mouse click
this allows me to resize the screen appropriately before users begin, may be
removed at a later version of the code
"""
play = False
gr.highScore()
while play != True:
    for event in P.event.get():
        if event.type == P.MOUSEBUTTONDOWN:
            play = True
# game loop - runs loopRate times a second!
while play:  # game loop - note:  everything in this loop is indented one tab
    gr.score()
    vertAcc += gravity / 10
    fly.y += gravity / 10
    if horAcc < 0:
        horAcc += fly.vel / 20
    elif horAcc > 0:
        horAcc -= fly.vel / 20
    fly.y += vertAcc
    screen.fill(black)
    fly.draw(screen, rectangle, blue)
    fly.x += horAcc
    fly.draw(screen, rectangle, blue)
    
    for event in P.event.get():# get user interaction events
        if event.type == P.QUIT: # tests if window's X (close) has been clicked
            play = False  # causes exit of game loop
        
        # your code starts here #
        fly.draw(screen, rectangle, blue)
        if event.type == P.MOUSEBUTTONDOWN: #includes touching screen
            vertAcc = -1.6 * gravity
            screen.fill(black)
            """
            for n in range(0,540):
                fly.draw(screen, rectangle, blue)
                fly.y -= 0.4
            """
            direction = fly.move(event)
            if direction == -1:
                horAcc -= fly.vel
            else:
                horAcc += fly.vel
            # change this to do something if user clicks mouse
            # or touches screen

        


    # your code ends here #
    P.display.flip()  # makes any changes visible on the screen
    clock.tick(loopRate)  # limits game to frame per second, FPS value

# out of game loop #
print("Thanks for playing")  # notifies user the game has ended
P.quit()   # stops the game engine
sys.exit()  # close operating system window

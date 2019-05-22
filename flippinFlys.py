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
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

rectangle = 'rect'
"""
x_fly = 600
y_fly = 350
vel_fly = 5
width_fly = 90
height_fly = 70
fly = sprite(x_fly,y_fly,vel_fly,width_fly,height_fly)
"""

fly = sprite(555,315,5,90,70)
play = True  # controls whether to keep playing

# game loop - runs loopRate times a second!
while play:  # game loop - note:  everything in this loop is indented one tab

    for event in P.event.get():  # get user interaction events
        if event.type == P.QUIT:  # tests if window's X (close) has been clicked
            play = False  # causes exit of game loop
        
        # your code starts here #
        if event.type == P.MOUSEBUTTONDOWN: #includes touching screen
            fly.draw(screen, rectangle, blue)
            print("frog")
            Mx, My = P.mouse.get_pos()
            print(Mx)
            fly.move()
            # change this to do something if user clicks mouse
            # or touches screen
            pass 
        


    # your code ends here #
    P.display.flip()  # makes any changes visible on the screen
    clock.tick(loopRate)  # limits game to frame per second, FPS value

# out of game loop #
print("Thanks for playing")  # notifies user the game has ended
P.quit()   # stops the game engine
sys.exit()  # close operating system window

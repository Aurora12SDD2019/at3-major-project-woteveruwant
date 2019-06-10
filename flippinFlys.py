""" Main Loop for the game Flippin Flys.
Flippin Flys is an arcarde game where the main objective is the reach the highest
score possible, it is family friendly and very enjoyable.
It has a seperate file for all of its modules.
"""

__author__ = "Tynan Matthews"
__license__ = "GPL"
__version__ = "0.0.2"
__email__ = "tynan.matthews@education.nsw.gov.au"
__status__ = "Alpha"

#dependencies
import pygame as P # accesses pygame files
import sys  # to communicate with windows
from mods import *
import time as T

# pygame setup - only runs once
P.init()  # starts the game engine
clock = P.time.Clock()  # creates clock to limit frames per second
loopRate = 60  # sets max speed of main loop
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 1200, 700  # sets size of screen/window
screen = P.display.set_mode(SCREENSIZE)  # creates window and game screen
P.display.set_caption("Archi")
basicFont = P.font.SysFont(None, 48)

play = True
while play:
    for event in P.event.get():# get user interaction events
        if event.type == P.QUIT: # tests if window's X (close) has been clicked
            print("Thanks for playing")  # notifies user the game has ended
            P.quit()   # stops the game engine
            sys.exit()  # close operating system window
            
    fly = Sprite(555,315,25,80,80,screen, 'rect', (0,0,0))
    gameStart(screen, fly)



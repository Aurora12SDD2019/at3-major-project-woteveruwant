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
# set variables for some colours if you wnat them RGB (0-255)
"""
white = (255, 255, 255)
black = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 0)

rectangle = 'rect'
fly = Sprite(555,315,25,80,80,screen, rectangle, blue)
gravity = gravity_sim('earth')
vertAcc = 0
horAcc = 0
key = 0
enemies = []
gr = GameRun(screen)

"""
"""
provides a buffer that prevents the game starting before the first mouse click
this allows me to resize the screen appropriately before users begin, may be
removed at a later version of the code
"""
"""
play = False
gr.highScore()
while play != True:
    for event in P.event.get():
        if event.type == P.MOUSEBUTTONDOWN:
            play = True
# game loop - runs loopRate times a second!
while play:  # game loop - note:  everything in this loop is indented one tab
    play = gr.WallContact(fly.x, fly.y, fly.width, fly.height)
    if play == False:
        gr.GameOver()
    mainLoop(gr, key, fly, gravity, vertAcc, horAcc, screen, black, enemies)  
    spawn = gr.enemies()
    if spawn == 1:
        bgX, bgY, bgWidth, bgHeight = R.randint(0,SCREENWIDTH),R.randint(-50, 0), R.randint(10, 200), R.randint(10, 200)
        badGuy = Sprite(bgX,bgY,5,bgWidth,bgHeight, screen, 'rect', (0,0,0))
        print(badGuy.x, badGuy.y, badGuy.width, badGuy.height)
        badGuy.draw()
        enemies.append(badGuy)
        key +=1
    for i in range(0, key):
        if enemies[i].y < SCREENHEIGHT:
            enemies[i].fall(gravity, 0)
    fly.fall(gravity, vertAcc)
    gr.scoring()
    if horAcc < 0:
        horAcc += fly.vel / 20
    elif horAcc > 0:
        horAcc -= fly.vel / 20
    screen.fill(black)
    fly.draw()
    for i in range(0, key):
        enemies[i].draw()
    fly.x += horAcc
    fly.draw() #makes it smoother, less visual glitches
    for event in P.event.get():# get user interaction events
        if event.type == P.QUIT: # tests if window's X (close) has been clicked
            play = False  # causes exit of game loop     
        # your code starts here #
        if event.type == P.MOUSEBUTTONDOWN: #includes touching screen
            fly.vertAcc = -1.6 * gravity
            direction = fly.move(event)
            if direction == -1:
                horAcc -= fly.vel
            else:
                horAcc += fly.vel
            # change this to do something if user clicks mouse
            # or touches screen

        
    """
play = True
while play:
    for event in P.event.get():# get user interaction events
        if event.type == P.QUIT: # tests if window's X (close) has been clicked
            print("Thanks for playing")  # notifies user the game has ended
            P.quit()   # stops the game engine
            sys.exit()  # close operating system window
    gameStart(screen)
    #mainLoop(screen, SCREENWIDTH, SCREENHEIGHT)

"""
# out of game loop #
print("Thanks for playing")  # notifies user the game has ended
P.quit()   # stops the game engine
sys.exit()  # close operating system window
"""

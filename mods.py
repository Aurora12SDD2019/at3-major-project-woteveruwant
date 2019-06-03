""" Mods for the game Flippin Flys
All of the modules used within the main code, includes classes and functions
for all the characters and environments.
"""

__author__ = "Tynan Matthews"
__license__ = "GPL"
__version__ = "0.0.2"
__email__ = "tynan.matthews@education.nsw.gov.au"
__status__ = "Alpha"


""" revision notes:


"""

SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 1200, 700

#import statements for any dependencies
import pygame as P
import random as R
import sys
import time as T
#modules

def gravity_sim(planet):
    """Simulates gravity in the environment

    Designed to hopefully create a more realistic rise and fall of the fly,
    this could also be tweaked to make the game easier or harder, it allows
    the playing on other planets feature.

    Args:
        planet = what planet the fly is on, this will get the gravity value.

    Returns:
        description of the stuff that is returned by the function.

    Raises:
        AnError: An error occurred running this function.
    """
    #A dictionary to store the gravity on different planets
    planetGravity = {
        "pluto": 0.62,
        "mars": 3.711,
        "earth": 9.8,
        "jupiter": 24.79,
        "sun": 274,
        }

    return planetGravity[planet]


class GameRun():
    """Controls the game sequence.

    Controls scoring, start and end of the game. 

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self,screen):
        """Inits variables required to run game loop"""
        self.score = 0
        self.points = 0
        self.screen = screen

    def WallContact(self, x, y, width, height):
        """Performs death sequence"""
        if x < 0 or x > (SCREENWIDTH - width):
            self.highScore()
            gameOver(self.screen)
        elif y < 0 or y > (SCREENHEIGHT - height):
            self.highScore()
            gameOver(self.screen)
        else:
            return True
        
    def enemies(self):
        """These are the main obstacles of the game to avoid."""
        difficulty = 180 - self.score #increases as game goes on
        spawn = R.randint(1,difficulty) #adds a random element to whether an enemy appears
        if spawn == 1:
            print("enemy spawned")
            return 1

    def PlayerContact(self, obj1, obj2):
        """Checks to see if player has contact with any death surfaces
            if so calls the death function to end the game"""
        pass
        if obj1XRange == obj2XRange:
            pass
            
        
    def scoring(self):
        """Updates score throughout play"""
        self.points += 1
        if self.points == 180:
            self.points = 0
            self.score += 1
            print(self.score)
        
    def highScore(self):
        """Checks if high score has been beaten or not"""
        scoreCard = open('highScore.txt', 'r')
        prevHighScore = scoreCard.read()
        prevHighScore = int(prevHighScore)
        scoreCard.close()
        if self.score > prevHighScore:
            highScore = self.score
            scoreCard = open('highScore.txt', 'w+')
            scoreCard.write(str(highScore))
            print(highScore)
        else:
            highScore = prevHighScore
            print(self.score)
            print(prevHighScore)
        
class Button(object):
    """Summary of class here.

    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam=False):
        """Inits SampleClass with blah."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Performs operation blah."""

class Sprite(object):
    """Fly that flips around.

    This fly is a interactable sprite, it is how the user plays the game
    it is the main character, it needs to be able to move around in the box
    but we dont want it able to escape. It should die if it comes into contact
    with the edge of the box or any enemies
    
    Attributes:
        x = the x coordinate it will first appear at
        y = the y coordinate it will first appear at
        vel = the velocity it will move at
        width = how wide it is in pixels
        height = how high it is in pixels
    """

    def __init__(self, x, y, vel, width, height, screen, shape, color):
        """Inits Sprites with all the values we need to draw/"""
        self.x = x
        self.y = y
        self.vel = vel
        self.width = width
        self.height = height
        self.vertAcc = 0
        self.screen = screen
        self.shape = shape
        self.color = color
    

    def draw(self):
        """Draws sprite onto surface"""
        if self.shape == 'rect':
            P.draw.rect(self.screen, self.color, [self.x,self.y,self.width,self.height], 0)
        elif self.shape == 'circle':
            P.draw.circle(screen, color, [self.x, self.y, self.height], 0)
    def move(self, event):
        """ moves player left and right, also jumps up"""
        moved = False
        while moved == False:
            if event.type == P.MOUSEBUTTONDOWN:
                Mx, My = P.mouse.get_pos()
                if Mx < (SCREENWIDTH / 2):
                    print("less")
                    return -1
                else:
                    print("more")
                    return 1
    def fall(self, gravity, vertAcc):
        """ Causes gravity to exist, moves player down """
        self.vertAcc += gravity / 10
        self.y += gravity / 10
        self.y += self.vertAcc
        self.screen.fill((0,0,0))
        self.draw()

        
def mainLoop(screen, SCREENWIDTH, SCREENHEIGHT):
    """Does something amazing.

    a much longer description of the really amazing stuff this function does and how it does it.

    Args:
        arg1: the first argument required by the function.
        arg2: the second argument required by the function.
        other_silly_variable: Another optional variable, that has a much
            longer name than the other args, and which does nothing.

    Returns:
        description of the stuff that is returned by the function.

    Raises:
        AnError: An error occurred running this function.
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

    
    clock = P.time.Clock()  # creates clock to limit frames per second
    loopRate = 60  # sets max speed of main loop

    """
    provides a buffer that prevents the game starting before the first mouse click
    this allows me to resize the screen appropriately before users begin, may be
    removed at a later version of the code
    """
    play = True
    #play = False
    gr.highScore()
    """
    while play != True:
        for event in P.event.get():
            if event.type == P.MOUSEBUTTONDOWN:
                play = True
    """
    # game loop - runs loopRate times a second!
    while play:  # game loop - note:  everything in this loop is indented one tab
        play = gr.WallContact(fly.x, fly.y, fly.width, fly.height)
        if play == False:
            gr.GameOver()
    
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
                print("Thanks for playing")  # notifies user the game has ended
                P.quit()   # stops the game engine
                sys.exit()  # close operating system window 
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
        P.display.flip()  # makes any changes visible on the screen
        clock.tick(loopRate)  # limits game to frame per second, FPS value
        
def gameOver(screen):
    while True:
        screen.fill((0,255,0))
        P.display.flip()
        for event in P.event.get():
            if event.type == P.QUIT:
                P.quit()
                sys.exit()

def gameStart(screen):
    while True:
        screen.fill((0,0,255))
        P.display.flip()
        for event in P.event.get():
            if event.type == P.QUIT:
                P.quit()
                sys.exit()
            elif event.type == P.MOUSEBUTTONDOWN:
                mainLoop(screen, SCREENWIDTH, SCREENHEIGHT)
# templates
def function_name(arg1, arg2, other_silly_variable=None):
    """Does something amazing.

    a much longer description of the really amazing stuff this function does and how it does it.

    Args:
        arg1: the first argument required by the function.
        arg2: the second argument required by the function.
        other_silly_variable: Another optional variable, that has a much
            longer name than the other args, and which does nothing.

    Returns:
        description of the stuff that is returned by the function.

    Raises:
        AnError: An error occurred running this function.
    """
    pass



class SampleClass(object):
    """Summary of class here.

    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam=False):
        """Inits SampleClass with blah."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Performs operation blah."""




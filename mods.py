""" Mods for the game Flippin Flys
All of the modules used within the main code, includes classes and functions
for all the characters and environments.
"""

__author__ = "Tynan Matthews"
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "tynan.matthews@education.nsw.gov.au"
__status__ = "Alpha"


""" revision notes:


"""

SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 1200, 700

#import statements for any dependencies
import pygame as P
import random as R

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

    gravity = planetGravity[planet]
    pass


class sprite:
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

    def __init__(self, x, y, vel, width, height):
        """Inits SampleClass with blah."""
        self.x = x
        self.y = y
        self.vel = vel
        self.width = width
        self.height = height

    def draw(self, screen, shape, color):
        """Draws sprite onto surface"""
        if shape == 'rect':
            P.draw.rect(screen, color, [self.x,self.y,self.width,self.height], 0)
        elif shape == 'circle':
            P.draw.circle(screen, color, [self.x, self.y, self.height], 0)
    def move(self):
        for event in P.event.get():
            if event.type == P.MOUSEBUTTONDOWN:
                Mx, My = P.mouse.get_pos()
                print(Mx)
                if Mx < (SCREENWIDTH /2) and (self.x - self.vel) > SCREENWIDTH:
                    self.x -= self.vel
                    fly.draw(screen, rectangle, blue)
                else:
                    self.x += self.vel
                    fly.draw(screen, rectangle, blue)
        



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




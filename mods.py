""" Mods for the game Flippin Flys
All of the modules used within the main code, includes classes and functions
for all the characters and environments.
"""

__author__ = "Tynan Matthews"
__license__ = "GPL"
__version__ = "0.1.1"
__email__ = "tynan.matthews@education.nsw.gov.au"
__status__ = "Beta"


SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 1200, 700

#import statements for any dependencies
import pygame as P
import random as R
import sys
import time as T

#variables and other setup
P.init()
font1 = P.font.SysFont('Arial Black', 70)
font2 = P.font.SysFont('Arial Black', 179)
scoreFont = P.font.SysFont('Arial Black', 50)
playerScore = 0

#modules
def gravity_sim(planet):
    """Simulates gravity in the environment

    Designed to hopefully create a more realistic rise and fall of the fly,
    this could also be tweaked to make the game easier or harder, it allows
    the playing on other planets feature.

    *NOT CURRENTLY IMPLEMENTED INTO GAME*
    At time of initial release it is purely used to pull Earth's gravity but
    I decided to leave it open incase of further development.

    Args:
        planet = what planet the fly is on, this will get the gravity value.

    Returns:
        The function returns the gravity present on the planet requested by
        the system in meters per second.
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

    Controls scoring, start and end of the game. As well as other small things 

    Attributes:
        score = Amount of score a player has collected in a given match
        points = 60 points = 1 score, this number can be altered to change how
                    fast or slow players gain score
        screen = the screen that objects will be displayed on
    """

    def __init__(self,screen):
        """Inits variables required to run game loop"""
        self.score = 0
        self.points = 0
        self.screen = screen

    def WallContact(self, x, y, width, height):
        """Ends game if player collides with wall"""
        gr = GameRun(self.screen)
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
            #print("enemy spawned")
            return 1            
        
    def scoring(self):
        """Updates score throughout play"""
        global playerScore
        self.points += 1
        if self.points == 60:
            self.points = 0
            self.score += 1
            playerScore = self.score
            #print(self.score)

    def highScore(self):
        """Checks previous highscore from text file, then compares this score
            with players current score to determine if new score is higher.
            It then returns this new high score."""
        global playerScore
        scoreCard = open('highScore.txt', 'r')
        prevHighScore = scoreCard.read()
        prevHighScore = int(prevHighScore)
        scoreCard.close()
        #print(self.score)
        playerScore = self.score
        if self.score > prevHighScore:
            highScore = self.score
            scoreCard = open('highScore.txt', 'w+')
            scoreCard.write(str(highScore))
            #print(highScore)
        else:
            highScore = prevHighScore
            #print(self.score)
            #print(prevHighScore)
        return highScore

def Hitbox(x, y, width, height):
    """Generates hitbox models.

    Uses the width and height a long with an objects co-ordinates to determine the borders of their rectangles.

    Args:
        x: the current x location of an object
        y: the current y location of an object
        width: how wide the object is
        height: how high the object is
        
    Returns:
        xRange: the range of x values the object is present at
        yRange: the range of y values the object is present at
    """
    xRange = []
    yRange = []
    x = int(x)
    y = int(y)
    for val in range(x, (width+x)):
        xRange.append(val)
    for val in range(y, (width+y)):
        yRange.append(val)
    return xRange, yRange

def Collide(obj1XRange, obj1YRange, obj2XRange, obj2YRange):
    """Checks for collision between two objects

    It takes the hitbox of object 1 and checks to see if it is breaching the hitbox of object 2

    Args:
        obj1XRange: range of X values object 1 is present at
        obj1XRange: range of Y values object 1 is present at
        obj2XRange: range of X values object 2 is present at
        obj2YRange: range of Y values object 2 is present at

    Returns:
        False: There is no collision between the objects
        True: The objects are colliding
    """
    #checking if they are sharing the same x co-ordinate at any time
    xCollide = False
    for val in obj1XRange:
        for i in obj2XRange:
            if i == val:
                xCollide = True
                pass
    #checking if they are sharing the same y co-ordinate at any time
    yCollide = False
    for val in obj1YRange:
        for i in obj2YRange:
            if i == val:
                yCollide = True
                pass
    #finally checking if they share both the same x and y co-ordinates at the same time
    if xCollide == True and yCollide == True:
        return True
    else:
        return False
        
class Button(P.Rect):
    """Interactable button.

    When mouse is pressed down within borders of the rectange it takes user
    do a new area of the code.

    Attributes:
        screen: screen to display the button on
        x: x location of the corner of the top left corner of the button
        y: y location of the top left corner of the button
        width: width of the button
        height: height of the button
        color: color of the button
        text: Text displayed within the button
        fill: Will the button be filled in or have a border
        
    """

    def __init__(self, screen, x, y, width, height, color, text="Button", fill=False):
        """Inits button with needed attributes"""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.screen = screen
        self.color = color
        self.text = text
        self.fill = fill

    def displayButton(self):
        """Draws button onto screen"""
        if self.fill == False:
            width = 0
        else:
            width = self.fill
        screen = self.screen
        textBox = P.draw.rect(self.screen, self.color, [self.x, self.y,self.width,self.height], width)
        displayButton = scoreFont.render(self.text, True, self.color)
        textBox.y = (SCREENHEIGHT/3 *2.3) - (self.height / 2)
        textBox.x = (SCREENWIDTH / 2) - (self.width / 2)
        screen.blit(displayButton,textBox)

    def highlight(self, obj):
        """Check if mouse click in within button boundries"""
        #print("highlight ran")
        #print(Mx)
        #print(My)
        collide = 0
        while collide == 0:
            #print("The while loop is working")
            for event in P.event.get():
                #print("The for loop is working")
                if event.type == P.QUIT:
                    P.quit()
                    sys.exit()
                elif event.type == P.MOUSEBUTTONDOWN:
                    #print("The mouse button down is working")
                    Mx, My = P.mouse.get_pos()
                    #print(Mx)
                    #print(My)
                    collide = obj.collidepoint((Mx,My))
                    #print(collide)
                    return collide

class Sprite(object):
    """Any drawn object on the screen other than text

    This class is used in the creation of both the interactable character
    and the objects that fall from the sky. It has the option to create circles
    although this isnt currently in use as it would break other elements of the
    program. It used the attributes to draw the object onto the screen as well
    as performing other features such as moveing the player and making both the
    player and enemies fall.
    
    Attributes:
        x = the x coordinate it will first appear at
        y = the y coordinate it will first appear at
        vel = the velocity it will move at
        width = how wide it is in pixels
        height = how high it is in pixels
        screen = The screen the sprite will be displayed on
        shape = the shape of given sprite, usually rect
        color = color of sprite
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
                    #print("less")
                    return -1
                else:
                    #print("more")
                    return 1
                
    def fall(self, gravity, vertAcc):
        """ Causes gravity to exist, moves sprites down"""
        self.vertAcc += gravity / 10
        self.y += gravity / 10
        self.y += self.vertAcc
        self.screen.fill((0,0,0))
        self.draw()

        
def mainLoop(screen, SCREENWIDTH, SCREENHEIGHT):
    """Controls the main loop of the game.

    This function is the playing of the actual game. Genrally this would be on the main
    code document although I wanted it to be a module so I could easily call it from the
    game over screen to play again. It calls all of the other modules in this file to create
    this wonderful game!

    Args:
        screen = the screen the game is taking place
        SCREENWIDTH = the width of the screen
        SCREENHEIGHT = the height of the screen
    """
    white = (255, 255, 255)
    black = (255, 255, 255)
    red = (255, 0, 0)
    yellow = (255, 255, 0)
    green = (0, 255, 0)
    blue = (0, 0, 0)

    fly = Sprite(555,315,25,80,80,screen, 'rect', blue) #using the sprite function to create the player character
    gravity = gravity_sim('earth') #using the gravity_sim function to set the gravity
    vertAcc = 0.0
    horAcc = 0.0
    key = 0
    enemies = [] #a list containing all active enemies at any given time
    gr = GameRun(screen) #initiates game run as gr and telling it which screen to use

    
    clock = P.time.Clock()  # creates clock to limit frames per second
    loopRate = 60  # sets max speed of main loop

    play = True
    # game loop - runs loopRate times a second!
    while play:  # game loop - note:  everything in this loop is indented one tab
        play = gr.WallContact(fly.x, fly.y, fly.width, fly.height) #play = false if player is touching wall
        flyXRange, flyYRange = Hitbox(fly.x, fly.y, fly.width, fly.height)
        global playerScore
        if play == False:
            gameOver(screen)
    
        spawn = gr.enemies()
        if spawn == 1: #creating the objects that fall
            bgX, bgY, bgWidth, bgHeight = R.randint(0,SCREENWIDTH),R.randint(-50, 0), R.randint(10, 200), R.randint(10, 200)
            badGuy = Sprite(bgX,bgY,5,bgWidth,bgHeight, screen, 'rect', (0,0,0))
            #print(badGuy.x, badGuy.y, badGuy.width, badGuy.height)
            badGuy.draw()
            enemies.append(badGuy)
            key +=1
        for i in range(0, key): #this essentially deletes any enemies not in use
            if enemies[i].y < SCREENHEIGHT:
                enemies[i].fall(gravity, 0)
                bgXRange, bgYRange = Hitbox(enemies[i].x, enemies[i].y, enemies[i].width, enemies[i].height)
                collision = Collide(bgXRange, bgYRange, flyXRange, flyYRange)
                if collision == True: #ends game if player hit by falling box
                    gr.highScore()
                    gameOver(screen)

        fly.fall(gravity, vertAcc) #makes gravity act on the player
        gr.scoring() #updates the score
        
        #slows the fly down over time
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
    
            if event.type == P.MOUSEBUTTONDOWN: #includes touching screen
                fly.vertAcc = -1.6 * gravity
                direction = fly.move(event)
                if direction == -1:
                    horAcc -= fly.vel
                else:
                    horAcc += fly.vel

        currentScore = str(playerScore)
        playScore = scoreFont.render(currentScore, True, (0,0,0))
        textBox = playScore.get_rect()
        textBox.x = (SCREENWIDTH / 2) - (textBox.width / 2)
        screen.blit(playScore,textBox)
        #print("this actually ran")
        
        P.display.flip()  # makes any changes visible on the screen
        clock.tick(loopRate)  # limits game to frame per second, FPS value
        
def gameOver(screen):
    """Controls the end of the game loop

    When the user loses this function runs, it updates the screen with all of
    the game over content, telling the user they have lost and comparing their
    score with the high score. It also allows for them to start again.

    Args:
        screen: the screen all the content is displayed on
    """
    fly = Sprite(555,315,25,80,80,screen, 'rect', (0,0,0))
    Bheight = 80
    Bwidth = 322
    rPlayButton = Button(screen, (SCREENWIDTH / 2) - (Bwidth / 2), (SCREENHEIGHT/3 *2.3) - (Bheight / 2), Bwidth, Bheight, (0,0,0), 'Play Again?', 4)
    gr = GameRun(screen)
    global playerScore
    
    #print("player score is "+ str(playerScore))

    finScore = "YOUR SCORE: " +str(playerScore)

    topScore = gr.highScore()
    topScore = "HIGHSCORE: " + str(topScore)
    while True:
        #displaying game over
        screen.fill((255,255,255))
        rPlayButton.displayButton()
        gameOver = font2.render("GAME OVER", True, (0,0,0))
        textBox = gameOver.get_rect()
        screen.blit(gameOver,textBox)
        
        #displaying high score
        displayTopScore = scoreFont.render(topScore, True, (0,0,0))
        textBox = displayTopScore.get_rect()
        textBox.y = (SCREENHEIGHT/3 *1.8) - (textBox.height / 2)
        textBox.x = (SCREENWIDTH / 2) - (textBox.width / 2)
        screen.blit(displayTopScore,textBox)

        #displaying player score
        displayPlayerScore = scoreFont.render(finScore, True, (0,0,0))
        textBox = displayPlayerScore.get_rect()
        textBox.y = (SCREENHEIGHT / 2) - (textBox.height / 2)
        textBox.x = (SCREENWIDTH / 2) - (textBox.width / 2)
        screen.blit(displayPlayerScore,textBox)
        P.display.flip()
        again = rPlayButton.highlight(rPlayButton)
        if again == 1:
            gameStart(screen,fly)
        for event in P.event.get():
            if event.type == P.QUIT:
                P.quit()
                sys.exit()

def gameStart(screen, char):
    """Controls initial display for game.

    Draws initial shapes onto the screen and provides a buffer before just
    throwing player into the game

    Args:
        screen: the screen for the content to be displayed on
        char: the character to display on the waiting screen
    """
    global playerScore
    playerScore = 0
    
    while True:
        #all of the things to display
        pressToStart = font1.render("PRESS ANYWHERE TO BEGIN...", True, (0,0,0))
        textBox = pressToStart.get_rect()
        screen.fill((255,255,255))
        char.draw()
        screen.blit(pressToStart,textBox)
        
        P.display.flip() #adds it all onto the screen

        #awaits users input before transitioning to main loop
        for event in P.event.get():
            if event.type == P.QUIT:
                P.quit()
                sys.exit()
            elif event.type == P.MOUSEBUTTONDOWN:
                mainLoop(screen, SCREENWIDTH, SCREENHEIGHT)

class LeaderBoard(object):
    """Leader Board to hold top scores and names.

    
    Attributes:
        leaders: An array of the leaders.
        leader_file: file containing the leader board data
    
    """

    def __init__(self):
        """Inits the leader doard with data from the file."""
        self.leaders = []
        try:
            leader_file = open('media\leader_board.txt', 'r')
            in_leaders = leader_file.readlines() #read the file
            leader_file.close() #always good practice to close the file ASAP
            
            for l in in_leaders:
                l = l.split(",")
                #change scores to int and strip EOL characters of names
                self.leaders.append([int(l[0]), l[1].strip()])
            # print(self.leaders)
        except FileNotFoundError:
            pass #we will create the file later

    def check(self, score): #not currently in use with current design
        #if you want this added to program consult at next meeting and it will be arranged
        """checks to see if new score makes it on leader board.
        
        Args:
        score: the first argument required by the function.

        Returns:
            True if score needs to go on leader board, or False
        """
        
        new_leader = False
        if len(self.leaders) < 10:
            new_leader = True
            
        for l in self.leaders:
            if score >= l[0]:
                new_leader = True
        
        return new_leader
        
        
    def update(self, score):
        """add a new leader and score on leader board.

        Adds a new leader to the leader board. Write the new leaderboard file
        TODO check names to see if they are nice
        
        Args:
        score: the first argument required by the function.

        Returns:
            True if score needs ot go on leader board, or false
        """
        player_name = input('Please enter your player name: ')
        banned = self.name_banned(player_name)
        while banned == True:
            player_name = input("You can't write that! Try again and be nice: ")
            banned = self.name_banned(player_name)
        
            
        self.leaders.append([score, player_name])
        self.leaders.sort(reverse=True) #sort in descending order
        if len(self.leaders) > 10:
            self.leaders.pop()

        leader_file = open('media\leader_board.txt', 'w+')
        for l in self.leaders:
            leader_file.write("{},{}\n".format(l[0], l[1]))
        leader_file.close() #always good practice to close the file ASAP


    def name_banned(self, name):
        """checks to see if name is on banned list.
        
        Args:
        name: the word to test.

        Returns:
            banned: True if word is banned, or False
        """
        
        banned = False
        banned_file = open('media\swear_words.txt', 'r')
        banned_words = banned_file.readlines()
        banned_file.close() #always good practice to close the file ASAP
        
        for b in banned_words:
            b = b.strip()
            if b in name:
                banned = True
                
        return banned


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




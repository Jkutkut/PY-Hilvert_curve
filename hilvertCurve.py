#!/usr/bin/env python3
import pygame # library to generate the graphic interface
import numpy as np # library to handle matrices
import time # to set a delay between each iteration


# -------------     FUNCTIONS      -------------

class color():
    def __init__(self):
        self.BG = (25, 25, 25)
        self.GRID = (128, 128, 128)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.DBLUE = (0, 153, 255) # L'
        self.LBLUE = (102, 255, 255) # Straight
        self.PURPLE = (153, 51, 255) # T
        self.GREEN = (102, 255, 102) #skew
        self.YELLOW = (255, 255, 102) #square
        self.ORANGE = (255, 102, 0) # L
        self.RED = (255, 80, 80) # Skew'
    def RANDOM(self):
        colorSet = dict(self.__dict__)
        for x in ["BG", "GRID", "WHITE", "BLACK"]: del colorSet[x] # Remove not wanted colors
        list = [colorSet[colorTitle] for colorTitle in [colorTitle for colorTitle in colorSet]]
        return list[np.random.randint(len(list))]

def indexToCoord(x, y, *center):
    centerc = 0 if not center else 0.5 
    return (int((x + centerc) * sizeWidth + marginFrame), int((y + centerc) * sizeWidth + marginFrame))

def getCubeCoord(x, y, *smaller): # Returns the same coordinates with the margin frame
    
    rawCoord = [ # get coord of the cornes of the square
        indexToCoord(x, y),
        indexToCoord(x + 1, y),
        indexToCoord(x + 1, y + 1),
        indexToCoord(x, y + 1)
    ]
    return rawCoord
    # return [tuple(map(lambda i: i + marginFrame, tu)) for tu in rawCoord]

def updateScreen():
    
    screen.fill(COLOR.BG) # Clean screen
    for x in range(pow(2, level)): # for each spot in the grid
        for y in range(pow(2, level)): # Draw the grid
            pygame.draw.polygon(screen, COLOR.GRID, getCubeCoord(x, y), 1) # print the grid

    # Score and level:
    # screen.blit(scoreLabel, (17.25 * sizeWidth, 5 * sizeWidth))
    # screen.blit(font.render(str(score), False, COLOR.WHITE), ((18.5 - (len(str(score))-1)/4) * sizeWidth, 6 * sizeWidth))
    hilvertCurve(level)
    pygame.display.flip() # Update the screen

def hilvertCurve(level):
    # What I know:
    # There are pow(2, level) cubes

    # if level == 1:

    for x in range(pow(2, level)):
        for y in range(pow(2, level)):
            pygame.draw.circle(screen, COLOR.ORANGE, indexToCoord(x, y, True), 5)


    # pygame.draw.circle(screen, COLOR.ORANGE, indexToCoord(pow(2, level) - 1, pow(2, level) - 1), 5)
    # pygame.draw.circle(screen, COLOR.ORANGE, indexToCoord(0, 0), 5)

# -------------     CLASSES      -------------

# -------------     CODE      -------------

pygame.init() # Init pygame
pygame.display.set_caption("Jkutkut's Tetris") # Set the title of the game

# CONSTANTS:
width = 500 
height = width
extraWidth = 0 # Some space to display the score, level, next piece...
marginFrame = 20
COLOR = color() # Get the color class with the constants
font = pygame.font.Font('freesansbold.ttf', 32) 
scoreLabel = font.render('Score:', False, COLOR.WHITE) 
levelLabel = font.render('Level:', False, COLOR.WHITE) 


# Variables:
level = 1
sizeWidth = width / pow(2, level)
screen = pygame.display.set_mode((width + extraWidth + 2 * marginFrame, height + 2 * marginFrame)) # Set the size of the window

lastGameTick = time.process_time() # store when we started (updates the screen)
lastKeyTick = time.process_time() # (updates the keys pressed to enable hold controls)
gameRunning = True # If false, the game stops
# running = True

# keys = {"up": 0, "down": 0, "right": 0, "left": 0} # 0 = key up, > 0 => Key down
while gameRunning:
    # if time.process_time() - lastGameTick > 0.25 - level/100: # Update the screen but game ticks every some period 
    #     lastGameTick = time.process_time() # Update current game tick
    sizeWidth = width / pow(2, level)
    for event in pygame.event.get(): # for each event
        if event.type == pygame.QUIT: # if quit btn pressed
            gameRunning = False # no longer running game
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == 32: # Space pressed
                level = level + 1
            # elif event.key == 273 or event.key == 119: # Arrow up
            # elif event.key == 274 or event.key == 115: # Arrow down
            # elif event.key == 275 or event.key == 100: # Arrow right
            # elif event.key == 276 or event.key == 97: # Arrow left
            # print(event.key)
    updateScreen()

print("Thanks for playing, I hope you liked it.")
print("See more projects like this one on https://github.com/jkutkut/")
pygame.quit() # End the pygame
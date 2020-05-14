#!/usr/bin/env python3
import pygame # library to generate the graphic interface
import time # to set a delay between each iteration

# -------------     FUNCTIONS      -------------
def indexToCoord(p): 
    return ((p[0] + 0.5) * sizeWidth + marginFrame, (p[1] + 0.5) * sizeWidth + marginFrame)

def hilvert(i):
    vec = [[0, 0], [0, 1], [1, 1], [1, 0]]
    index = i & 3
    v = [vec[index][0], vec[index][1]]
    for l in range(1, level, 1):
        i = i >> 2
        index = i & 3
        len = pow(2, l)
        if index == 0:
            temp = v[0]
            v[0] = v[1]
            v[1] = temp
        elif index == 3:
            temp = len - 1 - v[0]
            v[0] = len - 1 - v[1]
            v[1] = temp
        v[0] = v[0] + len * vec[index][0]
        v[1] = v[1] + len * vec[index][1]
    return v


# -------------     CODE      -------------

pygame.init() # Init pygame
pygame.display.set_caption("Jkutkut's Hilbert Curves") # Set the title of the game

# CONSTANTS:
level = 6
width = 1024
marginFrame = 20
gameRunning = True # If false, the current game stops
running = True # if false, the program stops
lastGameTick = time.process_time() # store when we started (updates the screen)


screen = pygame.display.set_mode((width + 2 * marginFrame, width + 2 * marginFrame)) # Set the size of the window
while running:
    level = level + 1
    screen.fill((25, 25, 25)) # Clean screen
    N = pow(2, level)
    sizeWidth = int(width / N)
    path = [hilvert(i) for i in range(N * N)]
    p = 0
    gameRunning = True
    while gameRunning:
        if time.process_time() - lastGameTick > 0.001: # Update the screen but game ticks every some period 
            lastGameTick = time.process_time() # Update current game tick
            pygame.draw.line(screen, (102, 255, 102), indexToCoord(path[p]), indexToCoord(path[p + 1]), 1)
            p = p + 1
            pygame.display.flip() # Update the screen
            if(p == len(path) - 1):
                gameRunning = False
        
        for event in pygame.event.get(): # for each event
            if event.type == pygame.QUIT: # if quit btn pressed
                gameRunning = False # no longer running game
                running = False

print("Thanks for playing, I hope you liked it.")
print("See more projects like this one on https://github.com/jkutkut/")
pygame.quit() # End the pygame
__author__ = 'Kshitij Sharma'
# Module to detect Joypad

import pygame.display
import Globals
import os
import string

pygame.display.init()

# Creating display
display = pygame.display.set_mode((400,400))
pygame.display.set_caption("Key Codes")

char = 0
# keys = ['0','DOWN','LEFT','RIGHT']

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == 27:
                done = True
                break
            print " case "+ str(event.key) +" : "
            print "    robot.keyPress(EventKey.VK_"+str(char)+");"
            print "    robot.delay(10);"
            print "    robot.keyRelease(EventKey.VK_"+str(char)+");"
            print "    break;"
            char = char + 1

    pygame.time.delay(100)

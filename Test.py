__author__ = 'Kshitij Sharma'
# Module to detect Joypad

import pygame.display
import pygame.joystick

import os

pygame.display.init()
pygame.joystick.init()

print "Detecting Joystick..."

while(pygame.joystick.get_count() == 0):
    pygame.joystick.quit()
    pygame.time.delay(1000)
    pygame.joystick.init()
    print ".",

print " :)"
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print "Joystick connected : ",joysticks[0].get_name()
joysticks[0].init()

# Creating display
display = pygame.display.set_mode((400,400))
pygame.display.set_caption("Joystick to Keyboard Mapper")

done = False

print "get_numaxes() = ", joysticks[0].get_numaxes()
print "get_numballs() = ", joysticks[0].get_numballs()
print "get_numbuttons() = ", joysticks[0].get_numbuttons()
print "get_numhats() = ", joysticks[0].get_numhats()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # joysticks[0].get_hat(0);
    b1 = joysticks[0].get_button(0)
    b2 = joysticks[0].get_button(1)
    b3 = joysticks[0].get_button(2)
    b4 = joysticks[0].get_button(3)
    b5 = joysticks[0].get_button(4)
    b6 = joysticks[0].get_button(5)
    b7 = joysticks[0].get_button(6)
    b8 = joysticks[0].get_button(7)
    b9 = joysticks[0].get_button(8)
    b10 = joysticks[0].get_button(9)
    b11 = joysticks[0].get_button(10)
    b12 = joysticks[0].get_button(11)

    print "Yes 1 ? = ", b1
    print "Yes 2 ? = ", b2
    print "Yes 3 ? = ", b3
    print "Yes 4 ? = ", b4
    print "Yes 5 ? = ", b5
    print "Yes 6 ? = ", b6
    print "Yes 7 ? = ", b7
    print "Yes 8 ? = ", b8
    print "Yes 9 ? = ", b9
    print "Yes 10 ? = ", b10
    print "Yes 11 ? = ", b11
    print "Yes 12 ? = ", b12

    pygame.time.delay(100)

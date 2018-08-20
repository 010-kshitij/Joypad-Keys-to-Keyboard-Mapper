__author__ = 'Kshitij Sharma'

import pygame
import os

import Globals

class MappingStarter:
    def __init__(self):
        # Initializing Window
        self.window = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("Start Mapping Joypad Keys")

        #Joypad Object
        self.joypad = pygame.joystick
        self.joypad.init()
        self.joystick = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        self.joystick[0].init()

    def run(self):
        done = False
        while not done:
            self.window.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                if event.type == pygame.JOYBUTTONDOWN:
                    terminalCommand = "java Keypress Press " + str(Globals.data[Globals.joypadKey[event.dict['button']]])
                    os.system(terminalCommand)

                if event.type == pygame.JOYBUTTONUP:
                    terminalCommand = "java Keypress Release " + str(Globals.data[Globals.joypadKey[event.dict['button']]])
                    os.system(terminalCommand)

                if event.type == pygame.JOYAXISMOTION:
                    if event.dict['axis'] == 2 and event.dict['value'] < 0:
                        terminalCommand = "java Keypress Press " + str(Globals.data['KEY_J22'])
                        os.system(terminalCommand)
                    if event.dict['axis'] == 2 and event.dict['value'] > 0:
                        terminalCommand = "java Keypress Press " + str(Globals.data['KEY_J20'])
                        os.system(terminalCommand)
                    if event.dict['axis'] == 0 and event.dict['value'] < 0:
                        terminalCommand = "java Keypress Press " + str(Globals.data['KEY_J18'])
                        os.system(terminalCommand)
                    if event.dict['axis'] == 0 and event.dict['value'] > 0:
                        terminalCommand = "java Keypress Press " + str(Globals.data['KEY_J16'])
                        os.system(terminalCommand)
                    if event.dict['axis'] == 1 and event.dict['value'] < 0:
                        terminalCommand = "java Keypress Press " + str(Globals.data['KEY_J15'])
                        os.system(terminalCommand)
                    if event.dict['axis'] == 1 and event.dict['value'] > 0:
                        terminalCommand = "java Keypress Press " + str(Globals.data['KEY_J17'])
                        os.system(terminalCommand)
                    if event.dict['axis'] == 3 and event.dict['value'] < 0:
                        terminalCommand = "java Keypress Press " + str(Globals.data['KEY_J21'])
                        os.system(terminalCommand)
                    if event.dict['axis'] == 3 and event.dict['value'] > 0:
                        terminalCommand = "java Keypress Press " + str(Globals.data['KEY_J19'])
                        os.system(terminalCommand)
                if event.type == pygame.JOYHATMOTION:
                    if event.dict['value'][0] == 0 and event.dict['value'][1] == 1:
                        terminalCommand = "java Keypress Press " + str(Globals.data['KEY_J11'])
                        os.system(terminalCommand)
                        pygame.time.delay(20);
                        terminalCommand = "java Keypress Release " + str(Globals.data['KEY_J11'])
                        os.system(terminalCommand)
                    if event.dict['value'][0] == 0 and event.dict['value'][1] == -1:
                        terminalCommand = "java Keypress Press " + str(Globals.data['KEY_J13'])
                        os.system(terminalCommand)
                        pygame.time.delay(20);
                        terminalCommand = "java Keypress Release " + str(Globals.data['KEY_J13'])
                        os.system(terminalCommand)
                    if event.dict['value'][0] == 1 and event.dict['value'][1] == 0:
                        terminalCommand = "java Keypress Press " + str(Globals.data['KEY_J12'])
                        os.system(terminalCommand)
                        pygame.time.delay(20);
                        terminalCommand = "java Keypress Release " + str(Globals.data['KEY_J12'])
                        os.system(terminalCommand)
                    if event.dict['value'][0] == -1 and event.dict['value'][1] == 0:
                        terminalCommand = "java Keypress Press " + str(Globals.data['KEY_J14'])
                        os.system(terminalCommand)
                        pygame.time.delay(20);
                        terminalCommand = "java Keypress Release " + str(Globals.data['KEY_J14'])
                        os.system(terminalCommand)


            pygame.display.flip()
            pygame.time.Clock().tick(60)

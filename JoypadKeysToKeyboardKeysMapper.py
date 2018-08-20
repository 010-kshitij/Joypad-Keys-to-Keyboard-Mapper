__author__ = 'Kshitij Sharma'

import pygame

import Globals
import JoypadDetector
import KeyAssigner
import MappingStarter

class Main:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("Joypad Keys To Keyboard Keys Mapper")

        # Initializing fonts
        pygame.font.init()
        self.fontHeading = pygame.font.Font(None, 30)

        # Initializing Option Chooser variable which will store the Option number chosen by the user,
        # 0 means, no option chosen.
        self.optionChosen = 0

    def run(self):
        done = False
        while not done:
            self.window.fill((255, 255, 255))

            # Stuffs that are being displayed on the screen
            self.window.blit(self.fontHeading.render("Joypad Keys to Keyboard Keys Mapper", True, (0, 0, 0)), (5, 20))
            self.window.blit(Globals.joypadDetector.joypadImage, (125, 50))
            self.window.blit(self.fontHeading.render("------------", True, (0, 0, 0)), (160, 210))
            self.window.blit(self.fontHeading.render("Options", True, (0, 0, 0)), (160, 250))
            self.window.blit(self.fontHeading.render("1. Assign Keys", True, (0, 0, 0)), (125, 290))
            self.window.blit(self.fontHeading.render("2. Start Mapper", True, (0, 0, 0)), (120, 330))
            self.window.blit(self.fontHeading.render("Press corresponding key to choose", True, (0, 0, 0)), (30, 370))
            # End Stuffs that are being displayed on the screen

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        # To assign keys to joypad buttons
                        self.optionChosen = 1
                        done = True
                    if event.key == pygame.K_2:
                        # To Start mapping
                        self.optionChosen = 2
                        done = True

            pygame.display.flip()


# Main
if not Globals.isJoypadConnected:
    Globals.joypadDetector = JoypadDetector.JoypadDetector()
    Globals.joypadDetector.run()

if Globals.isJoypadConnected:
    Globals.main = Main()
    Globals.main.run()

if Globals.main.optionChosen == 1:
    Globals.keyAssigner = KeyAssigner.KeyAssigner()
    Globals.keyAssigner.run()
    Globals.main.run()

if Globals.main.optionChosen == 2:
    Globals.mappingStarter = MappingStarter.MappingStarter()
    Globals.mappingStarter.run()

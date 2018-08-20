__author__ = 'Kshitij Sharma'

import pygame

import Globals


class KeyAssigner:
    def __init__(self):
        # Initializing Window
        self.window = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("Assign Keyboard Keys to Joypad")

        # Initializing fonts
        pygame.font.init()
        self.fontHeading = pygame.font.Font(None, 15)

    def run(self):
        done = False
        index = 0
        while not done:
            if index == 24:
                break
            self.window.fill((255, 255, 255))

            # Stuff for all processing
            self.window.blit(
                self.fontHeading.render("Press a Key to assign the indicated Joypad Button", True, (0, 0, 0)), (5, 20))
            joypadImage = pygame.image.load(Globals.joypadImage[index])
            self.window.blit(joypadImage, (0, 50))
            # End Stuff for all processing

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    Globals.data[Globals.joypadKey[index]] = event.key
                    index += 1
                    if index == 24:
                        done = True

            pygame.display.flip()
            pygame.time.Clock().tick(10)

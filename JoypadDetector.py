__author__ = 'Kshitij Sharma'

import pygame

import Globals


class JoypadDetector:
    """ Class that detects Joypad and then proceeds further """

    def __init__(self):
        # Initializing Window
        self.window = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("Detecting Joypad")

        # Initializing Fonts
        pygame.font.init()
        self.fontDetectingJoypad = pygame.font.Font(None, 30)

        self.joypadImage = pygame.image.load("g3.png")
        self.joypad = pygame.joystick
        self.joypad.init()

    def run(self):
        done = False
        times = 1
        waitDotsText = ". "
        while not done:
            self.window.fill((255, 255, 255))
            self.window.blit(self.joypadImage, (125, 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            times += 1
            if times == 18:
                times = 1
            numberOfJoypads = self.joypad.get_count()
            if numberOfJoypads == 0:
                self.joypad.quit()
                Globals.isJoypadConnected = False
                self.joypad.init()
                self.window.blit(self.fontDetectingJoypad.render("Detecting Joypad", True, (0, 0, 0)), (110, 250))
                self.window.blit(self.fontDetectingJoypad.render(waitDotsText*times, True, (0, 0, 0)), (110, 300))
            else:
                self.window.blit(self.fontDetectingJoypad.render("Joypad Detected", True, (0, 0, 0)), (110, 250))
                Globals.isJoypadConnected = True
                done = True
                pygame.time.wait(2000)

            pygame.display.flip()
            pygame.time.Clock().tick(10)

# import the pygame module
import pygame
import os

class Gui:
    def __init__(self, screen_x, screen_y, caption):
        self.screenX = screen_x
        self.screenY = screen_y
        pygame.display.set_caption(caption)

        self.screen = pygame.display.set_mode((self.screenX,self.screenY),pygame.FULLSCREEN | pygame.SCALED)
        self.screen.fill((244,222,222))

    def update_screen(self):
        pygame.display.flip()

    def return_screen(self):
        return self.screen

    def draw_line(self, screen, COLOR, POS, ENDPOS, THICKNESS):

        pygame.draw.line(screen,COLOR,POS,ENDPOS,THICKNESS)


# import the pygame module
import pygame
import os

class Gui:
    def __init__(self,SCREEN_X,SCREEN_Y,Caption):
        self.screenX = SCREEN_X
        self.screenY = SCREEN_Y

        pygame.display.set_caption(Caption)

        self.screen = pygame.display.set_mode((self.screenX,self.screenY))
        self.screen.fill((244,222,222))

    def updatescreen(self):
        pygame.display.flip()

    def returnscreen(self):
        return self.screen

    def drawline(self,screen,COLOR,POS,ENDPOS,THICKNESS):

        pygame.draw.line(screen,COLOR,POS,ENDPOS,THICKNESS)


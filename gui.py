# import the pygame module
import pygame
import os

class Gui:
    def __init__(self, screen_x, screen_y, caption):
        """
        Creates a screen instance.
        :param screen_x: Width of screen
        :type screen_x: int
        :param screen_y: Height of screen
        :type screen_y: int
        :param caption: Title of screen
        :type caption: string
        """
        self.screenX = screen_x
        self.screenY = screen_y
        pygame.display.set_caption(caption)

        self.screen = pygame.display.set_mode((self.screenX,self.screenY),pygame.FULLSCREEN | pygame.SCALED)
        self.screen.fill((244,222,222))

    def update_screen(self):
        """
        updates frame of screen.
        :return:
        :rtype:
        """
        pygame.display.flip()

    def return_screen(self):
        """
        returns the screen.
        :return: screen
        :rtype: screen
        """
        return self.screen

    def draw_line(self, screen, COLOR, POS, ENDPOS, THICKNESS):
        """
        Draws the line in the middle of screen.
        :param screen: The screen of the game
        :type screen: screen
        :param COLOR: Color of line
        :type COLOR: list
        :param POS: Start position of line
        :type POS: int
        :param ENDPOS: End position of line
        :type ENDPOS: int
        :param THICKNESS: Thickness of line
        :type THICKNESS: int
        :return: None
        :rtype: None
        """

        pygame.draw.line(screen,COLOR,POS,ENDPOS,THICKNESS)


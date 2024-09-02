import pygame.font


class TextManager:

    def __init__(self,screen):
        """
        Creates an instance of TextManager
        :param screen: Window of the game
        :type screen: screen
        """
        pygame.font.init()
        # Loads the font
        self.my_font = pygame.font.SysFont('Arial',25)
        self.screen = screen

    def create_label(self, label, COLOR, x, y):
        """
        Creates a label
        :param label: Text of the label
        :type label: str
        :param COLOR: Color of the label
        :type COLOR: List
        :param x: X position of the label
        :type x: int
        :param y: Y position of the label
        :type y: int
        :return: None
        :rtype: None
        """
        self.text_surface = self.my_font.render(label,False,COLOR)
        self.screen.blit(self.text_surface, (x,y))

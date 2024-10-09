import pygame.font


class TextManager:
    """
    Manages text rendering in the game.

    Attributes:
        screen (Surface): The Pygame surface representing the game window where text is displayed.
        my_font (Font): The font object used to render text.
   """

    def __init__(self, screen):
        """
        Initialize TextManager instance
        :param screen: Screen of game
        :type screen: Screen
        """

        pygame.font.init()
        # Loads the font
        self.my_font = pygame.font.SysFont('Arial', 25)
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
        text_surface = self.my_font.render(label, False, COLOR)
        self.screen.blit(text_surface, (x, y))

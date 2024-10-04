import pygame


class Gui:
    """
    Create a GUI for the game.

    This class is responsible for initializing the game window and handling
    various GUI-related functionalities, including drawing elements on the screen.

    Attributes:
        screenX (int): Width of the screen.
        screenY (int): Height of the screen.
        screen (Surface): The Pygame surface representing the game screen.
        black (tuple): RGB value for the color black used in the game.
    """

    def __init__(self, screen_x, screen_y, caption):
        """
        Initializes the GUI with the specified screen dimensions and caption.

        This method sets up the game window with the provided width, height,
        and title.

        :param screen_x: Width of screen.
        :type screen_x: int
        :param screen_y: Height of screen.
        :type screen_y: int
        :param caption: Title of screen.
        :type caption: str
        :return: None
        :rtype: None
        """
        self.screenX = screen_x
        self.screenY = screen_y
        pygame.display.set_caption(caption)

        self.screen = pygame.display.set_mode((self.screenX, self.screenY), pygame.FULLSCREEN | pygame.SCALED)
        self.screen.fill((244, 222, 222))
        self.black = (0, 0, 0)

    def update_screen(self):
        """
        Updates the frame of the screen.

        This method refreshes the display to show any changes made.

        :return: None
        :rtype: None
        """
        pygame.display.flip()

    def return_screen(self):
        """
        Returns the Pygame screen surface.

        This method allows access to the screen surface for additional drawing
        operations outside the Gui class.

        :return: Pygame screen surface.
        :rtype: Surface
        """
        return self.screen

    def draw_line(self, screen, color, pos, endpos, thickness):
        """
        Draws a line on the specified screen.

        This method renders a line between two points with the specified color
        and thickness.

        :param screen: The screen on which to draw the line.
        :type screen: Surface
        :param color: Color of the line in RGB format.
        :type color: tuple
        :param pos: Start position of the line (x, y).
        :type pos: tuple
        :param endpos: End position of the line (x, y).
        :type endpos: tuple
        :param thickness: Thickness of the line.
        :type thickness: int
        :return: None
        :rtype: None
        """
        pygame.draw.line(screen, color, pos, endpos, thickness)

    def cover_left_side(self, screen):
        """
        Covers the left side of the screen with a rectangle.

        This method draws a black rectangle over the left half of the screen.

        :param screen: The screen to cover.
        :type screen: Surface
        :return: None
        :rtype: None
        """
        pygame.draw.rect(screen, self.black, (0, 0, self.screenX // 2, self.screenY))

    def cover_right_side(self, screen):
        """
        Covers the right side of the screen with a rectangle.

        This method draws a black rectangle over the right half of the screen.

        :param screen: The screen to cover.
        :type screen: Surface
        :return: None
        :rtype: None
        """
        pygame.draw.rect(screen, self.black, (self.screenX // 2, 0, self.screenX // 2, self.screenY))

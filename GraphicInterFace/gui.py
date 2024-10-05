import pygame

from GraphicInterFace.imagemanager import ImageManager
from GraphicInterFace.textmanager import TextManager


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
        self.text_manager = TextManager(self.screen)
        self.image_manager = ImageManager()

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
        operations outside the GraphicInterFace class.

        :return: Pygame screen surface.
        :rtype: Surface
        """
        return self.screen

    def draw_line(self,color, pos, endpos, thickness):
        """
        Draws a line on the specified screen.

        This method renders a line between two points with the specified color
        and thickness.

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
        pygame.draw.line(self.screen, color, pos, endpos, thickness)

    def cover_left_side(self):
        """
        Covers the left side of the screen with a rectangle.

        This method draws a black rectangle over the left half of the screen.
        """

        pygame.draw.rect(self.screen, self.black, (0, 0, self.screenX // 2, self.screenY))


    def cover_right_side(self):
        """
        Covers the right side of the screen with a rectangle.

        This method draws a black rectangle over the right half of the screen.

        :param screen: The screen to cover.
        :type screen: Surface
        :return: None
        :rtype: None
        """
        pygame.draw.rect(self.screen, self.black, (self.screenX // 2, 0, self.screenX // 2, self.screenY))

    def create_label(self, text, color, x, y):
        """
       Creates a label
       :param text: Text of the label
       :type textl: str
       :param color: Color of the label
       :type color: List
       :param x: X position of the label
       :type x: int
       :param y: Y position of the label
       :type y: int
       :return: None
       :rtype: None
       """
        self.text_manager.create_label(text, color, x, y)

    def draw_image(self, image, x, y):
        """
        Draws the specified image on the screen.
        :param image: Image to be drawn
        :type image: pygame.Surface
        :param x: the x coordinate
        :type x: int
        :param y: the y coordinate
        :type y: int
        :return: None
        :rtype: None
        """
        self.image_manager.blit_image(self.screen, (x, y), image)

    def load_image(self, name):
        """
        Loads the image up
        :param name: Path to image
        :type name: str
        :return: None
        :rtype: None
        """
        self.image_manager.load_image(name)

    def return_images(self):
        """
        Returns an array with all images
        :return: All images
        :rtype: list
        """
        return self.image_manager.return_list()

    def return_last_image(self):
        """
        Returns the last image
        :return: Last image
        :rtype: pygame.Surface
        """
        return self.image_manager.return_last_image()

    def resize_image(self, image, width, height):
        """
        Resizes the given image
        :param image: Image to resize
        :type image: pygame.Surface
        :param width: New width of image
        :type width: int
        :param height: New height of image
        :type height: int
        :return: New resized image
        :rtype: pygame.Surface
        """
        return self.image_manager.resize_image(width, height, image)

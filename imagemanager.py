import os.path
import pygame.image


class ImageManager:
    """
    Manage images for the game.

    This class handles loading, resizing, and drawing images on the game screen.
    It maintains a list of images for easy access and management.

    Attributes:
        image_array (list): A list containing all loaded images.
        image (Surface): The last loaded image.
    """

    def __init__(self):
        """
        Initializes the ImageManager with an empty image list.

        This method sets up the image array to store images that will be loaded.

        :return: None
        :rtype: None
        """
        self.image_array = []
        self.image = None

    def load_image(self, name):
        """
        Loads an image and adds it to the list of images.

        This method retrieves the image from the specified path and stores
        it for future use.

        :param name: Name of the image file to load.
        :type name: str
        :return: None
        :rtype: None
        """
        image_path = os.path.join("assets", name)
        image = pygame.image.load(image_path)
        self.image = image
        self.image_array.append(image)

    def return_list(self):
        """
        Returns the list of all loaded images.

        This method provides access to the array of images stored in the manager.

        :return: List of images.
        :rtype: list
        """
        return self.image_array

    def return_last_image(self):
        """
        Returns the last loaded image.

        This method retrieves the most recently loaded image from the image array.

        :return: Last image in the list.
        :rtype: Surface
        """
        return self.image_array[-1]

    def blit_image(self, screen, position, image):
        """
        Draws the specified image on the screen at the given position.

        This method blits the image onto the game window at the provided (x, y) coordinates.

        :param screen: The game window surface where the image will be drawn.
        :type screen: Surface
        :param position: The (x, y) coordinates where the image will be placed.
        :type position: tuple
        :param image: The image to be drawn.
        :type image: Surface
        :return: None
        :rtype: None
        """
        screen.blit(image, position)

    def resize_image(self, width, height, image):
        """
        Resizes the specified image to new dimensions.

        This method scales the given image to the provided width and height.

        :param width: New width for the image.
        :type width: int
        :param height: New height for the image.
        :type height: int
        :param image: The image to be resized.
        :type image: Surface
        :return: Resized image.
        :rtype: Surface
        """
        return pygame.transform.scale(image, (width, height))

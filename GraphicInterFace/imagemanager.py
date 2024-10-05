import os
import pygame


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
        """
        self.image_array = []
        self.image = None
        # Set the assets path based on the current file's directory
        self.assets_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets')

    def load_image(self, name):
        """
        Loads an image and adds it to the list of images.

        :param name: Name of the image file to load.
        :type name: str
        """
        image_path = os.path.join(self.assets_path, name)
        try:
            # Load the image
            image = pygame.image.load(image_path)
            self.image = image
            self.image_array.append(image)
        except pygame.error as e:
            print(f"Unable to load image at {image_path}: {e}")

    def return_list(self):
        """
        Returns the list of all loaded images.

        :return: List of images.
        :rtype: list
        """
        return self.image_array

    def return_last_image(self):
        """
        Returns the last loaded image.

        :return: Last image in the list or None if no images have been loaded.
        :rtype: Surface or None
        """
        if self.image_array:
            return self.image_array[-1]
        return None

    def blit_image(self, screen, position, image):
        """
        Draws the specified image on the screen at the given position.

        :param screen: The game window surface where the image will be drawn.
        :type screen: Surface
        :param position: The (x, y) coordinates where the image will be placed.
        :type position: tuple
        :param image: The image to be drawn.
        :type image: Surface
        """
        screen.blit(image, position)

    def resize_image(self, width, height, image):
        """
        Resizes the specified image to new dimensions.

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

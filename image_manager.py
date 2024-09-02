import os.path

import pygame.image


class Image_Manager:

    def __init__(self):
        """
        Creates a list with all images to be used.
        """
        self.image_array = []

    def load_image(self,name):
        """
        Loads the image for further usage.
        :param name: Name of image
        :type name: string
        :return: None
        :rtype: None
        """
        image_path = os.path.join("assets", name)
        image = pygame.image.load(image_path)
        self.image = image
        self.image_array.append(image)

    def return_list(self):
        """
        Returns list with all images.
        :return: List of images
        :rtype: list
        """
        return self.image_array

    def return_last_image(self):
        """
        Returns the last image in the list.
        :return: Last image
        :rtype: image
        """
        return self.image_array[-1]

    def blit_image(self,screen,position,image):
        """
        Draws the image on the screen.
        :param screen: Window of game
        :type screen: screen
        :param position: Position of image
        :type position: list with (x,y)
        :param image: Image to be drawn
        :type image: image
        :return: None
        :rtype: None
        """
        screen.blit(image,position)
    def resize_image(self,width,height,image):
        """
        Resizes the image.
        :param width: New width of image
        :type width: int
        :param height: New height of image
        :type height: int
        :param image: Image to be resized
        :type image: image
        :return: None
        :rtype: None
        """
        pygame.transform.scale(image,(width,height))















import os.path

import pygame.image


class Image_Manager:
    def __init__(self):
        self.image_array = []

    def load_image(self,name):
        image_path = os.path.join("assets", name)
        image = pygame.image.load(image_path)
        self.image = image
        self.image_array.append(image)

    def return_list(self):
        return self.image_array

    def return_last_image(self):
        return self.image_array[-1]

    def blit_image(self,screen,position,image):
        screen.blit(image,position)
    def resize_image(self,width,height,image):
        pygame.transform.scale(image,(width,height))















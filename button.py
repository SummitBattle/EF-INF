# Imports
import pygame

# Configuration
pygame.init()


class Button():


    def __init__(self,screen, x, y, width, height, onclickFunction=None, onePress=False):
        """
        Initializes a new Button instance
        :param screen: The window of the game
        :type screen: screen
        :param x: The X position of the button
        :type x: int
        :param y: The Y position of the button
        :type y: int
        :param width: The Width of the button
        :type width: int
        :param height: The height of the button
        :type height: int
        :param onclickFunction: Function to be called when button is pressed
        :type onclickFunction: function
        :param onePress: Allow multiple presses or not
        :type onePress: bool
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.shipsplaced = False
        self.pressedbutton = False


        self.fillColors = {
            'normal': '#00aaaa',
            'hover': '#00ffff',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)



        self.alreadyPressed = False




    def process(self):
        """
        Collects the button state (normal,hover,pressed) and calls function when pressed
        :return: None
        :rtype: None
        """

        mousePos = pygame.mouse.get_pos()

        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])



                if self.onePress:
                    self.shipsplaced = True

                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False




        self.screen.blit(self.buttonSurface, self.buttonRect)





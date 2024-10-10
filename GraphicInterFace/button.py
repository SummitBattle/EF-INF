import pygame

# Configuration
pygame.init()

class Button:
    """
    A class representing a clickable button in the Pygame window.

    Attributes:
        screen (pygame.Surface): The screen surface where the button will be rendered.
        x (int): The x-coordinate of the button.
        y (int): The y-coordinate of the button.
        width (int): The width of the button.
        height (int): The height of the button.
        onclickFunction (function): The function to be executed when the button is clicked.
        ships_placed (bool): Indicates if ships have been placed, used for specific game logic.
        fillColors (dict): Dictionary holding colors for normal, hover, and pressed states.
        buttonSurface (pygame.Surface): The surface representing the button's visual display.
        buttonRect (pygame.Rect): The rectangle representing the button's position and size.
        is_pressed (bool): Tracks if the mouse button is currently pressed.
    """

    def __init__(self, screen, x, y, width, height, onclickFunction=None):
        """
        Initialize a new Button instance.

        Args:
            screen (pygame.Surface): The surface where the button will be displayed.
            x (int): The x-coordinate for the button's position.
            y (int): The y-coordinate for the button's position.
            width (int): The width of the button.
            height (int): The height of the button.
            onclickFunction (function): The function to be called when the button is clicked.
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.ships_placed = False
        self.fillColors = {
            'normal': '#00aaaa',
            'hover': '#00ffff',
            'pressed': '#333333',
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_pressed = False
    def process(self):
        """
        Update the button state based on user input and call the associated function if the button is clicked.

        This method changes the button's visual state (normal, hover, pressed) based on mouse interactions,
        and triggers the onclickFunction if the button is clicked and released.

        Returns:
            None
        """
        mousePos = pygame.mouse.get_pos()

        # Default state
        self.buttonSurface.fill(self.fillColors['normal'])

        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                # Mouse button is pressed down
                if not self.is_pressed:
                    self.is_pressed = True
                    self.buttonSurface.fill(self.fillColors['pressed'])

            elif self.is_pressed:
                # Mouse button is released after being pressed
                self.is_pressed = False
                self.onclickFunction()

        # Render the button on the screen
        self.screen.blit(self.buttonSurface, self.buttonRect)

class GameConfig:
    """
    Configuration settings for the game.

    This class encapsulates all constants and settings related to the game's
    dimensions, color schemes, and user interface.

    Attributes:
        SCREEN_X (int): The width of the game screen.
        SCREEN_Y (int): The height of the game screen.
        BLOCK_SIZE (int): The size of the blocks in the game grid.
        SMALLER_BLOCK_SIZE (int): The size of smaller grid blocks.
        CAPTION (str): The title displayed on the game window.
        WHITE (tuple): RGB value for the color white used in the game.
        LINE_THICKNESS (int): The thickness of the grid lines.
        GREEN (tuple): RGB value for the color green.
        CUSTOM_BUTTON_X (int): X-coordinate for the custom button placement.
        CUSTOM_BUTTON_Y (int): Y-coordinate for the custom button placement.
        CUSTOM_BUTTON_WIDTH (int): The width of the custom button.
        CUSTOM_BUTTON_HEIGHT (int): The height of the custom button.
    """

    def __init__(self):
        """
        Initializes the GameConfig with default settings.

        This method sets the dimensions of the game screen, the size of
        the blocks in the grid, color values, and the button dimensions.

        :return: None
        :rtype: None
        """
        self.SCREEN_X = 1300
        self.SCREEN_Y = 700
        self.BLOCK_SIZE = 30
        self.SMALLER_BLOCK_SIZE = 10
        self.CAPTION = "Battleship"
        self.WHITE = (255, 255, 255)
        self.LINE_THICKNESS = 30
        self.GREEN = (0, 255, 0)
        self.CUSTOM_BUTTON_X = self.SCREEN_X / 2
        self.CUSTOM_BUTTON_Y = 500
        self.CUSTOM_BUTTON_WIDTH = 50
        self.CUSTOM_BUTTON_HEIGHT = 200

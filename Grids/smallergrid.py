import pygame


class SmallerGrid:
    """
    Represents a smaller grid in the Battleship game.

    Attributes:
       rect (Rect or None): Pygame rectangle representing the current cell being processed.
       block_size (int): Size of each cell in the grid.
       screen (Surface): The window of the game where the grid is drawn.
       num_rows (int): Number of rows in the grid.
       num_cols (int): Number of columns in the grid.
       grid_rects (list): List to hold rectangles representing each cell in the grid.
       grid_state (list of lists): 2D list representing the state of each cell in the grid.
       colors (dict): A dictionary holding the colors used for different cell states.
    """
    def __init__(self, block_size, screen):
        """
        Initialize an instance of Smaller grid.
        :param block_size: Size of each cell
        :type block_size: int
        :param screen: The window of the game
        :type screen: screen
        """
        self.rect = None
        self.block_size = block_size
        self.screen = screen
        self.num_rows = 10  # Number of rows
        self.num_cols = 10  # Number of columns
        self.grid_rects = []  # List to hold grid rectangles
        self.grid_state = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        # Define colors for different states
        self.colors = {
            0: (0, 255, 255, 128),  # Empty (light blue, semi-transparent)
            1: (0, 0, 255, 128),  # Occupied (blue, semi-transparent)
            2: (255, 0, 0, 128),  # Miss (red, semi-transparent)
            3: (0, 255, 0, 128),  # Hit (green)
            4: (0, 0, 0, 128),  # Selected (black, semi-transparent)
            5: (0, 255, 255, 255)  # Hovering (light blue, fully visible)
        }

    def set_cell_state(self, row, col, state):
        """
        Set the state of a cell.
        :param row: Row of grid to be changed
        :type row: int
        :param col: Column of grid to be changed
        :type col: int
        :param state: State to change into
        :type state: int
        :return: None
        :rtype: None
        """

        if 0 <= row < self.num_rows and 0 <= col < self.num_cols:
            self.grid_state[row][col] = state

    def draw_grid(self, grid_x, grid_y):
        """
        Draw the smaller grid. Color is based on the state.
        :param grid_x: X position of the grid
        :type grid_x: int
        :param grid_y: Y position of the grid
        :type grid_y: int
        :return: None
        :rtype: None
        """
        self.grid_rects = []  # Clear previous grid_rects
        # Create a rect for each column and row
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                x = grid_x + col * self.block_size
                y = grid_y + row * self.block_size
                self.rect = pygame.Rect(x, y, self.block_size, self.block_size)
                self.grid_rects.append(self.rect)

                # Create a surface with an alpha channel
                cell_surface = pygame.Surface((self.block_size, self.block_size), pygame.SRCALPHA)

                # Receive color based on grid state
                color = self.colors[self.grid_state[row][col]]

                # Fill the cell surface with the color
                cell_surface.fill(color)

                # Blit the cell surface onto the main screen
                self.screen.blit(cell_surface, (x, y))

                # Draw the grid lines
                pygame.draw.rect(self.screen, (255, 255, 255), self.rect, 1)  # White color for grid lines

    def get_cell_state(self, row, col):
        """
        Return the state of a specific cell.
        :param row: Row of grid to be checked
        :type row: int
        :param col: Column of grid to be checked
        :type col: int
        :return: State of the grid to be checked
        :rtype: int
        """
        if 0 <= row < self.num_rows and 0 <= col < self.num_cols:
            return self.grid_state[row][col]
        return None

    def get_grids(self):
        return self.grid_rects

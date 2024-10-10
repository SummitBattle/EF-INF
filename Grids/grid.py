# Imports
import pygame


class Grid:
    """
    A class representing a grid for a game like Battleship, where cells can hold different states
    (empty, occupied, miss, hit, etc.) and display colors accordingly.

    Attributes:
        block_size (int): Size of each cell in the grid.
        SCREEN (pygame.Surface): The window surface where the grid will be drawn.
        num_rows (int): Number of rows in the grid.
        num_cols (int): Number of columns in the grid.
        grid_rects (list): List of grid cell rectangles (pygame.Rect).
        grid_state (list): 2D list holding the state of each cell.
        is_hovering (bool): Whether the mouse is hovering over a grid cell.
        colors (dict): A dictionary mapping cell states to RGBA color values.
        black_grid (bool): If True, allows grid cells to be switched to the black (state 4) state.
    """

    def __init__(self, block_size, screen):
        """
        Initialize a Grid instance.

        Args:
            block_size (int): Size of each grid cell in pixels.
            screen (pygame.Surface): The Pygame surface (window) where the grid will be drawn.

        Returns:
            None
        """
        self.rect = None
        self.block_size = block_size
        self.SCREEN = screen
        self.num_rows = 10  # Number of rows
        self.num_cols = 10  # Number of columns
        self.grid_rects = []  # List to hold grid rectangles
        self.grid_state = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)]  # Grid state (2D list)
        self.is_hovering = False  # Indicates if the mouse is hovering over the grid
        self.colors = {
            0: (0, 255, 255, 128),  # Empty (light blue)
            1: (0, 0, 255, 128),    # Occupied (blue, semi-transparent)
            2: (255, 0, 0, 128),    # Miss (red, semi-transparent)
            3: (0, 255, 0, 128),    # Hit (green)
            4: (0, 0, 0, 128),      # Selected (black, semi-transparent)
            5: (0, 255, 255, 255)   # Hovering (green-blue, transparent)
        }
        self.black_grid = False  # Check if current black grid state can be changed

    def set_cell_state(self, row, col, value):
        """
        Set the state of a cell in the grid.

        Args:
            row (int): The row of the cell.
            col (int): The column of the cell.
            value (int): The new state value (0 to 5).

        Returns:
            None
        """
        current_state = self.grid_state[row][col]

        # Prevent changing the state if it's already a miss (2) or hit (3)
        if current_state in [2, 3]:
            return

        # Update the state only if it's not 4 or if black grid is allowed
        if current_state != 4 or self.black_grid:
            self.grid_state[row][col] = value

    def get_cell_state(self, row, col):
        """
        Get the state of a specific cell.

        Args:
            row (int): The row of the cell.
            col (int): The column of the cell.

        Returns:
            int: The state of the specified cell.
        """
        return self.grid_state[row][col]

    def draw_grid(self, grid_x, grid_y):
        """
        Draw the grid on the screen, with each cell colored based on its state.

        Args:
            grid_x (int): The x-coordinate where the grid starts.
            grid_y (int): The y-coordinate where the grid starts.

        Returns:
            None
        """
        self.grid_rects = []  # Clear previous grid_rects

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                x = grid_x + col * self.block_size
                y = grid_y + row * self.block_size
                self.rect = pygame.Rect(x, y, self.block_size, self.block_size)
                self.grid_rects.append(self.rect)
                self.check_mouse_hover()  # Check if the mouse is hovering over the grid

                # Create a cell surface with an alpha channel
                cell_surface = pygame.Surface((self.block_size, self.block_size), pygame.SRCALPHA)

                # Set cell state based on whether the mouse is hovering or not
                if self.is_hovering:
                    self.set_cell_state(row, col, 5)
                else:
                    self.set_cell_state(row, col, 0)

                # Get color based on the cell state
                color = self.colors[self.grid_state[row][col]]

                # Fill the cell surface with the color and draw it on the screen
                cell_surface.fill(color)
                self.SCREEN.blit(cell_surface, (x, y))

                # Draw grid lines (white)
                pygame.draw.rect(self.SCREEN, (255, 255, 255), self.rect, 1)

    def get_cell_states(self):
        """
        Get the current states of all grid cells.

        Returns:
            list: 2D list representing the states of the grid cells.
        """
        return self.grid_state

    def get_grids(self):
        """
        Get the list of all grid cell rectangles (pygame.Rect objects).

        Returns:
            list: List of grid cell rectangles.
        """
        return self.grid_rects

    def check_mouse_hover(self):
        """
        Check if the mouse is hovering over the grid.

        Returns:
            None
        """
        mouse_pos = pygame.mouse.get_pos()
        self.is_hovering = self.rect.collidepoint(mouse_pos)



    def return_black_grids(self):
        """
        Get a list of all grid cells that are in the 'black' state (state 4).

        Returns:
            list: List of tuples representing the row and column of black grid cells.
        """
        black_grids = []
        for row in range(len(self.grid_state)):
            for col in range(len(self.grid_state[row])):
                if self.grid_state[row][col] == 4:
                    black_grids.append((row, col))
        return black_grids

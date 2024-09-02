import pygame

class Grid:
    def __init__(self, block_size, screen):
        """
        Creates a Grid instance
        :param block_size: Size of each cell in the grid
        :type block_size: int
        :param screen: The window of the game
        :type screen: screen
        """
        self.block_size = block_size
        self.SCREEN = screen
        self.num_rows = 10  # Number of rows
        self.num_cols = 10  # Number of columns
        self.grid_rects = []  # List to hold grid rectangles
        self.grid_state = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)]  # List to hold grid states
        self.is_hovering = True  # Check if mouse is hovering grid
        # Define colors for different states
        self.colors = {
            0: (0, 255, 255, 128),  # Empty (light blue)
            1: (0, 0, 255, 128),    # Occupied (blue, semi-transparent)
            2: (255, 0, 0, 128),    # Miss (red, semi-transparent)
            3: (0, 255, 0, 128), # Hit (green)
            4: (0,0,0,128),      # Selected (black, semi-transparent)
            5: (0,255,255,255) # Hovering (green-blue, transparent
        }
        self.blackgrid = False  # Check if current blackgrid state can be changed

    def set_cell_state(self, row, col, value):
        """
        Sets the cell in a different state, needed for colors
        :param row: Row of the cell to be changed
        :type row: int
        :param col: Column of the cell to be changed
        :type col: int
        :param value: State to change into
        :type value: int
        :return: None
        :rtype: None
        """

        current_state = self.grid_state[row][col]

        # Prevent changing the state if it's already a miss (2) or hit (3)
        if current_state in [2, 3]:
            return  # Do nothing, keep the current state

        # Update the state only if it's not 4 or if blackgrid is True
        if current_state != 4 or self.blackgrid:
            self.grid_state[row][col] = value

    def get_cell_state(self, row, col):
        # Directly return the state of the cell at the specified row and column
        return self.grid_state[row][col]


    def draw_grid(self, grid_x, grid_y):
        """
        draws the grids on the screen
        :param grid_x: X position of the grid
        :type grid_x: int
        :param grid_y: Y position of the grid
        :type grid_y: int
        :return: None
        :rtype: None
        """

        # Create Rects and List
        self.grid_rects = []
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                x = grid_x + col * self.block_size
                y = grid_y + row * self.block_size
                self.rect = pygame.Rect(x, y, self.block_size, self.block_size)
                self.grid_rects.append(self.rect)
                self.check_mouse_hover() # Check if mouse is hovering grid

                # Create a surface with an alpha channel
                cell_surface = pygame.Surface((self.block_size, self.block_size), pygame.SRCALPHA)
                if self.is_hovering:
                    self.set_cell_state(row,col,5)

                else:
                    self.set_cell_state(row,col,0)
                # Receive grid state for color
                color = self.colors[self.grid_state[row][col]]

                # Fill the cell surface with the color
                cell_surface.fill(color)

                # Blit the cell surface onto the main screen
                self.SCREEN.blit(cell_surface, (x, y))

                # Draw the grid lines
                pygame.draw.rect(self.SCREEN, (255, 255, 255), self.rect, 1)  # White color for grid lines

    def get_cell_states(self):
        """
        Returns the state from each grid
        :return: List of the states
        :rtype: list
        """
        return self.grid_state

    def get_grids(self):
        """
        Returns the rect from each grid
        :return: List of the rects
        :rtype: list
        """
        return self.grid_rects


    def check_mouse_hover(self):
        """
        Check if mouse is hovering button
        :return: None
        :rtype: None
        """
        self.mousePos = pygame.mouse.get_pos()
        if self.rect.collidepoint(self.mousePos):
            self.is_hovering = True  # Mouse is over the ship
        else:
            self.is_hovering = False # Moise is not over the ship

    def check_mouseclick(self):
        """
        Check for mouse click on button
        :return: None
        :rtype: None
        """
        mouse_pressed = pygame.mouse.get_pressed()
        if self.is_dragging and not mouse_pressed[0]:
            self.is_dragging = False

    def return_blackgrids(self):
        """
        Returns all black grids
        :return: List of black grids (state 4)
        :rtype: list
        """
        blackgrids = []
        # Iterate through grid_state and collect the coordinates with state 4
        for row in range(len(self.grid_state)):
            for col in range(len(self.grid_state[row])):
                if self.grid_state[row][col] == 4:
                    # Append a tuple with the coordinates (row, col)
                    blackgrids.append((row, col))

        return blackgrids

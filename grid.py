import pygame

class Grid:
    def __init__(self, block_size, screen):
        self.block_size = block_size
        self.SCREEN = screen
        self.num_rows = 10  # Number of rows
        self.num_cols = 10  # Number of columns
        self.grid_rects = []  # List to hold grid rectangles
        self.grid_state = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)]

        # Define colors for different states
        self.colors = {
            0: (0, 255, 255, 128),  # Empty (light blue)
            1: (0, 0, 255, 128),    # Occupied (blue, semi-transparent)
            2: (255, 0, 0, 128),    # Miss (red, semi-transparent)
            3: (0, 255, 0, 128)     # Hit (green)
        }

    def set_cell_state(self, row, col, state):
        """Set the state of a cell. State can be 0 (empty), 1 (occupied), 2 (miss), or 3 (hit)."""
        if 0 <= row < self.num_rows and 0 <= col < self.num_cols:
            self.grid_state[row][col] = state

    def get_cell_rects(self):
        """Return the rectangles for each cell in the grid."""
        rects = []
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                x = col * self.block_size
                y = row * self.block_size
                rect = pygame.Rect(x, y, self.block_size, self.block_size)
                rects.append(rect)
        return rects

    def drawgrid(self, grid_x, grid_y):
        """Draw the grid with cell states filled with semi-transparent colors."""
        self.grid_rects = self.get_cell_rects()  # Reset grid rectangles

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                x = grid_x + col * self.block_size
                y = grid_y + row * self.block_size
                rect = pygame.Rect(x, y, self.block_size, self.block_size)

                # Create a surface with an alpha channel
                cell_surface = pygame.Surface((self.block_size, self.block_size), pygame.SRCALPHA)

                # Get the color based on the cell state
                color = self.colors[self.grid_state[row][col]]

                # Fill the cell surface with the color
                cell_surface.fill(color)

                # Blit the cell surface onto the main screen
                self.SCREEN.blit(cell_surface, (x, y))

                # Draw the grid lines
                pygame.draw.rect(self.SCREEN, (255, 255, 255), rect, 1)  # White color for grid lines

    def get_cell_state(self, row, col):
        """Return the state of a specific cell."""
        if 0 <= row < self.num_rows and 0 <= col < self.num_cols:
            return self.grid_state[row][col]
        return None

    def check_overlap(self, ship_rect):
        """Check if the ship overlaps with any cell in the grid."""
        for rect in self.grid_rects:
            if ship_rect.colliderect(rect):
                return True
        return False

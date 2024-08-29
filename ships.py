import pygame


class Ship:
    dragging_ship = None

    def __init__(self, num_rows, num_cols, block_size, screen, name, orientation='horizontal'):

        self.block_size = block_size
        self.SCREEN = screen
        self.num_rows = num_rows  # Number of rows the ship will occupy
        self.num_cols = num_cols  # Number of columns the ship will occupy
        self.name = name
        self.is_hovering = False
        self.is_dragging = False
        self.orientation = orientation
        self.color = {
            'hover': (50, 0, 255, 255),  # Hover color
            'normal': (0, 0, 255, 128)  # Normal color
        }

    def checkmousehover(self):
        self.mousePos = pygame.mouse.get_pos()
        if self.rect.collidepoint(self.mousePos) and Ship.dragging_ship is None:
            self.is_hovering = True  # Mouse is over the ship


    def checkmouseclick(self):
        if self.is_dragging:
            self.is_dragging = False
            Ship.dragging_ship = None

        if self.is_hovering:
            if Ship.dragging_ship is None:
                Ship.dragging_ship = self  # Start dragging this ship
                self.is_dragging = True

    def toggle_orientation(self):

        if self.orientation == 'horizontal' and self.is_hovering or self.is_dragging:
            self.orientation = 'vertical'
            self.num_rows, self.num_cols = self.num_cols, self.num_rows
        elif self.orientation == 'vertical' and self.is_hovering or self.is_dragging:
            self.orientation = 'horizontal'
            self.num_rows, self.num_cols = self.num_cols, self.num_rows



    def drawship(self, grid_x, grid_y):

        """Draw the ship with hover effect on the grid."""

        self.is_hovering = False
        # Determine if mouse is over any part of the ship
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                x = grid_x + col * self.block_size
                y = grid_y + row * self.block_size
                self.rect = pygame.Rect(x, y, self.block_size, self.block_size)
                self.checkmousehover()

                if self.is_dragging:
                    self.rect.x, self.rect.y = self.mousePos
                    grid_x, grid_y = self.mousePos



        # Draw the ship's cells with the appropriate color
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                x = grid_x + col * self.block_size
                y = grid_y + row * self.block_size
                rect = pygame.Rect(x, y, self.block_size, self.block_size)

                # Create a surface with an alpha channel
                cell_surface = pygame.Surface((self.block_size, self.block_size), pygame.SRCALPHA)

                # Fill the surface with hover or normal color
                if self.is_hovering:
                    cell_surface.fill(self.color['hover'])  # Hover color
                else:
                    cell_surface.fill(self.color['normal'])  # Normal color

                # Blit the cell surface onto the main screen
                self.SCREEN.blit(cell_surface, (x, y))

                # Draw the grid lines
                pygame.draw.rect(self.SCREEN, (255, 255, 255), rect, 1)  # White color for grid lines




class PatrolBoat(Ship):
    def __init__(self,BLOCK_SIZE,SCREEN):
        super().__init__(2,2,BLOCK_SIZE,SCREEN,"PatrolBoat")


class Destroyer(Ship):
    def __init__(self,BLOCK_SIZE,SCREEN):
        super().__init__(3,1,BLOCK_SIZE,SCREEN,"Destroyer")

class Carrier(Ship):
    def __init__(self,BLOCK_SIZE,SCREEN):
        super().__init__(5,1,BLOCK_SIZE,SCREEN,"Carrier")

class Battleship(Ship):
    def __init__(self, BLOCK_SIZE, SCREEN):
        super().__init__(4, 1, BLOCK_SIZE, SCREEN, "Battleship")

import pygame

class Ship:
    dragging_ship = None

    def __init__(self, num_rows, num_cols, block_size, screen, name, orientation='horizontal'):
        self.overlapping = False
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
        else:
            self.is_hovering = False

    def checkmouseclick(self):
        mouse_pressed = pygame.mouse.get_pressed()
        if self.is_dragging and not mouse_pressed[0]:
            self.is_dragging = False
            Ship.dragging_ship = None

        if self.is_hovering and mouse_pressed[0]:
            if Ship.dragging_ship is None:
                Ship.dragging_ship = self  # Start dragging this ship
                self.is_dragging = True


    def toggle_orientation(self):
        if (self.orientation == 'horizontal' and (self.is_hovering or self.is_dragging)) or \
           (self.orientation == 'vertical' and (self.is_hovering or self.is_dragging)):
            self.orientation = 'vertical' if self.orientation == 'horizontal' else 'horizontal'
            self.num_rows, self.num_cols = self.num_cols, self.num_rows

    def drawship(self, grid_x, grid_y,grid):
        """Draw the ship with hover effect on the grid."""
        self.is_hovering = False
        width = self.num_cols * self.block_size
        height = self.num_rows * self.block_size
        if self.overlapping:
            grid_x = self.collided_rect.x
            grid_y = self.collided_rect.y
        # Create the rect for the ship
        self.rect = pygame.Rect(grid_x, grid_y, width, height)
        self.checkmousehover()
        if self.is_dragging:
            # Center the ship around the mouse position
            self.overlapping = False
            self.rect.topleft = (self.mousePos[0] - width // 2, self.mousePos[1] - height // 2)


        if self.overlapping:

            self.rect.topleft = self.collided_rect.topleft
            self.rect.midtop = self.collided_rect.midtop
            self.rect.midright = self.collided_rect.midright

        # Create a surface for the ship
        ship_surface = pygame.Surface((width, height), pygame.SRCALPHA)

        # Fill the surface with hover or normal color
        if self.is_hovering:
            ship_surface.fill(self.color['hover'])  # Hover color
        else:
            ship_surface.fill(self.color['normal'])  # Normal color

        # Blit the ship surface onto the main screen
        self.SCREEN.blit(ship_surface, self.rect.topleft)

        # Draw the grid lines around the ship
        pygame.draw.rect(self.SCREEN, (255, 255, 255), self.rect, 1)  # White color for grid lines

    def checkoverlap(self, grid):
        self.cell_rects = grid.get_cell_rects()

        # Check if the ship's rect collides with any rect in the grid
        self.collision_index = self.rect.collidelist(self.cell_rects)
        if self.collision_index != -1:
            self.collided_rect = self.cell_rects[self.collision_index]
            print(self.collided_rect)

            # Set ship's overlapping status and store the collided rectangle
            self.overlapping = True
        else:
            self.overlapping = False

        print("overlapping is:")
        print(self.overlapping)


class PatrolBoat(Ship):
    def __init__(self, BLOCK_SIZE, SCREEN):
        super().__init__(2, 2, BLOCK_SIZE, SCREEN, "PatrolBoat")

class Destroyer(Ship):
    def __init__(self, BLOCK_SIZE, SCREEN):
        super().__init__(3, 1, BLOCK_SIZE, SCREEN, "Destroyer")

class Carrier(Ship):
    def __init__(self, BLOCK_SIZE, SCREEN):
        super().__init__(5, 1, BLOCK_SIZE, SCREEN, "Carrier")

class Battleship(Ship):
    def __init__(self, BLOCK_SIZE, SCREEN):
        super().__init__(4, 1, BLOCK_SIZE, SCREEN, "Battleship")

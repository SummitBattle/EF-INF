import pygame


class Ship:
    """
    Represents a ship in the Battleship game.

    Attributes:
        dragging_ship (Ship or None): Reference to the ship currently being dragged.
        rect (Rect or None): Pygame rectangle representing the ship's position and size.
        collided_rect (Rect or None): Pygame rectangle for the area the ship is colliding with.
        overlapping (bool): Indicates whether the ship is overlapping with any grid cells.
        block_size (int): Size of each cell in the grid.
        screen (Surface): The window of the game where the ship is drawn.
        num_rows (int): Number of rows the ship occupies in the grid.
        num_cols (int): Number of columns the ship occupies in the grid.
        name (str): The name of the ship.
        is_hovering (bool): Indicates if the mouse is currently hovering over the ship.
        is_dragging (bool): Indicates if the ship is currently being dragged.
        orientation (str): Orientation of the ship ('horizontal' or 'vertical').
        color (dict): A dictionary holding the colors used for hover and normal states.
        SCREENY (int): Height of the screen.
        SCREENX (int): Width of the screen.
    """
    dragging_ship = None

    def __init__(self, num_rows, num_cols, block_size, screen, name, orientation='horizontal'):
        """
        Initialize a Ship instance.
        :param num_rows: Amount of grid rows
        :type num_rows: int
        :param num_cols: Amount of grid columns
        :type num_cols: int
        :param block_size: Size of each cell
        :type block_size: int
        :param screen: Window of the game
        :type screen: screen
        :param name: Name of the ship
        :type name: str
        :param orientation: Saves if ship is horizontal or flipped to vertical
        :type orientation: str
        """

        self.rect = None
        self.collided_rect = None
        self.overlapping = False
        self.block_size = block_size
        self.screen = screen
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
        self.SCREENY, self.SCREENX = screen.get_size()

    def check_mouse_hover(self):
        """
        Checks if mouse is over ship rect.
        :return: None
        :rtype: None
        """
        mousePos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mousePos) and Ship.dragging_ship is None:
            self.is_hovering = True  # Mouse is over the ship
        else:
            self.is_hovering = False  # Mouse is not over the ship

    def check_mouseclick(self):
        """
        Checks if mouse got clicked while on a ship rect.
        :return: None
        :rtype: None
        """
        mouse_pressed = pygame.mouse.get_pressed()
        # Checks if a ship is currently being dragged and clicked
        if self.is_dragging and not mouse_pressed[0]:
            self.is_dragging = False
            Ship.dragging_ship = None
        # Checks if mouse is hovering over ship and being clicked
        if self.is_hovering and mouse_pressed[0]:
            if Ship.dragging_ship is None:
                Ship.dragging_ship = self  # Start dragging this ship
                self.is_dragging = True

    def toggle_orientation(self):
        """
        Function to flip the ship to vertical or back to horizontal.
        :return:
        :rtype:
        """
        if (self.orientation == 'horizontal' and (self.is_hovering or self.is_dragging)) or \
                (self.orientation == 'vertical' and (self.is_hovering or self.is_dragging)):
            self.orientation = 'vertical' if self.orientation == 'horizontal' else 'horizontal'
            self.num_rows, self.num_cols = self.num_cols, self.num_rows

    def draw_ship(self, ship_x, ship_y, grid):
        """
        Draws the ship.
        :param ship_x: X position of the ship
        :type ship_x: int
        :param ship_y: Y position of the ship
        :type ship_y: int
        :param grid: Grid it belongs to (Ships1 belong to Grid1 and Ships2 to Grid2)
        :type grid: Grid
        :return: None
        :rtype: None
        """
        self.is_hovering = False
        width = self.num_cols * self.block_size
        height = self.num_rows * self.block_size
        # Clip the position of the ship to the overlapping grid
        if self.overlapping:
            ship_x = self.collided_rect.x
            ship_y = self.collided_rect.y

        # Create the rect for the ship
        self.rect = pygame.Rect(ship_x, ship_y, width, height)

        self.check_mouse_hover()
        if self.is_dragging:
            mousePos = pygame.mouse.get_pos()
            # If current ship is being dragged, center the ship around the mouse position
            self.overlapping = False
            self.rect.topleft = mousePos

        # Check if ship is overlapping with any grids
        overlapping_cells = self.check_overlap(grid)

        # If overlapping with any grids, clip ship to the position of the grid
        if self.overlapping:

            self.collided_rect = overlapping_cells[0]

            if self.rect.top <= self.screen.get_height() / 2.3:
                self.rect.top = self.collided_rect.top

            else:
                self.rect.bottom = self.collided_rect.bottom

            self.rect.left = self.collided_rect.left

        # Create a surface for the ship
        ship_surface = pygame.Surface((width, height), pygame.SRCALPHA)

        # Fill the surface with hover or normal color
        if self.is_hovering:
            ship_surface.fill(self.color['hover'])  # Hover color
        else:
            ship_surface.fill(self.color['normal'])  # Normal color

        # Blit the ship surface onto the main screen
        self.screen.blit(ship_surface, self.rect.topleft)

        # Draw the grid lines around the ship
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect, 1)  # White color for grid lines

    def check_overlap(self, grid):
        """
        Function to check for overlapping.
        :param grid: The corresponding Grid for the ship
        :type grid: Grid
        :return: All cells which are overlapping with the ship
        :rtype: List
        """

        cell_rects = grid.get_grids()  # Get all grid rectangles
        overlapping_cells = []  # List to store overlapping cells

        # Iterate through all grid cells and check if the ship's rect overlaps
        for cell_rect in cell_rects:

            if self.rect.colliderect(cell_rect):
                overlapping_cells.append(cell_rect)  # Store the overlapping grid cell
                self.overlapping = True

        return overlapping_cells


class PatrolBoat(Ship):
    """
    Child class of Ship, with specified size and name.
    """

    def __init__(self, BLOCK_SIZE, SCREEN):
        super().__init__(2, 2, BLOCK_SIZE, SCREEN, "PatrolBoat")


class Destroyer(Ship):
    """
    Child class of Ship, with specified size and name.
    """

    def __init__(self, BLOCK_SIZE, SCREEN):
        super().__init__(3, 1, BLOCK_SIZE, SCREEN, "Destroyer")


class Battleship(Ship):
    """
    Child class of Ship, with specified size and name.
    """

    def __init__(self, BLOCK_SIZE, SCREEN):
        super().__init__(4, 1, BLOCK_SIZE, SCREEN, "Battleship")


class Carrier(Ship):
    """
    Child class of Ship, with specified size and name.
    """

    def __init__(self, BLOCK_SIZE, SCREEN):
        super().__init__(5, 1, BLOCK_SIZE, SCREEN, "Carrier")

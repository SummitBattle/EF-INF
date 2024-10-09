import pygame.mouse


class GridManager:
    """
    Manage the grids for the game.

    This class handles the interactions and state changes between two grids,
    including drawing grids, managing ship placements, and handling user
    interactions.

    Attributes:
        grid1 (Grid): The first grid instance for the game.
        grid2 (Grid): The second grid instance for the game.
        block_size (int): Size of each grid cell.
        smallergrid1 (Smallergrid): The first smaller grid instance.
        smallergrid2 (Smallergrid): The second smaller grid instance.
        blackgrid (bool): State indicating if the black grid is active for grid1.
        blackgrid2 (bool): State indicating if the black grid is active for grid2.
        gridleft1 (float): The left position of grid1 on the screen.
        gridtop1 (int): The top position of grid1 on the screen.
        gridleft2 (float): The left position of grid2 on the screen.
        gridtop2 (int): The top position of grid2 on the screen.
       """
    def __init__(self, grid1, grid2, block_size, smallergrid1, smallergrid2, SCREEN_X):
        """
        Create a new GridManager instance.
        :param grid1: First Grid instance
        :type grid1: Grid
        :param grid2: Second Grid instance
        :type grid2: Grid
        :param block_size: Size of each grid cell
        :type block_size: int
        :param smallergrid1: First Smallergrid instance
        :type smallergrid1: Smallergrid
        :param smallergrid2: Second Smallergrid instance
        :type smallergrid2: Smallergrid
        """

        self.grid1 = grid1
        self.grid2 = grid2
        self.block_size = block_size
        self.smallergrid1 = smallergrid1
        self.smallergrid2 = smallergrid2
        self.blackgrid = True
        self.blackgrid2 = True

        self.gridleft1 = SCREEN_X / 2 - 400
        self.gridtop1 = 100
        self.gridleft2 = SCREEN_X / 2 + 100
        self.gridtop2 = 100

    def draw_smaller_grids(self, SCREEN_X, SCREEN_Y):
        """
        Draws the smallergrids on screen.
        :param SCREEN_X: Width of screen
        :type SCREEN_X: int
        :param SCREEN_Y: Height of screen
        :type SCREEN_Y: int
        :return: None
        :rtype: None
        """
        gridleft1 = SCREEN_X / 20
        gridtop1 = SCREEN_Y / 1.3
        gridleft2 = SCREEN_X - SCREEN_X / 8
        gridtop2 = SCREEN_Y / 1.3

        self.smallergrid1.draw_grid(gridleft1, gridtop1)
        self.smallergrid2.draw_grid(gridleft2, gridtop2)

    def draw_grids(self):
        """
        Draws the normal grids on the screen.
        :return: None
        :rtype: None
        """


        self.grid1.draw_grid(self.gridleft1, self.gridtop1)
        self.grid2.draw_grid(self.gridleft2, self.gridtop2)

    def ship_into_state(self, grid, ship, smallergrid,side):
        """
        Turns left ship into cell state 1 (occupied)
        :param grid: Grid instance.
        :type grid: Grid
        :param ship: Ship instance
        :type ship: Ship
        :param smallergrid: Smallergrid instance
        :type smallergrid: Smallergrid
        :return: List of grid positions of the ship
        :rtype: List
        """
        overlapping_rects = ship.check_overlap(grid)

        ship_positions = []  # Array to store the grid positions of the ship
        # If side is 1, calculate for the left grid, else for the right grid
        if side == 1:
            gridleft = self.gridleft1
            gridtop = self.gridtop1
        else:
            gridleft = self.gridleft2
            gridtop = self.gridtop2
        # Calculate colum and row and update cell state
        for rect in overlapping_rects:
            row = (rect.left - gridleft) // self.block_size
            col = (rect.top - gridtop) // self.block_size

            grid.set_cell_state(int(col), int(row), 1)
            smallergrid.set_cell_state(int(col), int(row), 1)

            # Store the grid position
            ship_positions.append((int(col), int(row)))

        return ship_positions



    def click_on_grid(self, grid, SCREEN_X,side):
        """
        Convert left state 0 (empty) into state 4 (selected).
        :param grid: Grid instance
        :type grid: Grid
        :param SCREEN_X: Width of screen
        :type SCREEN_X: int
        :return: None
        :rtype: None
        """
        # Calculate for either left or right side
        if side == 1:

            gridleft = SCREEN_X / 2 - 400
            gridtop = 100

        else:
            gridleft = SCREEN_X / 2 + 100
            gridtop = 100

        # Get the mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Get all rectangles for grid cells
        overlapping_rects2 = grid.get_grids()  # Assuming this method returns a list of pygame.Rect objects

        # Iterate through each rectangle to find which one was clicked
        for rect in overlapping_rects2:

            if rect.collidepoint(mouse_pos):
                # Turn all blackgrids back to normal
                blackgrids = grid.return_black_grids()
                for grids in blackgrids:
                    grid.black_grid = True
                    grid.set_cell_state(grids[0], grids[1], 0)
                    grid.black_grid = False

                # Calculate the row and column based on the rectangle's position
                row = (rect.left - gridleft) // self.block_size
                col = (rect.top - gridtop) // self.block_size
                grid.black_grid = True
                grid.set_cell_state(int(col), int(row), 4)  # Assuming the method expects (row, col, value)
                grid.black_grid = False

                break  # Exit the loop once the correct cell is found and processed

    def check_blackgrid(self, grid, smallergrid, all_ships):
        """
        Convert state 4 (selected) into 2 (miss) or 3 (hit).
        Dictionary contains keys as string.
        Dictionary contains values with lists of grid positions.
        :param grid: Grid instance
        :type grid: Grid
        :param smallergrid: Smallergrid instance
        :type smallergrid: Smallergrid
        :param all_ships: Dictionary with all ships and their grid positions
        :type all_ships: dict[str,list]
        :return: If a ship got hit
        :rtype: Bool
        """
        # Get the black grids with their row and column positions
        blackgrids = grid.return_black_grids()

        # Iterate through all the grid positions returned
        while blackgrids:  # Loop until there are no more black grids to check
            row, col = blackgrids.pop(0)  # Receive row and col of black grid, remove black grid from the list

            # If the enemy grid has a ship (state 1), mark it as a hit (state 3)
            hit_detected = False
            for ship_name, grids in all_ships.items():
                # Check if row and col of black grid match with row and col from a ship grid
                if (row, col) in grids:
                    hit_detected = True

                    grids.remove((row, col))  # Remove the grid from the ship's list

                    break

            if hit_detected:
                grid.black_grid = True
                grid.set_cell_state(row, col, 3)  # Update the grid to show a hit
                smallergrid.set_cell_state(row, col, 3)
                return hit_detected
            else:
                grid.black_grid = True
                grid.set_cell_state(row, col, 2)  # Update the grid to show a miss
                smallergrid.set_cell_state(row, col, 2)
                return hit_detected

        # Reset self.blackgrid

    def find_ships_with_no_grids_left(self, all_ships):
        """
        Finds and returns a list of ships that have no grids left.

        :param all_ships: Dictionary with ship names as keys and lists of grid positions as values.
        :return: List of ship names that have no grids left.
        """
        ships_with_no_grids_left = []
        ships_to_remove = []

        # Collect ships with no grids left
        for ship_name, grids in all_ships.items():
            if len(grids) == 0:
                ships_with_no_grids_left.append(ship_name)
                ships_to_remove.append(ship_name)

        # Remove collected ships from the dictionary
        for ship_name in ships_to_remove:
            all_ships.pop(ship_name)
            print(ship_name)

        return ships_with_no_grids_left

    def check_ship_ship_overlap(self, ship, ships):
        """
        Checks overlapping between ships
        :param ship: Ship to check overlapping
        :type ship: Ship
        :param ships: All own ships
        :type ships: Array
        :return: Returns if ships are overlapping with ship
        :rtype: Bool
        """
        # Inflate the ship's rectangle to expand the detection area
        expanded_rect = ship.rect.inflate(self.block_size * 2, self.block_size * 2)

        # Check for collisions, ignoring self
        for check_ship in ships:
            if check_ship != ship and expanded_rect.colliderect(check_ship.rect):
                return True  # Overlap detected
        return False  # No overlap detected

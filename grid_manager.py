import pygame.mouse


class GridManager:
    def __init__(self,grid1,grid2,block_size,smallergrid1,smallergrid2):
        """
        Creates a new GridManager instance.
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



    def draw_smallergrids(self, SCREEN_X, SCREEN_Y):
        """
        Draws the smallergrids on screen.
        :param SCREEN_X: Width of screen
        :type SCREEN_X: int
        :param SCREEN_Y: Height of screen
        :type SCREEN_Y: int
        :return: None
        :rtype: None
        """
        self.gridleft1 = SCREEN_X / 20
        self.gridtop1 = SCREEN_Y / 1.3
        self.gridleft2 = SCREEN_X - SCREEN_X/8
        self.gridtop2 = SCREEN_Y / 1.3

        self.smallergrid1.draw_grid(self.gridleft1, self.gridtop1)
        self.smallergrid2.draw_grid(self.gridleft2, self.gridtop2)

    def draw_grids(self, SCREEN_X, SCREEN_Y):
        """
        Draws the normal grids on the screen.
        :param SCREEN_X: Width of screen
        :type SCREEN_X: int
        :param SCREEN_Y: Height of screen
        :type SCREEN_Y: int
        :return: None
        :rtype: None
        """
        self.gridleft1 = SCREEN_X/2-400
        self.gridtop1 = 100
        self.gridleft2 = SCREEN_X/2+100
        self.gridtop2 = 100


        self.grid1.draw_grid(self.gridleft1, self.gridtop1)
        self.grid2.draw_grid(self.gridleft2, self.gridtop2)

    def ship_into_state1(self, grid, ship, smallergrid):
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
        ship.checkoverlap(grid)
        overlapping_rects = ship.overlapping_cells # Get all overlapping cells between ship and grid

        ship_positions = []  # Array to store the grid positions of the ship

        # Calculate colum and row and update cell state
        for rect in overlapping_rects:

            row = (rect.left - self.gridleft1) // self.block_size
            col = (rect.top - self.gridtop1) // self.block_size

            grid.set_cell_state(int(col), int(row), 1)
            smallergrid.set_cell_state(int(col), int(row), 1)

            # Store the grid position
            ship_positions.append((int(col), int(row)))


        return ship_positions

    def ship_into_state2(self, grid, ship, smallergrid):
        """
        Turns right ship into state 1 (occupied).
        :param grid: Grid instance
        :type grid: Grid
        :param ship: Ship instance
        :type ship: Ship
        :param smallergrid: Smallergrid instance
        :type smallergrid: Smallergrid
        :return: List of grid positions of the ship
        :rtype: List
        """
        ship.checkoverlap(grid)
        overlapping_rects = ship.overlapping_cells # Receive overlapping cells between ship and grid


        ship_positions = []

        # Calculate row and column and update cell state
        for rect in overlapping_rects:
            # Uses gridleft2 and gridtop2 this time (right position)
            row = (rect.left - self.gridleft2) // self.block_size
            col = (rect.top - self.gridtop2) // self.block_size
            grid.set_cell_state(int(col), int(row), 1)
            smallergrid.set_cell_state(int(col), int(row), 1)

            ship_positions.append((int(col), int(row)))


        # Return the list of grid positions
        return ship_positions

    def click_on_grid(self, grid, SCREEN_X):
        """
        Convert left state 0 (empty) into state 4 (selected).
        :param grid: Grid instance
        :type grid: Grid
        :param SCREEN_X: Width of screen
        :type SCREEN_X: int
        :return: None
        :rtype: None
        """
        self.gridleft1 = SCREEN_X / 2 - 400
        self.gridtop1 = 100
        self.gridleft2 = SCREEN_X / 2 + 100
        self.gridtop2 = 100

        # Get the mouse position
        self.mousePos = pygame.mouse.get_pos()

        # Get all rectangles for grid cells
        overlapping_rects2 = grid.get_grids()  # Assuming this method returns a list of pygame.Rect objects

        # Iterate through each rectangle to find which one was clicked
        for rect in overlapping_rects2:

            if rect.collidepoint(self.mousePos):


                # Calculate the row and column based on the rectangle's position
                row = (rect.left - self.gridleft1) // self.block_size
                col = (rect.top - self.gridtop1) // self.block_size
                grid.set_cell_state(int(col), int(row), 4)  # Assuming the method expects (row, col, value)
                if not self.blackgrid:

                    self.blackgrid = True
                    grid.blackgrid = True

                else:
                    self.blackgrid = False
                    grid.blackgrid = False


                break  # Exit the loop once the correct cell is found and processed

    def click_on_grid2(self, grid, SCREEN_X):
        self.gridleft1 = SCREEN_X / 2 - 400
        self.gridtop1 = 100
        self.gridleft2 = SCREEN_X / 2 + 100
        self.gridtop2 = 100

        # Get the mouse position
        self.mousePos = pygame.mouse.get_pos()

        # Get all rectangles for grid cells
        overlapping_rects2 = grid.get_grids()

        for rect in overlapping_rects2:
            if rect.collidepoint(self.mousePos):

                # Calculate the row and column based on the rectangle's position
                row = (rect.left - self.gridleft2) // self.block_size
                col = (rect.top - self.gridtop2) // self.block_size
                grid.set_cell_state(int(col), int(row), 4)

                # Toggle blackgrid2 correctly, similar to Player 1's behavior
                if not self.blackgrid2:
                    self.blackgrid2 = True
                    grid.blackgrid = True
                else:
                    self.blackgrid2 = False
                    grid.blackgrid = False

                break

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
        :return: None
        :rtype: None
        """
        # Get the black grids with their row and column positions
        blackgrids = grid.return_blackgrids()


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
                grid.blackgrid = True
                grid.set_cell_state(row, col, 3)  # Update the grid to show a hit
                smallergrid.set_cell_state(row, col, 3)
            else:
                grid.blackgrid = True
                grid.set_cell_state(row, col, 2)  # Update the grid to show a miss
                smallergrid.set_cell_state(row, col, 2)

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

        return ships_with_no_grids_left

import pygame.mouse


class GridManager:
    def __init__(self,grid1,grid2,blocksize,smallergrid1,smallergrid2):
        self.grid1 = grid1
        self.grid2 = grid2
        self.block_size = blocksize
        self.smallergrid1 = smallergrid1
        self.smallergrid2 = smallergrid2
        self.blackgrid = True



    def draw_smallergrids(self, SCREEN_X, SCREEN_Y):
        self.gridleft1 = SCREEN_X / 20
        self.gridtop1 = SCREEN_Y / 1.3
        self.gridleft2 = SCREEN_X - SCREEN_X/8
        self.gridtop2 = SCREEN_Y / 1.3

        self.smallergrid1.draw_grid(self.gridleft1, self.gridtop1)
        self.smallergrid2.draw_grid(self.gridleft2, self.gridtop2)

    def draw_grids(self, SCREEN_X, SCREEN_Y):
        self.gridleft1 = SCREEN_X/2-400
        self.gridtop1 = 100
        self.gridleft2 = SCREEN_X/2+100
        self.gridtop2 = 100


        self.grid1.draw_grid(self.gridleft1, self.gridtop1)
        self.grid2.draw_grid(self.gridleft2, self.gridtop2)

    def ship_into_state1(self, grid, ship, smallergrid):
        overlapping_rects = ship.overlapping_cells

        ship_positions = []  # Array to store the grid positions of the ship

        for rect in overlapping_rects:

            row = (rect.left - self.gridleft1) // self.block_size
            col = (rect.top - self.gridtop1) // self.block_size

            grid.set_cell_state(int(col), int(row), 1)
            smallergrid.set_cell_state(int(col), int(row), 1)

            # Store the grid position
            ship_positions.append((int(col), int(row)))


        # Return the list of grid positions
        return ship_positions

    def ship_into_state2(self, grid, ship, smallergrid):
        overlapping_rects = ship.overlapping_cells


        ship_positions = []

        for rect in overlapping_rects:
            row = (rect.left - self.gridleft2) // self.block_size
            col = (rect.top - self.gridtop2) // self.block_size
            grid.set_cell_state(int(col), int(row), 1)  # Assuming the method expects (row, col, value)
            smallergrid.set_cell_state(int(col), int(row), 1)  # Assuming the method expects (row, col, value)

            ship_positions.append((int(col), int(row)))


            # Return the list of grid positions
        return ship_positions

    def click_on_grid(self, grid, SCREEN_X):
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
        overlapping_rects2 = grid.get_grids()  # Assuming this method returns a list of pygame.Rect objects

        # Iterate through each rectangle to find which one was clicked

        for rect in overlapping_rects2:

            if rect.collidepoint(self.mousePos):

                # Calculate the row and column based on the rectangle's position
                row = (rect.left - self.gridleft2) // self.block_size
                col = (rect.top - self.gridtop2) // self.block_size
                grid.set_cell_state(int(col), int(row), 4)  # Assuming the method expects (row, col, value)
                if not self.blackgrid:
                    self.blackgrid = True
                    grid.blackgrid = True

                else:
                    self.blackgrid = False
                    grid.blackgrid = False


                break  # Exit the loop once the correct cell is found and processed

    def check_blackgrid(self, grid, smallergrid, all_ships):
        # Get the black grids with their row and column positions
        blackgrids = grid.return_blackgrids()

        # Debug: Print initial state of the black grids list

        # Iterate through all the grid positions returned
        while blackgrids:  # Loop until there are no more black grids to check
            row, col = blackgrids.pop(0)  # Process and remove the first element

            # If the enemy grid has a ship (state 1), mark it as a hit (state 3)
            hit_detected = False
            for ship_name, grids in all_ships.items():
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

            # Debug: Print the updated state of the black grids list

        # After the loop, reset self.blackgrid if necessary
        self.blackgrid = False

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

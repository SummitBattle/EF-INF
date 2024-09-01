import pygame.mouse


class GridManager:
    def __init__(self,grid1,grid2,blocksize,smallergrid1,smallergrid2):
        self.grid1 = grid1
        self.grid2 = grid2
        self.block_size = blocksize
        self.smallergrid1 = smallergrid1
        self.smallergrid2 = smallergrid2
        self.blackgrid = True



    def drawsmallergrids(self,SCREEN_X,SCREEN_Y):
        self.gridleft1 = SCREEN_X / 20
        self.gridtop1 = SCREEN_Y / 1.3
        self.gridleft2 = SCREEN_X - SCREEN_X/8
        self.gridtop2 = SCREEN_Y / 1.3

        self.smallergrid1.drawgrid(self.gridleft1, self.gridtop1)
        self.smallergrid2.drawgrid(self.gridleft2, self.gridtop2)

    def drawgrids(self,SCREEN_X,SCREEN_Y):
        self.gridleft1 = SCREEN_X/2-400
        self.gridtop1 = 100
        self.gridleft2 = SCREEN_X/2+100
        self.gridtop2 = 100


        self.grid1.drawgrid(self.gridleft1,self.gridtop1)
        self.grid2.drawgrid(self.gridleft2,self.gridtop2)

    def shipintostate1(self, grid, ship, smallergrid):
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

    def shipintostate2(self,grid,ship,smallergrid):
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

    def clickongrid(self, grid,SCREEN_X):
        self.gridleft1 = SCREEN_X / 2 - 400
        self.gridtop1 = 100
        self.gridleft2 = SCREEN_X / 2 + 100
        self.gridtop2 = 100

        # Get the mouse position
        self.mousePos = pygame.mouse.get_pos()

        # Get all rectangles for grid cells
        overlapping_rects2 = grid.getgrids()  # Assuming this method returns a list of pygame.Rect objects

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

                print(grid.returnblackgrids())
                break  # Exit the loop once the correct cell is found and processed

    def clickongrid2(self, grid, SCREEN_X):
        self.gridleft1 = SCREEN_X / 2 - 400
        self.gridtop1 = 100
        self.gridleft2 = SCREEN_X / 2 + 100
        self.gridtop2 = 100

        # Get the mouse position
        self.mousePos = pygame.mouse.get_pos()

        # Get all rectangles for grid cells
        overlapping_rects2 = grid.getgrids()  # Assuming this method returns a list of pygame.Rect objects

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

    def checkblackgrid(self, grid, smallergrid,all_ships):
        # Get the black grids with their row and column positions
        blackgrids = grid.returnblackgrids()

        # Debug: Print initial state of the black grids list

        # Iterate through all the grid positions returned
        while blackgrids:  # Loop until there are no more black grids to check
            row, col = blackgrids.pop(0)  # Process and remove the first element

            # Debug: Check the current grid state before any changes

            # Check the state of the corresponding cell in the smallergrid
            enemy_check = smallergrid.get_cell_state(row, col)



            # If the enemy grid has a ship (state 1), mark it as a hit (state 3)
            if enemy_check == 1:
                grid.blackgrid = True

                grid.set_cell_state(row, col, 3)  # Update the grid to show a hit
                smallergrid.set_cell_state(row,col,3)
            elif enemy_check == 0:
                grid.blackgrid = True

                # Optionally update the grid to show a miss or remove the black grid state
                grid.set_cell_state(row, col, 2)  # Set to empty or another state, e.g., state 0 for empty
                smallergrid.set_cell_state(row,col,2)




        # After the loop, reset self.blackgrid if necessary
        self.blackgrid = False


import pygame.mouse


class GridManager:
    def __init__(self,grid1,grid2,blocksize,smallergrid1,smallergrid2):
        self.grid1 = grid1
        self.grid2 = grid2
        self.block_size = blocksize
        self.smallergrid1 = smallergrid1
        self.smallergrid2 = smallergrid2



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

    def clickongrid(self, grid):
        grids = grid.getgrids()  # Assuming this returns a list of pygame.Rect objects
        self.mousePos = pygame.mouse.get_pos()

        for cell_rect in grids:
            if cell_rect.collidepoint(self.mousePos):
                # Determine the row and column of the clicked grid cell
                row = (cell_rect.top - self.gridtop1) // self.block_size
                col = (cell_rect.left - self.gridleft1) // self.block_size

                # Example action: Set the cell state
                grid.set_cell_state(int(row), int(col), 4)


                # Print or return the row and column (optional)
                print(f"Clicked on grid cell at row {row}, column {col}")
                break  # Exit the loop once the correct cell is found and processed



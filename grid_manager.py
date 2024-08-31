import pygame.mouse


class GridManager:
    def __init__(self,grid1,grid2,blocksize):
        self.grid1 = grid1
        self.grid2 = grid2
        self.block_size = blocksize



    def changegrid(self,STATE1,ROW1,COL1, ROW2,COL2,STATE2):
        self.grid1.set_cell_state(ROW1,COL1,STATE1)
        self.grid2.set_cell_state(ROW2,COL2,STATE2)


    def drawgrids(self,SCREEN_X,SCREEN_Y):
        self.gridleft1 = SCREEN_X/2-400
        self.gridtop1 = 100
        self.gridleft2 = SCREEN_X/2+100
        self.gridtop2 = 100


        self.grid1.drawgrid(self.gridleft1,self.gridtop1)
        self.grid2.drawgrid(self.gridleft2,self.gridtop2)

    def shipintostate1(self,grid,ship):

        overlapping_rects = ship.overlapping_cells
        print("overlapping rects are:")
        print(overlapping_rects)
        print(self.gridleft1, self.gridleft1)

        for rect in overlapping_rects:
            row = (rect.left - self.gridleft1) // self.block_size
            col = (rect.top - self.gridtop1) // self.block_size
            print(row)
            print(col)
            grid.set_cell_state(int(col), int(row), 1)  # Assuming the method expects (row, col, value)

    def shipintostate2(self,grid,ship):
        overlapping_rects = ship.overlapping_cells

        for rect in overlapping_rects:
            row = (rect.left - self.gridleft2) // self.block_size
            col = (rect.top - self.gridtop1) // self.block_size
            print(row)
            print(col)
            grid.set_cell_state(int(col), int(row), 1)  # Assuming the method expects (row, col, value)

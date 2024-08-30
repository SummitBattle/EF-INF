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
        self.grid1.drawgrid(SCREEN_X/2-400,100)
        self.grid2.drawgrid(SCREEN_X/2+100,100)

    def checkoverlap(self,ship,grid):

        if pygame.Rect.collidelist(ship.rect,[grid.get_cell_rects()]):
            print("COLLISION")


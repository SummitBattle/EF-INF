import pygame
from gui import Gui
from image_manager import ImageManager
from grid import Grid
from grid_manager import GridManager
from buttons import Button
from ships import *
from text_manager import Textmanager
from smallergrid import Smallergrid


# Initialize Pygame
pygame.init()

SCREEN_X = 1300
SCREEN_Y = 700
BLOCK_SIZE = 30
SMALLER_BLOCK_SIZE = 10
CAPTION = "SHIP WRECK"
WHITE = (255,255,255)
LINE_THICKNESS = 30


gui = Gui(SCREEN_X,SCREEN_Y,CAPTION)
SCREEN = gui.returnscreen()

imagemanager = ImageManager()
imagemanager.load_image("BACKGROUND2.jpg")
imagemanager.resize_image(SCREEN_X,SCREEN_Y,imagemanager.return_last_image())
imagemanager.blit_image(SCREEN,(-700,-700),imagemanager.return_last_image())


grid = Grid(BLOCK_SIZE, SCREEN)
grid2 = Grid(BLOCK_SIZE, SCREEN)
smallergrid1 = Smallergrid(SMALLER_BLOCK_SIZE,SCREEN)
smallergrid2 = Smallergrid(SMALLER_BLOCK_SIZE,SCREEN)
grid_manager = GridManager(grid,grid2,BLOCK_SIZE,smallergrid1,smallergrid2)

turn = 1

copiedgrids = False
def buttonclick1():
    global turn
    if turn == 1 and customButton.shipsplaced:
        grid_manager.checkblackgrid(grid, smallergrid2,all_ships_smallergrid2)
        smallergrid2.drawgrid(SCREEN_X,SCREEN_Y)

    customButton.shipsplaced = True


    turn = 2


def buttonclick2():
    global turn
    if turn == 2 and customButton2.shipsplaced:
        grid_manager.checkblackgrid(grid2, smallergrid1,all_ships_smallergrid)
        smallergrid1.drawgrid(SCREEN_X, SCREEN_Y)
    customButton2.shipsplaced = True

    turn = 1


CUSTOMBUTTON_X = SCREEN_X/2
CUSTOMBUTTON_Y = 500
CUSTOMBUTTON_WIDTH = 50
CUSTOMBUTTON_HEIGHT = 200
customButton = Button(SCREEN, CUSTOMBUTTON_X - 375,CUSTOMBUTTON_Y,CUSTOMBUTTON_HEIGHT, CUSTOMBUTTON_WIDTH, buttonclick1)
customButton2 = Button(SCREEN, CUSTOMBUTTON_X +125,CUSTOMBUTTON_Y, CUSTOMBUTTON_HEIGHT, CUSTOMBUTTON_WIDTH, buttonclick2)
text_manager = Textmanager(SCREEN)

#BATTLESHIPS
all_ships1 = []
all_ships2 = []
destroyer = Destroyer(BLOCK_SIZE,SCREEN)
carrier = Carrier(BLOCK_SIZE,SCREEN)
patrol_boat = PatrolBoat(BLOCK_SIZE,SCREEN)
battleship = Battleship(BLOCK_SIZE,SCREEN)

destroyer2 = Destroyer(BLOCK_SIZE,SCREEN)
carrier2 = Carrier(BLOCK_SIZE,SCREEN)
patrol_boat2 = PatrolBoat(BLOCK_SIZE,SCREEN)
battleship2 = Battleship(BLOCK_SIZE,SCREEN)

all_ships1.append(destroyer)
all_ships1.append(carrier)
all_ships1.append(patrol_boat)
all_ships1.append(battleship)

all_ships2.append(destroyer2)
all_ships2.append(carrier2)
all_ships2.append(patrol_boat2)
all_ships2.append(battleship2)



# Main loop
clock = pygame.time.Clock()
clock.tick(90)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                for ship1 in all_ships1:
                    ship1.checkmousehover()
                    if not customButton.shipsplaced:
                        ship1.checkmouseclick()


                if not customButton2.shipsplaced:
                    for ship2 in all_ships2:
                        ship2.checkmousehover()
                        ship2.checkmouseclick()

                if turn == 1 and copiedgrids == True:
                    grid_manager.clickongrid(grid,SCREEN_X)

                if turn == 2 and copiedgrids == True:
                    grid_manager.clickongrid2(grid2,SCREEN_X)
            if event.button == 3:
                if not customButton.shipsplaced:
                    for ship1 in all_ships1:
                        ship1.checkmousehover()
                        ship1.toggle_orientation()
                if not customButton2.shipsplaced:
                    for ship2 in all_ships2:
                        ship2.checkmousehover()
                        ship2.toggle_orientation()

        elif event.type == pygame.MOUSEBUTTONUP:
            for ship1 in all_ships1:
                ship1.checkmouseclick()



            for ship2 in all_ships2:
                ship2.checkmouseclick()



    #draw line and images

    SCREEN.fill((255, 255, 255))
    imagemanager.blit_image(SCREEN, (-700, -700), imagemanager.return_last_image())
    gui.drawline(SCREEN, WHITE, (SCREEN_X/2, 0), (SCREEN_X/2, SCREEN_Y), LINE_THICKNESS,)

    if not customButton.shipsplaced:
        text_manager.createlabel('BATTLESHIPS', WHITE, 100,25)
        destroyer.drawship(50, 100, grid)
        carrier.drawship(150, 100, grid)
        patrol_boat.drawship(50, 300, grid)
        battleship.drawship(150, 300, grid)


    if not customButton2.shipsplaced:

        text_manager.createlabel('BATTLESHIPS', WHITE,SCREEN_X-240, 25)

        destroyer2.drawship(SCREEN_X - 70, 100, grid2)
        carrier2.drawship(SCREEN_X - 150, 100, grid2)
        patrol_boat2.drawship(SCREEN_X - 70, 300, grid2)
        battleship2.drawship(SCREEN_X - 150, 300, grid2)



    if customButton.shipsplaced and customButton2.shipsplaced and not copiedgrids:
        all_ships_smallergrid = {}  # Dictionary to store ships and their grid positions
        all_ships_smallergrid2 = {}
        for ship1 in all_ships1:
            ship_name = ship1.name
            shipgrids = grid_manager.shipintostate1(grid, ship1, smallergrid1)
            all_ships_smallergrid[ship_name] = shipgrids  # Store the grid positions in the dictionary

        for ship2 in all_ships2:
            ship_name2 = ship2.name
            shipgrids2 = grid_manager.shipintostate2(grid2, ship2, smallergrid2)
            all_ships_smallergrid2[ship_name2] = shipgrids2  # Store the grid positions in the dictio

        grid_manager.drawsmallergrids(SCREEN_X,SCREEN_Y)
        copiedgrids = True



    #draw buttons and label

    grid_manager.drawgrids(SCREEN_X, SCREEN_Y)

    if customButton.shipsplaced and customButton2.shipsplaced:
        grid_manager.drawsmallergrids(SCREEN_X, SCREEN_Y)

    if turn == 1:
        customButton.process()
        text_manager.createlabel('CONFIRM', WHITE, CUSTOMBUTTON_X - 375 + CUSTOMBUTTON_WIDTH / 2 + 28,
                                 CUSTOMBUTTON_Y + CUSTOMBUTTON_WIDTH / 2 - 13)


    if turn == 2:
        customButton2.process()

        text_manager.createlabel('CONFIRM', WHITE, CUSTOMBUTTON_X + 125 + CUSTOMBUTTON_WIDTH / 2 + 28,
                                 CUSTOMBUTTON_Y + CUSTOMBUTTON_WIDTH / 2 - 13)




    # Update the display
    gui.updatescreen()

# Quit Pygame
pygame.quit()
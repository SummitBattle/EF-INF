import pygame
from gui import Gui
from image_manager import ImageManager
from grid import Grid
from grid_manager import GridManager
from buttons import Button
from ships import *
from text_manager import Textmanager


# Initialize Pygame
pygame.init()

SCREEN_X = 1300
SCREEN_Y = 700
BLOCK_SIZE = 30
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
grid_manager = GridManager(grid,grid2,BLOCK_SIZE)

turn = 1


def buttonclick1():
    customButton.shipsplaced = True
    global turn
    turn = 2


def buttonclick2():
    customButton2.shipsplaced = True
    global turn
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
                if not customButton.shipsplaced:
                    for ship1 in all_ships1:
                        ship1.checkmousehover()
                        ship1.checkmouseclick()


                if not customButton2.shipsplaced:
                    for ship2 in all_ships2:
                        ship2.checkmousehover()
                        ship2.checkmouseclick()


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

    if customButton.shipsplaced:
        for ship1 in all_ships1:
            grid_manager.shipintostate1(grid,ship1)

    if customButton2.shipsplaced:
        for ship2 in all_ships2:
            grid_manager.shipintostate2(grid2,ship2)


    grid_manager.drawgrids(SCREEN_X,SCREEN_Y)

    #draw buttons and label

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


import pygame
from gui import Gui
from image_manager import Image_Manager
from grid import Grid
from grid_manager import GridManager
from button import Button
from ships import *
from textmanager import TextManager
from smallergrid import Smallergrid

# Initialize Pygame
pygame.init()

class Main:
    def __init__(self):
        self.SCREEN_X  = 1300
        self.SCREEN_Y = 700
        self.BLOCK_SIZE = 30
        self.SMALLER_BLOCK_SIZE = 10
        self.CAPTION = "SHIP WRECK"
        self.WHITE = (255,255,255)
        self.LINE_THICKNESS = 30
        self.GREEN = (0,255,0)


        self.CUSTOMBUTTON_X = self.SCREEN_X / 2
        self.CUSTOMBUTTON_Y = 500
        self.CUSTOMBUTTON_WIDTH = 50
        self.CUSTOMBUTTON_HEIGHT = 200
        self.reset_game()  # Initialize game state

    def reset_game(self):
        self.destroyed_ship = False
        self.destroyed_ship2 = False
        self.won1 = False
        self.won2 = False
        self.turn = 1
        self.copiedgrids = False
        self.create_gui()
        self.create_grids()

        self.create_imagemanager()
        self.create_ships()

        self.create_buttons()

    def create_gui(self):
        self.gui = Gui(self.SCREEN_X, self.SCREEN_Y, self.CAPTION)
        self.SCREEN = self.gui.return_screen()

    def create_imagemanager(self):
        self.imagemanager = Image_Manager()
        self.imagemanager.load_image("BACKGROUND2.jpg")
        self.imagemanager.resize_image(self.SCREEN_X, self.SCREEN_Y, self.imagemanager.return_last_image())
        self.imagemanager.blit_image(self.SCREEN, (-700, -700), self.imagemanager.return_last_image())

    def create_grids(self):
        self.grid = Grid(self.BLOCK_SIZE, self.SCREEN)
        self.grid2 = Grid(self.BLOCK_SIZE, self.SCREEN)
        self.smallergrid1 = Smallergrid(self.SMALLER_BLOCK_SIZE, self.SCREEN)
        self.smallergrid2 = Smallergrid(self.SMALLER_BLOCK_SIZE, self.SCREEN)
        self.grid_manager = GridManager(self.grid, self.grid2, self.BLOCK_SIZE, self.smallergrid1, self.smallergrid2)

    def button_click1(self):
        if self.turn == 1 and self.customButton.shipsplaced:
            self.grid_manager.check_blackgrid(self.grid, self.smallergrid2, self.all_ships_smallergrid2)
            self.smallergrid2.draw_grid(self.SCREEN_X, self.SCREEN_Y)
            destroyedships2 = self.grid_manager.find_ships_with_no_grids_left(self.all_ships_smallergrid2)

            if len(self.all_ships_smallergrid2) == 0:
                self.won1 = True
                self.won2 = False


        self.customButton.shipsplaced = True
        self.turn = 2

    def button_click2(self):
        if not hasattr(self, 'all_ships_smallergrid'):
            self.all_ships_smallergrid = {}  # Initialize if it doesn't exist
        if not hasattr(self, 'all_ships_smallergrid2'):
            self.all_ships_smallergrid2 = {}  # Initialize if it doesn't exist

        if self.turn == 2 and self.customButton2.shipsplaced:
            self.grid_manager.check_blackgrid(self.grid2, self.smallergrid1, self.all_ships_smallergrid)
            self.smallergrid1.draw_grid(self.SCREEN_X, self.SCREEN_Y)
            destroyedships = self.grid_manager.find_ships_with_no_grids_left(self.all_ships_smallergrid)

            if len(self.all_ships_smallergrid) == 0:
                self.won1 = False
                self.won2 = True

        print(self.all_ships_smallergrid)
        self.customButton2.shipsplaced = True
        self.turn = 1

    def create_buttons(self):
        self.customButton = Button(self.SCREEN, self.CUSTOMBUTTON_X - 375, self.CUSTOMBUTTON_Y, self.CUSTOMBUTTON_HEIGHT, self.CUSTOMBUTTON_WIDTH, self.button_click1)
        self.customButton2 = Button(self.SCREEN, self.CUSTOMBUTTON_X + 125, self.CUSTOMBUTTON_Y, self.CUSTOMBUTTON_HEIGHT, self.CUSTOMBUTTON_WIDTH, self.button_click2)
        self.text_manager = TextManager(self.SCREEN)

    def create_ships(self):
        self.all_ships1 = []
        self.all_ships2 = []
        self.destroyer = Destroyer(self.BLOCK_SIZE, self.SCREEN)
        self.carrier = Carrier(self.BLOCK_SIZE, self.SCREEN)
        self.patrol_boat = PatrolBoat(self.BLOCK_SIZE, self.SCREEN)
        self.battleship = Battleship(self.BLOCK_SIZE, self.SCREEN)

        self.destroyer2 = Destroyer(self.BLOCK_SIZE, self.SCREEN)
        self.carrier2 = Carrier(self.BLOCK_SIZE, self.SCREEN)
        self.patrol_boat2 = PatrolBoat(self.BLOCK_SIZE, self.SCREEN)
        self.battleship2 = Battleship(self.BLOCK_SIZE, self.SCREEN)

        self.all_ships1.append(self.destroyer)
        self.all_ships1.append(self.carrier)
        self.all_ships1.append(self.patrol_boat)
        self.all_ships1.append(self.battleship)

        self.all_ships2.append(self.destroyer2)
        self.all_ships2.append(self.carrier2)
        self.all_ships2.append(self.patrol_boat2)
        self.all_ships2.append(self.battleship2)

    def adjust_fps(self):
        # Main loop
        self.clock = pygame.time.Clock()
        self.clock.tick(90)

    def mouse_click_events(self, event):
        if event.button == 1:
            for ship1 in self.all_ships1:
                ship1.checkmousehover()
                if not self.customButton.shipsplaced:
                    ship1.checkmouseclick()

            if not self.customButton2.shipsplaced:
                for ship2 in self.all_ships2:
                    ship2.checkmousehover()
                    ship2.checkmouseclick()

            if self.turn == 1 and self.copiedgrids:
                self.grid_manager.click_on_grid(self.grid, self.SCREEN_X)

            if self.turn == 2 and self.copiedgrids:
                self.grid_manager.click_on_grid2(self.grid2, self.SCREEN_X)

        if event.button == 3:
            if not self.customButton.shipsplaced:
                for ship1 in self.all_ships1:
                    ship1.checkmousehover()
                    ship1.toggle_orientation()
            if not self.customButton2.shipsplaced:
                for ship2 in self.all_ships2:
                    ship2.checkmousehover()
                    ship2.toggle_orientation()

    def mousebutton_up_event(self):
        for ship1 in self.all_ships1:
            ship1.checkmouseclick()

        for ship2 in self.all_ships2:
            ship2.checkmouseclick()

    def draw_background_and_line(self):
        # Draw line and images
        self.SCREEN.fill((255, 255, 255))
        self.imagemanager.blit_image(self.SCREEN, (-700, -700), self.imagemanager.return_last_image())
        self.gui.draw_line(self.SCREEN, self.WHITE, (self.SCREEN_X / 2, 0), (self.SCREEN_X / 2, self.SCREEN_Y), self.LINE_THICKNESS)

    def draw_ships_and_label(self):
        if not self.customButton.shipsplaced:
            self.text_manager.create_label('BATTLESHIPS', self.WHITE, 100, 25)
            self.destroyer.drawship(50, 100, self.grid)
            self.carrier.drawship(150, 100, self.grid)
            self.patrol_boat.drawship(50, 300, self.grid)
            self.battleship.drawship(150, 300, self.grid)

        if not self.customButton2.shipsplaced:
            self.text_manager.create_label('BATTLESHIPS', self.WHITE, self.SCREEN_X - 240, 25)
            self.destroyer2.drawship(self.SCREEN_X - 70, 100, self.grid2)
            self.carrier2.drawship(self.SCREEN_X - 150, 100, self.grid2)
            self.patrol_boat2.drawship(self.SCREEN_X - 70, 300, self.grid2)
            self.battleship2.drawship(self.SCREEN_X - 150, 300, self.grid2)

        if self.customButton.shipsplaced and self.customButton2.shipsplaced and not self.copiedgrids:
            self.all_ships_smallergrid = {}  # Dictionary to store ships and their grid positions
            self.all_ships_smallergrid2 = {}
            for ship1 in self.all_ships1:
                ship_name = ship1.name
                shipgrids = self.grid_manager.ship_into_state1(self.grid, ship1, self.smallergrid1)
                self.all_ships_smallergrid[ship_name] = shipgrids  # Store the grid positions in the dictionary

            for ship2 in self.all_ships2:
                ship_name2 = ship2.name
                shipgrids2 = self.grid_manager.ship_into_state2(self.grid2, ship2, self.smallergrid2)
                self.all_ships_smallergrid2[ship_name2] = shipgrids2  # Store the grid positions in the dictionary

            self.grid_manager.draw_smallergrids(self.SCREEN_X, self.SCREEN_Y)
            self.copiedgrids = True

    def draw_smallergrids(self):
        self.grid_manager.draw_grids(self.SCREEN_X, self.SCREEN_Y)
        if self.customButton.shipsplaced and self.customButton2.shipsplaced:
            self.grid_manager.draw_smallergrids(self.SCREEN_X, self.SCREEN_Y)

    def draw_labels(self):
        if self.turn == 1:
            self.customButton.process()
            self.text_manager.create_label('CONFIRM', self.WHITE, self.CUSTOMBUTTON_X - 375 + self.CUSTOMBUTTON_WIDTH / 2 + 28,
                                           self.CUSTOMBUTTON_Y + self.CUSTOMBUTTON_WIDTH / 2 - 13)

        if self.won1:
            self.text_manager.create_label("ALL ENEMY SHIPS DESTROYED!", self.GREEN, self.SCREEN_X / 30, 50)
            self.text_manager.create_label("ALL ALLY SHIPS DESTROYED!", self.GREEN, self.SCREEN_X - self.SCREEN_X / 4, 50)

        elif self.destroyed_ship and self.turn == 1:
            self.text_manager.create_label("SHIP DESTROYED!", self.GREEN, self.SCREEN_X - self.SCREEN_X / 2.5, 50)

        if self.turn == 2:
            self.customButton2.process()
            self.text_manager.create_label('CONFIRM', self.WHITE, self.CUSTOMBUTTON_X + 125 + self.CUSTOMBUTTON_WIDTH / 2 + 28,
                                           self.CUSTOMBUTTON_Y + self.CUSTOMBUTTON_WIDTH / 2 - 13)

        if self.won2:
            self.text_manager.create_label("ALL ALLY SHIPS DESTROYED!", self.GREEN, self.SCREEN_X / 30, 50)
            self.text_manager.create_label("ALL ENEMY SHIPS DESTROYED!", self.GREEN, self.SCREEN_X - self.SCREEN_X / 4, 50)

        elif self.destroyed_ship2 and self.turn == 2:
            self.text_manager.create_label("SHIP DESTROYED!", self.GREEN, self.SCREEN_X / 3.2, 50)

        if self.won2 or self.won1:


            self.text_manager.create_label("PRESS R TO RESTART", self.GREEN, self.SCREEN_X / 10, 300)
            self.text_manager.create_label("PRESS R TO RESTART", self.GREEN, self.SCREEN_X / 20, 800)
            self.text_manager.create_label("PRESS R TO RESTART", self.GREEN, self.SCREEN_X / 1, 600)
            self.text_manager.create_label("PRESS R TO RESTART", self.GREEN, self.SCREEN_X / 6, 950)
            self.text_manager.create_label("PRESS R TO RESTART", self.GREEN, self.SCREEN_X / 20, 250)
            self.text_manager.create_label("PRESS R TO RESTART", self.GREEN, self.SCREEN_X / 30, 500)
            self.text_manager.create_label("PRESS R TO RESTART", self.GREEN, self.SCREEN_X / 1.2,350 )
            self.text_manager.create_label("PRESS R TO RESTART", self.GREEN, self.SCREEN_X / 1.5, 700)
            self.text_manager.create_label("PRESS R TO RESTART", self.GREEN, self.SCREEN_X / 1.7, 400)
            self.text_manager.create_label("PRESS R TO RESTART", self.GREEN, self.SCREEN_X / 1.9, 90)









    def update_screen(self):
        self.gui.update_screen()

    def run_game(self):
        while True:
            self.reset_game()  # Reset game state at the start of each run
            running = True

            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return

                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        self.mouse_click_events(event)

                    elif event.type == pygame.MOUSEBUTTONUP:
                        self.mousebutton_up_event()

                self.draw_background_and_line()
                self.draw_ships_and_label()
                self.draw_smallergrids()
                self.draw_labels()

                self.update_screen()

                # Check for restart condition (you can define a condition based on your game logic)
                # For demonstration, we will just simulate a restart by waiting for a key press
                keys = pygame.key.get_pressed()
                if keys[pygame.K_r]:  # Press 'R' to restart the game
                    self.reset_game()
                    break

# To run the game
main = Main()
main.run_game()
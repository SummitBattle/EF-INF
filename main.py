from gui import Gui
from imagemanager import ImageManager
from grid import Grid
from grid_manager import GridManager
from button import Button
from ships import *
from textmanager import TextManager
from smallergrid import SmallerGrid

# Initialize Pygame
pygame.init()


class Main:
    def __init__(self):
        # Arrays to collect ships
        self.all_ships1 = None
        self.all_ships2 = None
        # Dicts to store ships and grid positions from smaller grid
        self.all_ships_smaller_grid1 = {}
        self.all_ships_smaller_grid2 = {}
        # Clock to decide fps
        self.CLOCK = 60

        # Needed for game process
        self.copied_grids = None
        self.ships_overlaps1 = False
        self.ships_overlaps2 = False
        self.destroyed_ship = False
        self.destroyed_ship2 = False
        self.won1 = False
        self.won2 = False
        self.turn = 1

        # CONST Variables
        self.SCREEN_X = 1300
        self.SCREEN_Y = 700
        self.BLOCK_SIZE = 30
        self.SMALLER_BLOCK_SIZE = 10
        self.CAPTION = "SHIP WRECK"
        self.WHITE = (255, 255, 255)
        self.LINE_THICKNESS = 30
        self.GREEN = (0, 255, 0)
        self.CUSTOM_BUTTON_X = self.SCREEN_X / 2
        self.CUSTOM_BUTTON_Y = 500
        self.CUSTOM_BUTTON_WIDTH = 50
        self.CUSTOM_BUTTON_HEIGHT = 200

        # Class instances for later

        self.grid1 = None
        self.grid2 = None
        self.gui = None
        self.grid_manager = None
        self.customButton1 = None
        self.customButton2 = None
        self.image_manager = None
        self.smaller_grid1 = None
        self.smaller_grid2 = None
        self.text_manager = None
        self.patrol_boat1 = None
        self.patrol_boat2 = None
        self.destroyer1 = None
        self.destroyer2 = None
        self.carrier1 = None
        self.carrier2 = None
        self.battleship1 = None
        self.battleship2 = None

        # Screen instance
        self.SCREEN = None

        # This creates all instances
        self.setup_game()

    def setup_game(self):
        """
        Calls and resets all needed variables.
        :return: None
        :rtype: None
        """
        self.destroyed_ship = False
        self.destroyed_ship2 = False
        self.won1 = False
        self.won2 = False
        self.turn = 1
        self.copied_grids = False

        self.create_gui()
        self.create_grids()

        self.create_image_manager()
        self.create_ships()

        self.create_buttons()

    def create_gui(self):
        """
        Creates screen.
        :return: None
        :rtype: None
        """
        self.gui = Gui(self.SCREEN_X, self.SCREEN_Y, self.CAPTION)
        self.SCREEN = self.gui.return_screen()

    def create_image_manager(self):
        """
        Creates image_manager and draws background.
        :return: None
        :rtype: None
        """
        self.image_manager = ImageManager()
        self.image_manager.load_image("BACKGROUND2.jpg")
        self.image_manager.resize_image(self.SCREEN_X, self.SCREEN_Y, self.image_manager.return_last_image())
        self.image_manager.blit_image(self.SCREEN, (-700, -700), self.image_manager.return_last_image())

    def create_grids(self):
        """
        Creates big and small grids.
        :return: None
        :rtype: None
        """
        self.grid1 = Grid(self.BLOCK_SIZE, self.SCREEN)
        self.grid2 = Grid(self.BLOCK_SIZE, self.SCREEN)
        self.smaller_grid1 = SmallerGrid(self.SMALLER_BLOCK_SIZE, self.SCREEN)
        self.smaller_grid2 = SmallerGrid(self.SMALLER_BLOCK_SIZE, self.SCREEN)
        self.grid_manager = GridManager(self.grid1, self.grid2, self.BLOCK_SIZE, self.smaller_grid1, self.smaller_grid2)

    def button_click1(self):
        """
        Events if left button gets pressed.
        :return: None
        :rtype: None
        """

        # Boolean if ship was hit
        ship_hit = False

        # Boolean if there is a black grid
        black_grids = self.grid1.return_black_grids()
        black_grid_exists = False
        if black_grids:
            black_grid_exists = True

        all_ships_placed = True  # Assume all ships are placed at first
        # Draws smaller grid and checks for selected grids
        if self.turn == 1 and self.customButton1.ships_placed:
            ship_hit = (self.grid_manager.check_blackgrid(self.grid1, self.smaller_grid2, self.all_ships_smaller_grid2))

            self.smaller_grid2.draw_grid(self.SCREEN_X, self.SCREEN_Y)
            destroyed_ships2 = self.grid_manager.find_ships_with_no_grids_left(self.all_ships_smaller_grid2)
            # Checks if any ships are left
            if len(self.all_ships_smaller_grid2) == 0:
                self.won1 = True
                self.won2 = False

            if len(destroyed_ships2) >= 1:
                self.destroyed_ship2 = True
            else:
                self.destroyed_ship2 = False
        if not self.customButton1.ships_placed:
            # Change turn and check if all ships were placed

            for ship1 in self.all_ships1:
                # Check if all ships were placed properly
                ship_list = ship1.check_overlap(self.grid1)

                # Check for overlaps between ships with 1 grid distance
                self.ships_overlaps1 = self.grid_manager.check_ship_ship_overlap(ship1, self.all_ships1)

                if not ship_list:  # If any ship is not placed correctly
                    all_ships_placed = False  # Set flag to False
                    break  # Exit the loop early if a ship isn't placed correctly

        # After all ships were placed and no ships are overlapping
        if all_ships_placed and not self.copied_grids and not self.ships_overlaps1:
            self.customButton1.ships_placed = True
            self.turn = 2

        # Repeat turn if a ship was hit
        if ship_hit:
            self.turn = 1
        # Change turn only if a black grid exists
        elif black_grid_exists:

            self.turn = 2

    def button_click2(self):
        """
        Events if right button is clicked.
        :return: None
        :rtype:  None
        """
        ship_hit = False
        black_grids = self.grid2.return_black_grids()
        black_grid_exists = False
        if black_grids:
            black_grid_exists = True
        all_ships_placed = True  # Assume all ships are placed at first

        # Draw smaller grid and check for black grids
        if self.turn == 2 and self.customButton2.ships_placed:
            ship_hit = self.grid_manager.check_blackgrid(self.grid2, self.smaller_grid1, self.all_ships_smaller_grid1)
            self.smaller_grid1.draw_grid(self.SCREEN_X, self.SCREEN_Y)
            destroyed_ships = self.grid_manager.find_ships_with_no_grids_left(self.all_ships_smaller_grid1)

            # Check if somebody won
            if len(self.all_ships_smaller_grid1) == 0:
                self.won1 = False
                self.won2 = True
            if len(destroyed_ships) >= 1:
                self.destroyed_ship = True
            else:
                self.destroyed_ship = False

        # Check if all ships were placed and change turn
        if not self.customButton2.ships_placed:
            for ship2 in self.all_ships2:
                ship_list = ship2.check_overlap(self.grid2)
                self.ships_overlaps2 = self.grid_manager.check_ship_ship_overlap(ship2, self.all_ships2)
                if not ship_list:  # If any ship is not placed correctly
                    all_ships_placed = False  # Set flag to False
                    break  # Exit the loop early if a ship isn't placed correctly

        # Only change turn if all ships are placed correctly
        if all_ships_placed and not self.copied_grids and not self.ships_overlaps2:
            self.customButton2.ships_placed = True
            self.turn = 1
        if ship_hit:
            self.turn = 2
        elif black_grid_exists:
            self.turn = 1

    def create_buttons(self):
        """
        Create buttons and text manager.
        :return: None
        :rtype: None
        """

        self.customButton1 = Button(self.SCREEN, self.CUSTOM_BUTTON_X - 375, self.CUSTOM_BUTTON_Y,
                                    self.CUSTOM_BUTTON_HEIGHT,
                                    self.CUSTOM_BUTTON_WIDTH, self.button_click1)

        self.customButton2 = Button(self.SCREEN, self.CUSTOM_BUTTON_X + 125, self.CUSTOM_BUTTON_Y,
                                    self.CUSTOM_BUTTON_HEIGHT,
                                    self.CUSTOM_BUTTON_WIDTH, self.button_click2)
        self.text_manager = TextManager(self.SCREEN)

    def create_ships(self):
        """
        Creates all ships and adds them to list.
        :return: None
        :rtype: None
        """
        # Create ships
        self.all_ships1 = []
        self.all_ships2 = []
        self.destroyer1 = Destroyer(self.BLOCK_SIZE, self.SCREEN)
        self.carrier1 = Carrier(self.BLOCK_SIZE, self.SCREEN)
        self.patrol_boat1 = PatrolBoat(self.BLOCK_SIZE, self.SCREEN)
        self.battleship1 = Battleship(self.BLOCK_SIZE, self.SCREEN)

        self.destroyer2 = Destroyer(self.BLOCK_SIZE, self.SCREEN)
        self.carrier2 = Carrier(self.BLOCK_SIZE, self.SCREEN)
        self.patrol_boat2 = PatrolBoat(self.BLOCK_SIZE, self.SCREEN)
        self.battleship2 = Battleship(self.BLOCK_SIZE, self.SCREEN)
        # Append ships
        self.all_ships1.append(self.destroyer1)
        self.all_ships1.append(self.carrier1)
        self.all_ships1.append(self.patrol_boat1)
        self.all_ships1.append(self.battleship1)

        self.all_ships2.append(self.destroyer2)
        self.all_ships2.append(self.carrier2)
        self.all_ships2.append(self.patrol_boat2)
        self.all_ships2.append(self.battleship2)

    def adjust_fps(self):
        """
        Adjusts fps.
        :return: None
        :rtype: None
        """
        # Main loop
        self.CLOCK = pygame.time.Clock()
        self.CLOCK.tick(90)

    def mouse_click_events(self, event):
        """
        Events if button gets clicked.
        :param event: All events like quit, mouse input and keyboard input
        :type event: event
        :return: None
        :rtype: None
        """
        # 1 equals left click
        # Check for hovers and clicks for right and left ships
        if event.button == 1:
            for ship1 in self.all_ships1:
                ship1.check_mouse_hover()
                if not self.customButton1.ships_placed:
                    ship1.check_mouseclick()

            if not self.customButton2.ships_placed:
                for ship2 in self.all_ships2:
                    ship2.check_mouse_hover()
                    ship2.check_mouseclick()
            # Allows to select grids for left and right side
            if self.turn == 1 and self.copied_grids:
                self.grid_manager.click_on_grid(self.grid1, self.SCREEN_X)

            if self.turn == 2 and self.copied_grids:
                self.grid_manager.click_on_grid2(self.grid2, self.SCREEN_X)
        # 3 equals right click

        if event.button == 3:
            if not self.customButton1.ships_placed:
                for ship1 in self.all_ships1:
                    ship1.check_mouse_hover()
                    ship1.toggle_orientation()
            if not self.customButton2.ships_placed:
                for ship2 in self.all_ships2:
                    ship2.check_mouse_hover()
                    ship2.toggle_orientation()

    def mouse_button_up_event(self):
        """
        Events when mouse button gets lifted.
        :return: None
        :rtype: None
        """
        # Allows dis-attaching of ships after clicking them
        for ship1 in self.all_ships1:
            ship1.check_mouseclick()

        for ship2 in self.all_ships2:
            ship2.check_mouseclick()

    def draw_background_and_line(self):
        """
        Draws background and line in middle.
        :return: None
        :rtype: None
        """
        # Draw line and images
        self.SCREEN.fill((255, 255, 255))
        self.image_manager.blit_image(self.SCREEN, (-700, -700), self.image_manager.return_last_image())
        self.gui.draw_line(self.SCREEN, self.WHITE, (self.SCREEN_X / 2, 0), (self.SCREEN_X / 2, self.SCREEN_Y),
                           self.LINE_THICKNESS)

    def draw_ships_and_label(self):
        """
        Draws all ships on screen and text.
        :return: None
        :rtype: None
        """

        # If ships were not placed yet, draw ships
        if not self.customButton1.ships_placed:
            self.text_manager.create_label('BATTLESHIPS', self.WHITE, 100, 25)
            self.destroyer1.draw_ship(50, 100, self.grid1)
            self.carrier1.draw_ship(150, 100, self.grid1)
            self.patrol_boat1.draw_ship(50, 300, self.grid1)
            self.battleship1.draw_ship(150, 300, self.grid1)

        if not self.customButton2.ships_placed:
            self.text_manager.create_label('BATTLESHIPS', self.WHITE, self.SCREEN_X - 240, 25)
            self.destroyer2.draw_ship(self.SCREEN_X - 70, 100, self.grid2)
            self.carrier2.draw_ship(self.SCREEN_X - 150, 100, self.grid2)
            self.patrol_boat2.draw_ship(self.SCREEN_X - 70, 300, self.grid2)
            self.battleship2.draw_ship(self.SCREEN_X - 150, 300, self.grid2)

        # If ships were placed, turn ships into state 1 and draws smaller grids ONCE

        if self.customButton1.ships_placed and self.customButton2.ships_placed and not self.copied_grids:

            for ship1 in self.all_ships1:
                ship_name = ship1.name
                ship_grids = self.grid_manager.ship_into_state1(self.grid1, ship1, self.smaller_grid1)
                self.all_ships_smaller_grid1[ship_name] = ship_grids  # Store the grid positions in the dictionary

            for ship2 in self.all_ships2:
                ship_name2 = ship2.name
                ship_grids2 = self.grid_manager.ship_into_state2(self.grid2, ship2, self.smaller_grid2)
                self.all_ships_smaller_grid2[ship_name2] = ship_grids2  # Store the grid positions in the dictionary

            self.grid_manager.draw_smaller_grids(self.SCREEN_X, self.SCREEN_Y)
            self.copied_grids = True

    def draw_smaller_grids(self):
        """
        Draws smaller grids and bigger grids.
        :return: None
        :rtype: None
        """
        self.grid_manager.draw_grids(self.SCREEN_X)
        if self.customButton1.ships_placed and self.customButton2.ships_placed:
            self.grid_manager.draw_smaller_grids(self.SCREEN_X, self.SCREEN_Y)

    def draw_labels(self):
        """
        Draws all text on screen.
        :return: None
        :rtype: None
        """

        # Text for Buttons
        if self.turn == 1:
            self.customButton1.process()
            self.text_manager.create_label('CONFIRM', self.WHITE,
                                           self.CUSTOM_BUTTON_X - 375 + self.CUSTOM_BUTTON_WIDTH / 2 + 28,
                                           self.CUSTOM_BUTTON_Y + self.CUSTOM_BUTTON_WIDTH / 2 - 13)
            self.gui.cover_right_side(self.SCREEN)

        if self.turn == 2:
            self.customButton2.process()
            self.text_manager.create_label('CONFIRM', self.WHITE,
                                           self.CUSTOM_BUTTON_X + 125 + self.CUSTOM_BUTTON_WIDTH / 2 + 28,
                                           self.CUSTOM_BUTTON_Y + self.CUSTOM_BUTTON_WIDTH / 2 - 13)
            self.gui.cover_left_side(self.SCREEN)

        # When ship got destroyed
        if self.destroyed_ship2 and self.turn == 1:
            self.text_manager.create_label("SHIP DESTROYED!", self.GREEN, self.SCREEN_X / 4, 50)

        if self.destroyed_ship and self.turn == 2:
            self.text_manager.create_label("SHIP DESTROYED!", self.GREEN, self.SCREEN_X / 1.5, 50)

        if self.ships_overlaps1:
            self.text_manager.create_label("NO TOUCHING SHIPS!", self.GREEN, self.SCREEN_X / 4, 50)

        if self.ships_overlaps2:
            self.text_manager.create_label("NO TOUCHING SHIPS!", self.GREEN, self.SCREEN_X / 1.5, 50)

        if self.won2 or self.won1:
            self.text_manager.create_label("PRESS R TO RESTART", self.GREEN, self.SCREEN_X / 2 - 120, 300)

    def update_screen(self):
        """
        Updates screen to next frame.
        :return: None
        :rtype: None
        """
        self.gui.update_screen()

    def draw_elements(self):
        self.draw_background_and_line()
        self.draw_ships_and_label()
        self.draw_smaller_grids()
        self.draw_labels()

        self.update_screen()

    def run_game(self):
        """
        Main loop of Game.
        :return: None
        :rtype: None
        """
        while True:
            self.setup_game()  # Reset game state at the start of each run
            running = True

            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return

                    elif event.type == pygame.MOUSEBUTTONDOWN:  # Checks for mouse clicks
                        self.mouse_click_events(event)

                    elif event.type == pygame.MOUSEBUTTONUP:  # Events after mouse got clicked
                        self.mouse_button_up_event()

                # Events that happen every frame

                self.draw_elements()

                # Check for restart condition
                keys = pygame.key.get_pressed()
                if keys[pygame.K_r]:  # Press 'R' to restart the game
                    self.setup_game()
                    break


# To run the game


main = Main()
main.run_game()

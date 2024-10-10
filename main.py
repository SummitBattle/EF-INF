import pygame
from GraphicInterFace.gui import Gui
from Grids.grid import Grid
from Grids.gridmanager import GridManager
from Grids.smallergrid import SmallerGrid
from GraphicInterFace.button import Button
from Ships.ships import Destroyer, Carrier, PatrolBoat, Battleship
from gameconfig import GameConfig

# Initialize Pygame
pygame.init()


class Main:
    """
    The Main class is responsible for managing the game state and flow
    in a Battleship-style game.

    Attributes:
        all_ships1 (list): List of all ships for Player 1.
        all_ships2 (list): List of all ships for Player 2.
        all_ships_smaller_grid1 (dict): Dictionary of ships for Player 1 with their grid positions.
        all_ships_smaller_grid2 (dict): Dictionary of ships for Player 2 with their grid positions.
        copied_grids (bool): Indicates if the grid state has been copied.
        ships_overlaps1 (bool): Indicates if ships for Player 1 overlap.
        ships_overlaps2 (bool): Indicates if ships for Player 2 overlap.
        destroyed_ship (bool): Indicates if a ship has been destroyed for Player 1.
        destroyed_ship2 (bool): Indicates if a ship has been destroyed for Player 2.
        won1 (bool): Indicates if Player 1 has won.
        won2 (bool): Indicates if Player 2 has won.
        turn (int): Indicates the current player's turn (1 or 2).
        screen (Surface): Pygame surface for the game screen.

        Rest are all instances of their respective classes.
    """

    def __init__(self):
        """
        Initialize the Main instance.
        """

        # Dicts to store ships and grid positions from smaller grid
        self.all_ships_smaller_grid1 = {}
        self.all_ships_smaller_grid2 = {}

        # Needed for game process
        self.copied_grids = None
        self.ships_overlaps1 = False
        self.ships_overlaps2 = False
        self.destroyed_ship = False
        self.destroyed_ship2 = False
        self.won1 = None
        self.won2 = None
        self.turn = 1

        # CONST Variables
        self.config = GameConfig()

        # Class instances placeholders

        self.grid1 = None
        self.grid2 = None
        self.gui = None
        self.grid_manager = None
        self.customButton1 = None
        self.customButton2 = None
        self.smaller_grid1 = None
        self.smaller_grid2 = None

        self.patrol_boat1 = None
        self.patrol_boat2 = None
        self.destroyer1 = None
        self.destroyer2 = None
        self.carrier1 = None
        self.carrier2 = None
        self.battleship1 = None
        self.battleship2 = None
        # Arrays to collect ships
        self.all_ships1 = None
        self.all_ships2 = None

        # Screen instance
        self.screen = None
        # Sets needed variables for game
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

        self.create_ships()

        self.create_buttons()

    def create_gui(self):
        """
        Creates screen.
        :return: None
        :rtype: None
        """
        self.gui = Gui(self.config.SCREEN_X, self.config.SCREEN_Y, self.config.CAPTION)
        self.screen = self.gui.return_screen()

        self.gui.load_image("BACKGROUND2.jpg")
        self.gui.resize_image(self.gui.return_last_image(), self.config.SCREEN_X, self.config.SCREEN_Y,
                              )

        self.gui.draw_image(self.gui.return_last_image(), -700, -700)

    def create_grids(self):
        """
        Creates big and small grids.
        :return: None
        :rtype: None
        """
        self.grid1 = Grid(self.config.BLOCK_SIZE, self.screen)
        self.grid2 = Grid(self.config.BLOCK_SIZE, self.screen)
        self.smaller_grid1 = SmallerGrid(self.config.SMALLER_BLOCK_SIZE, self.screen)
        self.smaller_grid2 = SmallerGrid(self.config.SMALLER_BLOCK_SIZE, self.screen)
        self.grid_manager = GridManager(self.grid1, self.grid2, self.config.BLOCK_SIZE, self.smaller_grid1,
                                        self.smaller_grid2, self.config.SCREEN_X)

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

        all_ships_placed = True
        # Draws smaller grid and checks for selected grids
        if self.turn == 1 and self.customButton1.ships_placed:
            ship_hit = (self.grid_manager.check_blackgrid(self.grid1, self.smaller_grid2, self.all_ships_smaller_grid2))

            self.smaller_grid2.draw_grid(self.config.SCREEN_X, self.config.SCREEN_Y)
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
        all_ships_placed = True

        # Draw smaller grid and check for black grids
        if self.turn == 2 and self.customButton2.ships_placed:
            ship_hit = self.grid_manager.check_blackgrid(self.grid2, self.smaller_grid1, self.all_ships_smaller_grid1)
            self.smaller_grid1.draw_grid(self.config.SCREEN_X, self.config.SCREEN_Y)
            destroyed_ships = self.grid_manager.find_ships_with_no_grids_left(self.all_ships_smaller_grid1)

            # Check if somebody won
            print(self.all_ships_smaller_grid1)
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

        self.customButton1 = Button(self.screen, self.config.CUSTOM_BUTTON_X - 375, self.config.CUSTOM_BUTTON_Y,
                                    self.config.CUSTOM_BUTTON_HEIGHT,
                                    self.config.CUSTOM_BUTTON_WIDTH, self.button_click1)

        self.customButton2 = Button(self.screen, self.config.CUSTOM_BUTTON_X + 125, self.config.CUSTOM_BUTTON_Y,
                                    self.config.CUSTOM_BUTTON_HEIGHT,
                                    self.config.CUSTOM_BUTTON_WIDTH, self.button_click2)

    def create_ships(self):
        """
        Creates all ships and adds them to list.
        :return: None
        :rtype: None
        """
        # Create ships
        self.all_ships1 = []
        self.all_ships2 = []
        self.destroyer1 = Destroyer(self.config.BLOCK_SIZE, self.screen)
        self.carrier1 = Carrier(self.config.BLOCK_SIZE, self.screen)
        self.patrol_boat1 = PatrolBoat(self.config.BLOCK_SIZE, self.screen)
        self.battleship1 = Battleship(self.config.BLOCK_SIZE, self.screen)

        self.destroyer2 = Destroyer(self.config.BLOCK_SIZE, self.screen)
        self.carrier2 = Carrier(self.config.BLOCK_SIZE, self.screen)
        self.patrol_boat2 = PatrolBoat(self.config.BLOCK_SIZE, self.screen)
        self.battleship2 = Battleship(self.config.BLOCK_SIZE, self.screen)
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
        clock = pygame.time.Clock()
        clock.tick(90)

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
                self.grid_manager.click_on_grid(1)

            if self.turn == 2 and self.copied_grids:
                self.grid_manager.click_on_grid(2)
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
        self.screen.fill((255, 255, 255))
        self.gui.draw_image(self.gui.return_last_image(), -700, -700, )
        self.gui.draw_line(self.config.WHITE, (self.config.SCREEN_X / 2, 0),
                           (self.config.SCREEN_X / 2, self.config.SCREEN_Y),
                           self.config.LINE_THICKNESS)

    def draw_ships_and_label(self):
        """
        Draws all ships on screen and text.
        :return: None
        :rtype: None
        """

        # If ships were not placed yet, draw ships
        if not self.customButton1.ships_placed:
            self.gui.create_label('BATTLESHIPS', self.config.WHITE, 100, 25)
            self.destroyer1.draw_ship(50, 100, self.grid1,1)
            self.carrier1.draw_ship(150, 100, self.grid1,1)
            self.patrol_boat1.draw_ship(50, 300, self.grid1,1)
            self.battleship1.draw_ship(150, 300, self.grid1,1)

        if not self.customButton2.ships_placed:
            self.gui.create_label('BATTLESHIPS', self.config.WHITE, self.config.SCREEN_X - 240, 25)
            self.destroyer2.draw_ship(self.config.SCREEN_X - 70, 100, self.grid2, 2)
            self.carrier2.draw_ship(self.config.SCREEN_X - 150, 100, self.grid2, 2)
            self.patrol_boat2.draw_ship(self.config.SCREEN_X - 70, 300, self.grid2, 2)
            self.battleship2.draw_ship(self.config.SCREEN_X - 150, 300, self.grid2, 2)

        # If ships were placed, turn ships into state 1 and draws smaller grids ONCE

        if self.customButton1.ships_placed and self.customButton2.ships_placed and not self.copied_grids:

            for ship1 in self.all_ships1:
                ship_name = ship1.name
                ship_grids = self.grid_manager.ship_into_state(self.grid1, ship1, 1)
                self.all_ships_smaller_grid1[ship_name] = ship_grids  # Store the grid positions in the dictionary

            for ship2 in self.all_ships2:
                ship_name2 = ship2.name
                ship_grids2 = self.grid_manager.ship_into_state(self.grid2, ship2, 2)
                self.all_ships_smaller_grid2[ship_name2] = ship_grids2  # Store the grid positions in the dictionary

            self.grid_manager.draw_smaller_grids(self.config.SCREEN_Y)
            self.copied_grids = True

    def draw_smaller_grids(self):
        """
        Draws smaller grids and bigger grids.
        :return: None
        :rtype: None
        """
        self.grid_manager.draw_grids()
        if self.customButton1.ships_placed and self.customButton2.ships_placed:
            self.grid_manager.draw_smaller_grids(self.config.SCREEN_Y)

    def draw_labels(self):
        """
        Draws all text on screen.
        :return: None
        :rtype: None
        """

        # Text for Buttons
        if self.turn == 1:
            self.customButton1.process()
            self.gui.create_label('CONFIRM', self.config.WHITE,
                                  self.config.CUSTOM_BUTTON_X - 375 + self.config.CUSTOM_BUTTON_WIDTH / 2 + 28,
                                  self.config.CUSTOM_BUTTON_Y + self.config.CUSTOM_BUTTON_WIDTH / 2 - 13)
            if not self.won1 or not self.won2:
                self.gui.cover_right_side()

        if self.turn == 2:
            self.customButton2.process()
            self.gui.create_label('CONFIRM', self.config.WHITE,
                                  self.config.CUSTOM_BUTTON_X + 125 + self.config.CUSTOM_BUTTON_WIDTH / 2 + 28,
                                  self.config.CUSTOM_BUTTON_Y + self.config.CUSTOM_BUTTON_WIDTH / 2 - 13)
            if not self.won1 or not self.won2:
                self.gui.cover_left_side()

        # If ship was destroyed
        if self.destroyed_ship2 and self.turn == 1:
            self.gui.create_label("SHIP DESTROYED!", self.config.GREEN, self.config.SCREEN_X / 4, 50)

        if self.destroyed_ship and self.turn == 2:
            self.gui.create_label("SHIP DESTROYED!", self.config.GREEN, self.config.SCREEN_X / 1.5, 50)

        # If ships are overlapping
        if self.ships_overlaps1:
            self.gui.create_label("NO TOUCHING SHIPS!", self.config.GREEN, self.config.SCREEN_X / 4, 50)

        if self.ships_overlaps2:
            self.gui.create_label("NO TOUCHING SHIPS!", self.config.GREEN, self.config.SCREEN_X / 1.5, 50)

        # If someone won
        if self.won2 or self.won1:
            self.gui.create_label("PRESS R TO RESTART", self.config.GREEN, self.config.SCREEN_X / 2 - 120, 300)

    def update_screen(self):
        """
        Updates screen to next frame.
        :return: None
        :rtype: None
        """
        self.gui.update_screen()

    def draw_elements(self):
        """
        Draws line,background,ships,labels and smaller_grids on the screen.
        :return: None
        :rtype: None
        """
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

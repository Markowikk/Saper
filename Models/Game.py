import re
from Board import Board
from Point import Point
from typing import Dict, Tuple
from ContentOfField import ContentOfField


class Game:
    def __init__(self, filename="saperSavedGame"):
        self.filename = filename

    def save_game(self, board: Board):
        """
        Save the current state of the game to a file.
        The first line of the file contains the size of the board.
        Each subsequent line contains the coordinates, status, and mark of each point.

        :param board: The Board object containing the game state
        :return: None
        """
        try:
            with open(self.filename, "w") as file:
                # Write the size of the board on the first line
                file.write(f"{board.x} {board.y}\n")
                # Write each point and its status on subsequent lines
                for k, p in board.board.items():
                    file.write(f"{k[0]},{k[1]};{p.status.name};{p.mark.name}\n")
                print("The game has been saved")
        except IOError as e:
            print(e)

    def load_game(self, board: Board):
        """
        Load the game state from a file.
        The first line of the file contains the size of the board.
        Each subsequent line contains the coordinates, status, and mark of each point.

        :param board: The Board object to load the game state into
        :return: None
        """
        res: Dict[Tuple[int, int], Point] = {}
        try:
            with open(self.filename, "r") as file:
                # Read the size of the board from the first line
                first_line = file.readline().strip()
                board.x, board.y = map(int, first_line.split())
                board.validation_board_size()
                # Read the points and their statuses from subsequent lines
                regexPattern = r"(\d+),(\d+);(\w+);(\w+)"
                for line in file:
                    match = re.search(regexPattern, line)
                    if match:
                        x = int(match.group(1))
                        y = int(match.group(2))
                        status = ContentOfField[match.group(3)]
                        mark = ContentOfField[match.group(4)]
                        p = Point(x, y, status)
                        p.mark_point(mark)
                        res[(x, y)] = p
        finally:
            print("The game has been loaded")
        board.board = res


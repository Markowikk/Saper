import re
import random
from Point import Point
from typing import Dict, Tuple
from ContentOfField import ContentOfField


class Board:
    """
    This class represents a Board

    Attributes:
        x (int): The x size of the board
        y (int): The y size of the board
    """

    def __init__(self, x, y):
        """
        Initialize the new Board object
        :param x: Size of the x dimension of the board
        :param y: Size of the y dimension of the board
        """
        self.x = x
        self.y = y
        self.board: Dict[Tuple[int, int], Point] = {}
        self.saveFileName = "saperSavedGame"

    def create_board(self):
        """
        Create the new board and add it to the boards dict
        :return: None
        """
        for y in range(0, self.y):
            for x in range(0, self.x):
                p = Point(x, y, ContentOfField.EMPTY)
                self.board[(x, y)] = p

    def save_game(self):
        try:
            with open(self.saveFileName, "w") as file:
                for k, p in self.board.items():
                    file.write(f"{p};{p.status}\n")
                print("The game has been saved")
        except IOError as e:
            print(e)

    def load_game(self):
        res: Dict[Tuple[int, int], Point] = {}
        try:
            with open(self.saveFileName, "r") as file:
                regexPattern = r"\|(\d+):(\d+)\|\;ContentOfField\.(\w+)"
                for line in file:
                    from typing import re
                    match = re.search(regexPattern, line)
                    if match:
                        x = int(match.group(1))
                        y = int(match.group(2))
                        status = ContentOfField[match.group(3)]
                        p = Point(x, y, status)
                        res[(x, y)] = p
        finally:
            print("The game has been loaded")
        self.board = res

    def print_board(self):
        """
        Print the board
        :return: None
        """
        for y in range(self.y):
            for x in range(self.x):
                print(self.board[(x, y)], end='')
            print('')

    def insert_bombs(self, bombs):
        for b in range(0, bombs):
            while (True):
                randomX = random.randint(0, self.x - 1)
                randomY = random.randint(0, self.y - 1)
                if self.board[randomX, randomY].status != ContentOfField.BOMB:
                    self.board[randomX, randomY].put_bomb()
                    self.add_bombs_to_neighbor_points(randomX, randomY)
                    break

    def test(self):
        for y in range(0, self.y):
            for x in range(0, self.x):
                self.get_point(x, y)

    def check_point(self, x, y):
        try:
            self.board[x, y].change_outlook()
        except:
            print("NO such point")

    def add_bombs_to_neighbor_points(self, x, y):
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx = x + dx
                ny = y + dy
                if 0 <= nx < self.x and 0 <= ny < self.y:
                    neighbor_point = self.board.get((nx, ny))
                    if neighbor_point and neighbor_point.status != ContentOfField.BOMB:
                        neighbor_point.add_bomb_neighbor()

    def mark_point(self, x, y):
        try:
            self.check_point(x, y)
        except Exception as e:
            return
        # dodac dawanie flagi albo zaznaczanie

    def get_point(self, x, y):
        """
        Change te status of the specific point fromt the board
        :param x: val x of the point
        :param y: val y of the point
        :return: None
        """
        try:
            p = self.board.get((x, y))
            p.change_outlook()
            self.board[(x, y)] = p
        except KeyError:
            print("no such point")

from Point import Point
from typing import List, Dict, Tuple
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

    def create_board(self):
        for y in range(0, self.y):
            for x in range(0, self.x):
                p = Point(x, y, ContentOfField.BOMB)
                self.board[(x, y)] = p

    def print_board(self):
        for y in range(self.y):
            for x in range(self.x):
                print(self.board[(x, y)], end='')
            print('')

    def check_point(self, x, y):
        try:
            p = self.board.get((x, y))
            p.change_outlook()
            self.board[(x, y)] = p
        except KeyError:
            print("no such point")

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

    def create_board(self):
        """
        Create the new board and add it to the boards dict
        :return: None
        """
        for y in range(0, self.y):
            for x in range(0, self.x):
                p = Point(x, y, ContentOfField.EMPTY)
                self.board[(x, y)] = p

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
                print(randomX)
                print(randomY)
                print("LLLLLLLLLLLLLLLL")
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
                if 0 <= nx < self.x and 0 <= ny < self.y and self.board.get((nx, ny)).status == ContentOfField.BOMB:
                    self.board[(nx, ny)].add_bomb_neighbor()

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

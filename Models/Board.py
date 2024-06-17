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
        self.validation_board_size()
        self.board: Dict[Tuple[int, int], Point] = {}
        self.saveFileName = "saperSavedGame"
        self.game_over = False

    def create_board(self):
        """
        Create the new board and add it to the boards dict
        :return: None
        """
        for y in range(0, self.y):
            for x in range(0, self.x):
                p = Point(x, y, ContentOfField.EMPTY)
                self.board[(x, y)] = p

    def validation_board_size(self):
        """
            Validate the size of the board. The minimum size is 5x5.
            If the size is smaller, prompt the user to enter a new size until it is valid.

            :return: None
            """
        while self.x < 5 or self.y < 5:
            print("Board is too small. Board size must be at least 5x5.")
            new_x = int(input("Enter board size x: "))
            self.x = new_x
            new_y = int(input("Enter board size y: "))
            self.y = new_y

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
        """
        Insert bombs randomly on the board
        :param bombs: Number of bombs to insert
        :return: None
        """
        bombs = self.validation_number_of_bombs(bombs)
        for b in range(0, bombs):
            while (True):
                randomX = random.randint(0, self.x - 1)
                randomY = random.randint(0, self.y - 1)
                if self.board[randomX, randomY].status != ContentOfField.BOMB:
                    self.board[randomX, randomY].put_bomb()
                    self.add_bombs_to_neighbor_points(randomX, randomY)
                    break

    def validation_number_of_bombs(self, number_of_bombs):
        """
        Validate the number of bombs to ensure it is within the allowed range.
        The number of bombs must be at least 1 and no more than half the number of fields.

        :param number_of_bombs: Number of bombs to validate
        :return: Validated number of bombs
        """
        number_of_fields = self.x * self.y
        max_number_of_bombs = number_of_fields // 2
        while max_number_of_bombs < number_of_bombs or number_of_bombs < 1:
            print("Wrong amount of bombs. Maximum number of bombs is " + str(max_number_of_bombs) + " Minimum number of bombs is 1.")
            number_of_bombs = int(input("Enter number of bombs: "))
        return number_of_bombs

    def check_point(self, x, y):
        """
        Check the status of the point at (x, y)
        :param x: x-coordinate of the point
        :param y: y-coordinate of the point
        :return: True if no bomb is hit, False otherwise
        """
        try:
            if self.check_for_bomb(x, y):
                print("Bomb hit! GAME OVER.")
                return False
            self.board[x, y].change_outlook()
            self.reveal_empty_neighbors(x, y)
            return True
        except:
            print("No such point")
            return False

    def check_for_bomb(self, x, y):
        """
        Check if there is a bomb at the given coordinates
        :param x: x-coordinate
        :param y: y-coordinate
        :return: True if there is a bomb, False otherwise
        """
        return self.board[(x, y)].is_bomb()

    def reveal_empty_neighbors(self, x, y):
        """
        Reveal empty neighbors recursively
        :param x: x coordinate
        :param y: y coordinate
        :return: None
        """
        stack = [(x, y)]
        visited = set()

        while stack:
            cx, cy = stack.pop()
            if (cx, cy) in visited:
                continue
            visited.add((cx, cy))

            point = self.board.get((cx, cy))
            if point and point.status == ContentOfField.EMPTY:
                point.change_outlook()
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < self.x and 0 <= ny < self.y:
                            neighbor = self.board.get((nx, ny))
                            if neighbor and neighbor.status == ContentOfField.EMPTY:
                                stack.append((nx, ny))
                            elif neighbor:
                                neighbor.change_outlook()

    def add_bombs_to_neighbor_points(self, x, y):
        """
        Increment the bomb neighbor count for all points adjacent to (x, y).

        :param x: x-coordinate of the bomb
        :param y: y-coordinate of the bomb
        :return: None
        """
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

    def question_mark_point(self, x, y):
        """
        Mark a point with a question mark on the board.

        :param x: x-coordinate of the point
        :param y: y-coordinate of the point
        :return: None
        """
        try:
            self.board[x, y].mark_point(ContentOfField.QUESTIONMARK)
            print(f"Point ({x}, {y}) marked.")
        except KeyError:
            print("No such point to mark.")

    def flag_point(self, x, y):
        """
        Flag a point on the board.
        :param x: x-coordinate of the point
        :param y: y-coordinate of the point
        :return: None
        """
        try:
            self.board[x, y].mark_point(ContentOfField.FLAG)
            print(f"Point ({x}, {y}) flagged.")
        except KeyError:
            print("No such point to flag.")

    def check_all_bombs_flagged(self):
        """
        Check if all bomb points have been flagged.
        End the game if all bombs are flagged.
        :return: None
        """
        all_flagged = True
        for point in self.board.values():
            if point.status == ContentOfField.BOMB and point.mark != ContentOfField.FLAG:
                all_flagged = False
                break
        if all_flagged:
            self.game_over = True
            print("All bombs have been flagged. Game over!")
        else:
            print("Not all bombs are flagged yet.")

    def get_point(self, x, y):
        """
        Change te status of the specific point from the board
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

from typing import Dict, Tuple

from ContentOfField import ContentOfField


class Point:
    """
    This class represents a specific Point of the Board
    Attributes:
        x (int): x coordinate of the x dimension
        y (int): y coordinate of the y dimension
    """

    def __init__(self, x, y, status):
        """
        Initializes the Point

        :param x: x coordinate of the x dimension
        :param y: y coordinate of the y dimnsion
        """
        self.x = int(x)
        self.y = int(y)
        self.outlook = f"|{x}:{y}|"
        self.status = status
        self.mark = None
        self.neighbors = 0

    def __str__(self):
        """
        Returns the string representation of the point
        :return: string
        """
        return self.outlook

    def change_outlook(self):
        """
        Uncover the point content
        :return: None
        """
        if self.mark is not None:
            self.outlook = f"|{self.mark.value}|"
        else:
            self.outlook = f"|{self.status.value}|"

    def put_bomb(self):
        """
        Place a bomb at this point.

        :return: None
        """
        self.status = ContentOfField.BOMB

    def mark_point(self, content: ContentOfField):
        """
        Mark the point with a specific content (flag or question mark).

        :param content: The mark to place on the point
        :return: None
        """
        self.mark = content
        self.change_outlook()

    def get_status_from_neighbors(self):
        """
        Get the ContentOfField status based on the number of neighbors.
        :return: ContentOfField status
        """
        neighbor_status_mapping = {
            1: ContentOfField.ONEBOMB,
            2: ContentOfField.TWOBOMBS,
            3: ContentOfField.THREEBOMBS,
            4: ContentOfField.FOURBOMBS,
            5: ContentOfField.FIVEBOMBS,
            6: ContentOfField.SIXBOMBS,
            7: ContentOfField.SEVENBOMBS,
            8: ContentOfField.EIGHTBOMBS
        }
        return neighbor_status_mapping[self.neighbors]

    def add_bomb_neighbor(self):
        """
        Increment the neighbor bomb count and update the status accordingly if this point is not a bomb.

        :return: None
        """
        self.neighbors += 1
        if self.status != ContentOfField.BOMB:
            self.status = self.get_status_from_neighbors()

    def is_bomb(self):
        """
        Check if this point is a bomb.

        :return: True if the point is a bomb, False otherwise
        """
        return self.status == ContentOfField.BOMB

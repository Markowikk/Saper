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

    def __str__(self):
        """
        Returns the string representation of the point
        :return: string
        """
        return self.outlook

    def change_outlook(self):
        """
        Uncover the point content
        :return:
        """
        self.outlook = f"|{self.status.value}|"

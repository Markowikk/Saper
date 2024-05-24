from enum import Enum


class ContentOfField(Enum):
    EMPTY = "   "
    BOMB = " * "
    FLAG = " @ "
    MARK = " ? "

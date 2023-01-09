from enum import Enum


class Difficulty(str, Enum):
    pl_name: str
    code_length: int
    digit_max: int

    def __new__(
        cls, title: str, pl_name: str, code_length: int = 0, digit_max: int = 0
    ):
        obj = str.__new__(cls, title)
        obj._value_ = title
        obj.pl_name = pl_name
        obj.code_length = code_length
        obj.digit_max = digit_max
        return obj

    EASY = ("Easy", "Easyyay", 4, 7)
    MEDIUM = ("Medium", "Ediummay", 4, 9)
    HARD = ("Hard", "Ardhay", 5, 9)
    VERY_HARD = ("Very Hard", "Eryvay Ardhay", 6, 9)

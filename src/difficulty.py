from enum import Enum


class Difficulty(str, Enum):
    code_length: int
    digit_max: int

    def __new__(
        cls, title: str, code_length: int = 0, digit_max: int = 0
    ):
        obj = str.__new__(cls, title)
        obj._value_ = title
        obj.code_length = code_length
        obj.digit_max = digit_max
        return obj

    
    EASY = ("Easy", 4, 7)
    MEDIUM = ("Medium", 4, 9)
    HARD = ("Hard", 6, 9)
    VERY_HARD = ("Very Hard", 8, 9)

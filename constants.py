import numpy as np
from enum import unique, Enum

WINNING_COMBINATIONS = [
    np.array(
        [
            [1, 1, 1],
            [0, 0, 0],
            [0, 0, 0]
        ]
    ),
    np.array(
        [
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 0]
        ]
    ),
    np.array(
        [
            [0, 0, 0],
            [0, 0, 0],
            [1, 1, 1]
        ]
    ),
    np.array(
        [
            [1, 0, 0],
            [1, 0, 0],
            [1, 0, 0]
        ]
    ),
    np.array(
        [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]
    ),
    np.array(
        [
            [0, 0, 1],
            [0, 0, 1],
            [0, 0, 1]
        ]
    ),
    np.array(
        [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
    ),
    np.array(
        [
            [0, 0, 1],
            [0, 1, 0],
            [1, 0, 0]
        ]
    ),
]

@unique
class Signs(Enum):
    X = 'X'
    O = 'O'

    @staticmethod
    def get_list_of_values():
        return list(map(lambda s: s.value, Signs))

@unique
class EndOfTheGameCommunicates(Enum):
    DRAW = "End of the Game. DRAW"
    WON = "End of the Game. You WON"
    LOSE = "End of the Game. You lose"


INITIAL_ARRAY = np.array(
    [
        ["11", "12", "13"],
        ["21", "22", "23"],
        ["31", "32", "33"]
    ],
    dtype=str
)

VALUES_OF_INITIAL_ARRAY = INITIAL_ARRAY.flatten()
CORNERS_VALUES = ['11', '13', '31', '33']
CENTRE_VALUE = '22'
GAME_BOARD_SIZE = 3
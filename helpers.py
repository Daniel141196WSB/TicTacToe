import numpy as np
from typing import Tuple, Union, Literal

from constants import Signs, VALUES_OF_INITIAL_ARRAY, GAME_BOARD_SIZE


def check_if_there_are_no_empty_fields(
    array: np.ndarray
) -> bool:
    """
        Function checks if there are no empty fields int the passed array
    """
    return np.sum(array != Signs.X.value) == np.sum(array == Signs.O.value)


def display_array(array: np.ndarray) -> None:
    """
        Function displays current state of the passed array
    """
    for i in range(GAME_BOARD_SIZE):
        for j in range(GAME_BOARD_SIZE):
            item = array[i][j]

            print_item = item + '    ' \
                if item in Signs.get_list_of_values() else item + '   '

            print_end = '\n' if j == GAME_BOARD_SIZE - 1 else ' '

            print(print_item, end=print_end)


def get_height_and_width_index_from_field_number(
    field_number: Literal[tuple(VALUES_OF_INITIAL_ARRAY)]
) -> Tuple[int, int]:
    """
        Function converts 'field' included in INITIAL_ARRAY into numpy index
    """
    height_index = int(field_number[0]) - 1
    width_index = int(field_number[1]) - 1
    return height_index, width_index


def check_if_field_is_empty(
    array: np.ndarray,
    field_number: Literal[tuple(VALUES_OF_INITIAL_ARRAY)]
) -> bool:
    """
        Function checks if the field(specified by INITIAL_ARRAY
        variable in the file constants.py) is empty
    """
    height_index, width_index = get_height_and_width_index_from_field_number(
        field_number=field_number
    )
    return array[height_index][width_index] not in Signs.get_list_of_values()


def get_first_empty_field(
    array: np.ndarray
) -> Union[Tuple[int, int], None]:
    """
        Function returns numpy index of the first found filed which is empty
    """
    for field in VALUES_OF_INITIAL_ARRAY:
        if check_if_field_is_empty(
                array=array,
                field_number=corner
        ):
            return get_height_and_width_index_from_field_number(field_number=field)
    return None


def get_index_of_first_empty_corner(
    array: np.ndarray
) -> Tuple[int, int]:
    """
        Function returns numpy index of the first found empty corner
    """

    for corner_value in CORNERS_VALUES:
        if check_if_field_is_empty(
                array=array,
                field_number=corner_value
        ):
            return get_height_and_width_index_from_field_number(field_number=corner_value)

    return None


def set_field_by_field_number(
    array: np.ndarray,
    field_number: Literal[tuple(VALUES_OF_INITIAL_ARRAY)],
    sign: Literal[tuple(Signs.get_list_of_values())]
) -> None:
    """
        Function put passed sign into the passed numpy array
        with the use of 'field_number'
        (
            'field_number' indicates which field will be fulfilled.
            Please see 'INITIAL_ARRAY' variable
        )
    """
    height_index, width_index = get_height_and_width_index_from_field_number(
        field_number=field_number
    )
    array[height_index][width_index] = sign


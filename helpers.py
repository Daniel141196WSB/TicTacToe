import numpy as np
from typing import Tuple, Union, Literal

from constants import \
    Signs, \
    VALUES_OF_INITIAL_ARRAY, \
    GAME_BOARD_SIZE, \
    WINNING_COMBINATIONS, \
    CORNERS_VALUES


def is_any_winning_combination_filled(
    array: np.ndarray,
    sign: Literal[tuple(Signs.get_list_of_values())]
) -> bool:
    """
       Function checks the current state of
       the passed array and informs if someone won or not
    """
    for winning_combination in WINNING_COMBINATIONS:
        winning_indexes = np.where(winning_combination)
        number_of_sign_occurrences = np.sum(array[winning_indexes] == sign)
        if number_of_sign_occurrences == GAME_BOARD_SIZE:
            return True

    return False


def get_combination_to_win_or_block(
    array: np.ndarray,
    sign: Literal[tuple(Signs.get_list_of_values())]
):
    """
        Function checks if someone may win in the next move
        and returns the index of the field which will allow him to achieve it
    """
    for winning_combination in WINNING_COMBINATIONS:
        winning_indexes = np.where(winning_combination)
        number_of_sign_occurrences = np.sum(array[winning_indexes] == sign)
        if number_of_sign_occurrences == GAME_BOARD_SIZE - 1:
            winning_indexes = list(zip(*winning_indexes))
            for winning_index in winning_indexes:
                if array[winning_index] not in Signs.get_list_of_values():
                    return winning_index

    return None


def get_field_number_from_user(array):
    """
        Function takes the field number from the user
        until he will give us the correct one
    """
    while True:
        display_array(array)
        field_number = input(
            f"Please choose the field that is not filled. "
            f"For example: '{get_first_empty_field(array=array, numpy_index=False)}'. \n"
        )
        if field_number not in VALUES_OF_INITIAL_ARRAY:
            print("Incorrect Value")
            continue

        if not check_if_field_is_empty(
            array=array,
            field_number=field_number
        ):
            print("Incorrect Value")
            continue

        return field_number


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
    array: np.ndarray,
    numpy_index: bool = True
) -> Union[Tuple[int, int], None]:
    """
        Function returns numpy index of the first found filed which is empty
    """
    for field in VALUES_OF_INITIAL_ARRAY:
        if check_if_field_is_empty(
            array=array,
            field_number=field
        ):
            if not numpy_index:
                return field
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
            'field_number' indicates which field will be filled.
            Please see 'INITIAL_ARRAY' variable
        )
    """
    height_index, width_index = get_height_and_width_index_from_field_number(
        field_number=field_number
    )
    array[height_index][width_index] = sign


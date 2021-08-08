import numpy as np
import random
from constants import \
    WINNING_COMBINATIONS, \
    INITIAL_ARRAY, \
    VALUES_OF_INITIAL_ARRAY, \
    Signs, CORNERS_VALUES
from typing import Tuple, Literal


def _get_count_dict_of_winning_combination(
    array: np.ndarray,
    winning_combination
) -> dict:
    winning_indexes = np.where(winning_combination)
    unique, counts = np.unique(
        array[winning_indexes],
        return_counts=True
    )
    return dict(zip(unique, counts))


def check_if_won(
    array: np.ndarray,
    sign
):
    for winning_combination in WINNING_COMBINATIONS:
        count_dict = _get_count_dict_of_winning_combination(
            array=array,
            winning_combination=winning_combination
        )
        if count_dict.get(sign) == 3:
            return True

    return False


def get_potential_winning_index(
    array: np.ndarray,
    sign
):
    for winning_combination in WINNING_COMBINATIONS:
        count_dict = _get_count_dict_of_winning_combination(
            array=array,
            winning_combination=winning_combination
        )

        number_of_searched_sign = count_dict.pop(sign, None)
        if number_of_searched_sign == 2 and list(count_dict.keys())[0] in VALUES_OF_INITIAL_ARRAY:
            winning_indexes = np.where(winning_combination)
            for i in range(3):
                height_index = winning_indexes[0][i]
                width_index = winning_indexes[1][i]
                if array[height_index][width_index] not in ['X','O']:
                    return height_index, width_index

    return None

def get_field_number_from_user(array):
    while True:
        display_array(array)
        field_number = input(
            "Please choose the field that is not fulfilled. "
            "For example: '11'. \n"
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

if __name__ == "__main__":
    play_tic_tac_toe()

# komunikaty wyniesc do stalych
# Napisac ze moj znak to X
# Dodac tylko pokazywanie tych pol co zostaly
# ten index sprawdzic
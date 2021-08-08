import numpy as np
from constants import \
    INITIAL_ARRAY,\
    Signs, \
    CENTRE_VALUE, \
    EndOfTheGameCommunicates
from helpers import \
    get_field_number_from_user, \
    set_field_by_field_number, \
    check_if_there_are_no_empty_fields, \
    is_any_winning_combination_filled, \
    get_combination_to_win_or_block, \
    get_index_of_first_empty_corner


def make_computer_move(
    array: np.ndarray
) -> None:

    """
        Function chooses the best computer's move and make it
    """

    # First check if we can win the game
    winning_indexes = get_combination_to_win_or_block(
        array=array,
        sign=Signs.O.value
    )
    if winning_indexes:
        array[winning_indexes] = Signs.O.value
        return

    # Check if the opponent can win and if yes block him
    blocking_indexes = get_combination_to_win_or_block(
        array=array,
        sign=Signs.X.value
    )
    if blocking_indexes:
        array[blocking_indexes] = Signs.O.value
        return

    # Take first empty corner
    empty_corner_indexes = get_index_of_first_empty_corner(array=array)
    if empty_corner_indexes:
        array[empty_corner_indexes] = Signs.O.value
        return

    # Take the centre
    if check_if_field_is_empty(
        array=array,
        field_number=CENTRE_VALUE
    ):
        set_field_by_field_number(
            array=array,
            field_number=CENTRE_VALUE,
            sign=Signs.O.value
        )
        return

    # Take first empty field
    first_empty_field_indexes = get_first_empty_field(array=array)
    array[first_empty_field_indexes] = Signs.O.value


def check_if_game_is_finished(
    array: np.ndarray,
    sign: Literal[tuple(Signs.get_list_of_values())],
    won_lose: Literal[
        EndOfTheGameCommunicates.WON.value,
        EndOfTheGameCommunicates.LOSE.value
    ]
) -> bool:

    """
        Function checks if someone has already won or all fields has been filled
    """

    if check_if_there_are_no_empty_fields(array=array):
        print(EndOfTheGameCommunicates.DRAW.value)
        return True

    if is_any_winning_combination_filled(
        array=array,
        sign=sign
    ):
        print(won_lose)
        return True

    return False


def play_tic_tac_toe() -> None:
    """
        Main function responsible for playing the game
    """

    array = INITIAL_ARRAY.copy()
    while True:
        field_number = get_field_number_from_user(array=array)
        set_field_by_field_number(
            array=array,
            field_number=field_number,
            sign=Signs.X.value
        )

        if check_if_game_is_finished(
            array=array,
            sign=Signs.X.value,
            won_lose=EndOfTheGameCommunicates.WON.value
        ):
            break

        make_computer_move(array=array)
        if check_if_game_is_finished(
            array=array,
            sign=Signs.O.value,
            won_lose=EndOfTheGameCommunicates.LOSE.value
        ):
            break
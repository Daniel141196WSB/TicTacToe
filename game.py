
def make_computer_move(
    array: np.ndarray
) -> None:
    winning_index = get_potential_winning_index(
        array=array,
        sign=Signs.O.value
    )
    if winning_index is not None:
        array[winning_index[0]][winning_index[1]] = Signs.O.value
        return

    blocking_index = get_potential_winning_index(
        array=array,
        sign=Signs.X.value
    )
    if blocking_index is not None:
        array[blocking_index[0]][blocking_index[1]] = Signs.O.value
        return

    empty_corner = get_empty_corner(array=array)
    if empty_corner is not None:
        array[empty_corner[0]][empty_corner[1]] = Signs.O.value
        return

    if check_if_field_is_empty(
        array=array,
        field_number='22'
    ):
        array[1][1] = Signs.O.value
        return

    first_empty_field = get_first_empty_field(array=array)
    if first_empty_field is not None:
        array[first_empty_field[0]][first_empty_field[1]] = Signs.O.value
        return


def check_if_game_is_finished(
    array,
    sign,
    won_lose
) -> bool:
    if check_if_all_fields_are_fulfilled(array=array):
        print("DRAW")
        return True

    if check_if_won(
        array=array,
        sign=sign
    ):
        print(won_lose)
        return True

    return False


def play_tic_tac_toe():

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
            won_lose="WON"
        ):
            break

        make_computer_move(array=array)
        if check_if_game_is_finished(
            array=array,
            sign=Signs.O.value,
            won_lose="LOSE"
        ):
            break

# from utils import *
from utils import rows, cols, boxes, history
from utils import extract_units, extract_peers, cross, grid2values, display

row_units = [cross(r, cols) for r in rows]
# row_units[0] = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9']
column_units = [cross(rows, c) for c in cols]
# column_units[0] = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1']
square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI')
                for cs in ('123', '456', '789')]
# square_units[0] = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
unitlist = row_units + column_units + square_units

# TODO: Update the unit list to add the new diagonal units

one_diagonal = [x[0]+x[1] for x in zip(rows, cols)]
other_diagonal = [rows[i] + cols[-i-1] for i in range(len(cols))]


# diagonal_units = [one_diagonal, other_diagonal]

# unitlist = unitlist + diagonal_units

# Must be called after all units (including diagonals) are added to the unitlist
units = extract_units(unitlist, boxes)
peers = extract_peers(units, boxes)


def run_own_implementation(grid):
    # testing own implemenation of methods
    # test grid2values, own implementation
    values = grid2values(grid)
    display(values)

    # test extract_units, own implemenation
    units = extract_units(unitlist, boxes)
    print(units)

    # test extract_peers, own implemenation
    peers = extract_peers(units, boxes)
    print(peers)

    # test eliminate, own implemenation
    values['A3'] = '3'  # is already, just for clarification
    values['A5'] = '2'

    eliminated_values = eliminate(values)
    # display(eliminated_values)
    print(eliminated_values['A2'])  # should be reduced

    reduced_values = only_choice(eliminated_values)
    print("A6, should be '1', is", reduced_values['A6'])  # should be '1'

    values = reduce_puzzle(values)
    display(values)

    print("starting puzzling")
    solve(grid)


def naked_twins(values):
    """Eliminate values using the naked twins strategy.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict
        The values dictionary with the naked twins eliminated from peers

    Notes
    -----
    Your solution can either process all pairs of naked twins from the input once,
    or it can continue processing pairs of naked twins until there are no such
    pairs remaining -- the project assistant test suite will accept either
    convention. However, it will not accept code that does not process all pairs
    of naked twins from the original input. (For example, if you start processing
    pairs of twins and eliminate another pair of twins before the second pair
    is processed then your code will fail the PA test suite.)

    The first convention is preferred for consistency with the other strategies,
    and because it is simpler (since the reduce_puzzle function already calls this
    strategy repeatedly).
    """
    # TODO: Implement this function!
    raise NotImplementedError


def eliminate(values):
    """Apply the eliminate strategy to a Sudoku puzzle

    The eliminate strategy says that if a box has a value assigned, then none
    of the peers of that box can have the same value.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict
        The values dictionary with the assigned values eliminated from peers
    """
    for box in values:
        if len(values[box]) != 1:
            continue

        for peer in peers[box]:
            # values[peer] = "".join(list(
            #     filter(
            #         lambda pot_value: pot_value != values[box], values[peer])
            # ))

            values[peer] = values[peer].replace(values[box], "")

    return values


def only_choice(values):
    """Apply the only choice strategy to a Sudoku puzzle

    The only choice strategy says that if only one box in a unit allows a certain
    digit, then that box must be assigned that digit.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict
        The values dictionary with all single-valued boxes assigned

    Notes
    -----
    You should be able to complete this function by copying your code from the classroom
    """

    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]

            if len(dplaces) == 1:
                values[dplaces[0]] = digit

        # own solution
        # pot_values = '123456789'
        # unit_counter = {}
        # clear_values = []

        # for box in unit:
        #     print(box)
        #     for value in values[box]:
        #         unit_counter[value] = unit_counter[value] + \
        #             1 if value in unit_counter else 1

        # for key in unit_counter:
        #     if unit_counter[key] == 1:
        #         clear_values.append(key)

        # for box in unit:
        #     for clear_value in clear_values:
        #         if clear_value in values[box] and len(values[box]) > 1:
        #             values[box] = clear_value

    return values


def reduce_puzzle(values):
    """Reduce a Sudoku puzzle by repeatedly applying all constraint strategies

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict or False
        The values dictionary after continued application of the constraint strategies
        no longer produces any changes, or False if the puzzle is unsolvable
    """

    while True:
        solved_values_before = len(
            [box for box in values.keys() if len(values[box]) == 1])

        removed_fields = [values[box]
                          for box in values if len(values[box]) == 0]
        if len(removed_fields) > 0:
            # some boxes have no valid options any longer
            # print("that didn't work out")
            return False

        open_fields = [values[box] for box in values if len(values[box]) > 1]
        if len(open_fields) == 0:
            # print('puzzle solved')
            return values

        values = eliminate(values)
        values = only_choice(values)

        solved_values_after = len(
            [box for box in values.keys() if len(values[box]) == 1])

        if solved_values_before == solved_values_after:
            # print("didn't improve")
            return values


def search(values):
    """Apply depth first search to solve Sudoku puzzles in order to solve puzzles
    that cannot be solved by repeated reduction alone.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict or False
        The values dictionary with all boxes assigned or False

    Notes
    -----
    You should be able to complete this function by copying your code from the classroom
    and extending it to call the naked twins strategy.
    """

    values = reduce_puzzle(values)

    if values is False:
        return False

    # display(values)

    if all(len(values[s]) == 1 for s in boxes):
        return values  # solved

    # values_to_find = [(box, values[box])
    #                   for box in boxes if len(values[box]) > 1]

    # fewest_possibilities = sorted(values_to_find, key=lambda x: len(x[1]))

    # fewest_possibilities_box = fewest_possibilities[0][0]
    # fewest_possibilities_next_value = fewest_possibilities[0][1][0]

    # print("fewest possilibities: {}, will be '{}'".format(
    #     fewest_possibilities[0], fewest_possibilities_next_value))

    # values[fewest_possibilities_box] = fewest_possibilities_next_value

    # return search(values)

    _, candidate = min((len(values[s]), s)
                       for s in boxes if len(values[s]) > 1)

    for case in values[candidate]:
        values_case = values.copy()
        values_case[candidate] = case

        attempt = search(values_case)

        if attempt:
            return attempt

    return False


def solve(grid):
    """Find the solution to a Sudoku puzzle using search and constraint propagation

    Parameters
    ----------
    grid(string)
        a string representing a sudoku grid.

        Ex. '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'

    Returns
    -------
    dict or False
        The dictionary representation of the final sudoku grid or False if no solution exists.
    """
    values = grid2values(grid)

    values = search(values)

    return values


if __name__ == "__main__":
    # diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    # display(grid2values(diag_sudoku_grid))
    # result = solve(diag_sudoku_grid)
    # display(result)

    # solvable
    # test_grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
    # run_own_implementation(test_grid)

    # not solvable without search
    test_grid2 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
    # run_own_implementation(test_grid2)
    display(grid2values(test_grid2))
    result = solve(test_grid2)
    display(result)

    try:
        import PySudoku
        PySudoku.play(grid2values(test_grid2), result, history)

    except SystemExit:
        pass

    except Exception as e:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.\n', e)

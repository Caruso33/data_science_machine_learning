import copy


class GameState:
    """
    Attributes
    ----------
    _board: list(list)
        Represent the board with a 2d array _board[x][y]
        where open spaces are 0 and closed spaces are 1
        and a coordinate system where [0][0] is the top-
        left corner, and x increases to the right while
        y increases going down (this is an arbitrary
        convention choice -- there are many other options
        that are just as good)

    _parity: bool
        Keep track of active player initiative (which
        player has control to move) where 0 indicates that
        player one has initiative and 1 indicates player two

    _player_locations: list(tuple)
        Keep track of the current location of each player
        on the board where position is encoded by the
        board indices of their last move, e.g., [(0, 0), (1, 0)]
        means player one is at (0, 0) and player two is at (1, 0)

    Considerations:
        - Board coordinates are situated at the top - left corner
        - Position structure is based on tuples (x: columns,y: rows)
        - Movements are numbered starting from: 'upwards' till: 'diagonal upwards - left', clockwise
    """

    def __init__(self, dim_x=3, dim_y=2):
        self._board = [[0] * dim_y for _ in range(dim_x)]
        self._board[-1][-1] = "/"
        self._player_locations = [None, None]
        self._parity = 0  # player one

    def get_legal_moves(self):
        """Return a list of all legal moves available to the
        active player.  Each player should get a list of all
        empty spaces on the board on their first move, and
        otherwise they should get a list of all open spaces
        in a straight line along any row, column or diagonal
        from their current position. (Players CANNOT move
        through obstacles or blocked squares.) Moves should
        be a pair of integers in (column, row) order specifying
        the zero-indexed coordinates on the board.
        """
        legal_moves = []

        num_row = len(self._board)
        num_col = len(self._board[0])

        move_directions = [
            (0, -1),
            (1, -1),
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
            (-1, -1),
        ]

        player_location = self._player_locations[self._parity]

        if not player_location:
            legal_moves = [
                (x, y)
                for x in range(num_row)
                for y in range(num_col)
                if self._board[x][y] == 0
            ]

            return legal_moves  # all board positions

        def move_if_legal(current_direction, board_location=()):
            nonlocal legal_moves

            loc_zip = (
                zip(board_location, current_direction)
                if board_location
                else zip(player_location, current_direction)
            )

            new_loc = tuple(map(sum, loc_zip))
            new_row_loc, new_col_loc = new_loc

            if (
                # Inside of board
                0 <= new_row_loc < num_row
                and 0 <= new_col_loc < num_col
                # Place occupied
                and self._board[new_row_loc][new_col_loc] == 0
            ):

                # is legal move
                legal_moves.append(new_loc)

                # check ongoing direction
                return move_if_legal(current_direction, new_loc)

        for move_direction in move_directions:
            move_if_legal(move_direction)

        return legal_moves

    def forecast_move(self, move):
        """Return a new board object with the specified move
        applied to the current game state.

        Parameters
        ----------
        move: tuple
            The target position for the active player's next move
            (e.g., (0, 0) if the active player will move to the
            top-left corner of the board)
        """

        new_board = copy.deepcopy(self)

        new_board._player_locations[new_board._parity] = move

        new_board._board[move[0]][move[1]] = 1

        new_board._parity = int(not new_board._parity)

        return new_board

    def __str__(self) -> str:
        return f"""
        Board: {self._board}
        Parity: {self._parity}
        Player locations: {self._player_locations}
        """
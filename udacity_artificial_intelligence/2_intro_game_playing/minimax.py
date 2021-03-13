from minimax_helpers import *


def minimax_decision(gameState, depth=float("inf")):
    """Return the move along a branch of the game tree that
    has the best possible value.  A move is a pair of coordinates
    in (column, row) order corresponding to a legal move for
    the searching player.

    You can ignore the special case of calling this function
    from a terminal state.
    """

    legal_moves = gameState.get_legal_moves()

    maximum = float("-Infinity")
    best_move = None
    for move in legal_moves:
        future_game = gameState.forecast_move(move)

        min_val = min_value(future_game, depth - 1)
        if min_val > maximum:
            maximum = min_val
            best_move = move

    return best_move

    return max(
        gameState.get_legal_moves(),
        key=lambda m: min_value(gameState.forecast_move(m), depth - 1),
    )

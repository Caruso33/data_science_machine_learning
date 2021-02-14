def terminal_test(gameState):
    """Return True if the game is over for the active player
    and False otherwise.
    """
    return len(gameState.get_legal_moves()) == 0


def min_value(gameState):
    """Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    if terminal_test(gameState):
        return 1

    legal_moves = gameState.get_legal_moves()

    minimum = float("Infinity")
    for move in legal_moves:
        future_game = gameState.forecast_move(move)

        max_val = max_value(future_game)
        if max_val < minimum:
            minimum = max_val

    return minimum


def max_value(gameState):
    """Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    if terminal_test(gameState):
        return -1

    legal_moves = gameState.get_legal_moves()

    maximum = float("-Infinity")
    for move in legal_moves:
        future_game = gameState.forecast_move(move)

        min_val = min_value(future_game)
        if min_val > maximum:
            maximum = min_val

    return maximum
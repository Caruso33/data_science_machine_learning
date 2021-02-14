import unittest
import gamestate
import minimax_helpers
from gamestate import *


def test_minmax_helpers():
    g = GameState()

    print("Calling min_value on an empty board...")
    v = minimax_helpers.min_value(g)

    if v == -1:
        print("min_value() returned the expected score!")
    else:
        print("Uh oh! min_value() did not return the expected score.")


class TestMinimaxHelpers(unittest.TestCase):
    def test_terminal_test(self):
        # Case Player 1 game is not over works for dim_x = 3 , dim_y = 2)
        game = gamestate.GameState()
        self.assertEqual(minimax_helpers.terminal_test(game), False)

        # Case Player 1 game is over (works for dim_x = 3 , dim_y = 2)
        game = gamestate.GameState()
        game._board = [[2, 0], [1, 2], [1, "/"]]
        game._player_locations = [(2, 0), (1, 1)]
        self.assertEqual(minimax_helpers.terminal_test(game), True)

        # Case Player 2 game is not over works for dim_x = 3 , dim_y = 2)
        game = gamestate.GameState()
        game_future = game.forecast_move((0, 0))
        self.assertEqual(minimax_helpers.terminal_test(game_future), False)

        # # Case Player 2 game is over (works for dim_x = 3 , dim_y = 2)
        game = gamestate.GameState()
        game._board = [[1, 2], [1, 2], [2, "/"]]
        game._player_locations = [(2, 0), (0, 1)]
        game._parity = 1
        self.assertEqual(minimax_helpers.terminal_test(game), True)

    def test_min_value(self):
        # Case Player 2 (min_game is over (works for dim_x = 3 , dim_y = 2)
        game = gamestate.GameState()
        game._board = [[1, 2], [1, 2], [2, "/"]]
        game._player_locations = [(2, 0), (0, 1)]
        game._initiative = 1
        self.assertEqual(minimax_helpers.min_value(game), 1)

        # Case Player 2 (min_value) game is not over (works for dim_x = 3 , dim_y = 2)
        game = gamestate.GameState()
        game._board = [[1, 0], [2, 0], [0, "/"]]
        game._player_locations = [(0, 0), (1, 0)]
        self.assertEqual(minimax_helpers.min_value(game), -1)

    def test_max_value(self):
        # Case Player 1 (max_value) game is over (works for dim_x = 3 , dim_y = 2)
        game = gamestate.GameState()
        game._board = [[2, 0], [1, 2], [1, "/"]]
        game._player_locations = [(2, 0), (1, 1)]
        self.assertEqual(minimax_helpers.max_value(game), -1)

        # Case Player 1 (max_value) game is not over (works for dim_x = 3 , dim_y = 2)
        game = gamestate.GameState()
        game._board = [[0, 0], [1, 0], [2, "/"]]
        game._player_locations = [(1, 0), (2, 0)]
        self.assertEqual(minimax_helpers.max_value(game), 1)


if __name__ == "__main__":
    test_minmax_helpers()

    unittest.main()

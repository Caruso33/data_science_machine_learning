import unittest
import gamestate

from gamestate import *


def test_game_class():
    # game class
    print("Creating empty game board...")
    emptyState = GameState()
    print("Everything looks good!")

    # game class functionality
    print("Creating empty game board...")
    g = GameState()

    print("Getting legal moves for player 1...")
    p1_empty_moves = g.get_legal_moves()
    print("Found {} legal moves.".format(len(p1_empty_moves or [])))

    print("Applying move (0, 0) for player 1...")
    g1 = g.forecast_move((0, 0))

    print("Getting legal moves for player 2...")
    p2_empty_moves = g1.get_legal_moves()
    if (0, 0) in set(p2_empty_moves):
        print(
            "Failed\n  Uh oh! (0, 0) was not blocked properly when "
            + "player 1 moved there."
        )
    else:
        print("Everything looks good!")


class TestGameState(unittest.TestCase):
    def test_initializer_default(self):
        board = [[0] * 2 for _ in range(3)]
        board[2][1] = "/"
        game = gamestate.GameState()

        self.assertEqual(game._board, board)

    def test_forecast_move(self):
        game = gamestate.GameState()
        future_game_1 = game.forecast_move((0, 0))
        future_game_2 = future_game_1.forecast_move((1, 1))
        # Player 0 checks
        self.assertEqual(future_game_1._board[0][0], 1)
        self.assertEqual(future_game_1._parity, 1)
        self.assertEqual(future_game_1._player_locations[0], (0, 0))
        # Player 1 checks
        self.assertEqual(future_game_2._board[1][1], 1)
        self.assertEqual(future_game_2._parity, 0)
        self.assertEqual(future_game_2._player_locations[1], (1, 1))

    def test_get_legal_moves(self):
        game_1 = gamestate.GameState()
        future_game_1_1 = game_1.forecast_move((0, 0))  # Player 1
        future_game_1_2 = future_game_1_1.forecast_move((1, 1))  # Player 2
        future_game_1_3 = future_game_1_2.forecast_move((0, 1))  # Player 1

        game_2 = gamestate.GameState()
        future_game_2_1 = game_2.forecast_move((1, 1))  # Player 1
        future_game_2_2 = future_game_2_1.forecast_move((0, 1))  # Player 2

        game_3 = gamestate.GameState()
        future_game_3_1 = game_3.forecast_move((1, 0))  # Player 1
        future_game_3_2 = future_game_3_1.forecast_move((0, 0))  # Player 2

        # Initial case:
        self.assertEqual(
            game_1.get_legal_moves(), [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0)]
        )
        self.assertEqual(
            future_game_1_1.get_legal_moves(), [(0, 1), (1, 0), (1, 1), (2, 0)]
        )

        # Other cases:
        self.assertEqual(future_game_1_2.get_legal_moves(), [(1, 0), (2, 0), (0, 1)])
        self.assertEqual(future_game_1_3.get_legal_moves(), [(1, 0), (2, 0)])

        self.assertEqual(future_game_2_2.get_legal_moves(), [(1, 0), (2, 0), (0, 0)])

        self.assertEqual(future_game_3_2.get_legal_moves(), [(2, 0), (1, 1), (0, 1)])


if __name__ == "__main__":
    # test_game_class()

    unittest.main()

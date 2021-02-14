import unittest
import gamestate
import minimax
import gamestate as game


def test_minmax():
    best_moves = set([(0, 0), (2, 0), (0, 1)])
    rootNode = game.GameState()
    minimax_move = minimax.minimax_decision(rootNode)

    print("Best move choices: {}".format(list(best_moves)))
    print("Your code chose: {}".format(minimax_move))

    if minimax_move in best_moves:
        print(
            "That's one of the best move choices. Looks like your minimax-decision function worked!"
        )
    else:
        print("Uh oh...looks like there may be a problem.")


class TestMinimax(unittest.TestCase):
    def test_minimax_decision(self):
        game = gamestate.GameState()
        self.assertIn(minimax.minimax_decision(game), [(0, 1), (2, 0), (0, 0)])


if __name__ == "__main__":
    test_minmax()

    unittest.main()

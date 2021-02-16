"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

from queue import Empty as QueueEmptyError
from multiprocessing import TimeoutError
from threading import Thread
from queue import Queue
from functools import wraps
from copy import copy
from copy import deepcopy
from collections import Counter
import sys
import timeit
import random
import unittest

import isolation
import game_agent

from importlib import reload


# class IsolationTest(unittest.TestCase):
#     """Unit tests for isolation agents"""

#     def setUp(self):
#         reload(game_agent)
#         self.player1 = "Player1"
#         self.player2 = "Player2"
#         self.game = isolation.Board(self.player1, self.player2)

#     def test_example(self):
#         # TODO: All methods must start with "test_"
#         self.fail("Hello, World!")


# if __name__ == '__main__':
#     unittest.main()

"""
This file contains test cases to verify the correct implementation of the
functions required for this project including minimax, alphabeta, and iterative
deepening.  The heuristic function is tested for conformance to the expected
interface, but cannot be automatically assessed for correctness.
STUDENTS SHOULD NOT NEED TO MODIFY THIS CODE.  IT WOULD BE BEST TO TREAT THIS
FILE AS A BLACK BOX FOR TESTING.
"""


WRONG_MOVE = """
The {} function failed because it returned a non-optimal move at search depth {}.
Valid choices: {}
Your selection: {}
"""

WRONG_NUM_EXPLORED = """
Your {} search visited the wrong nodes at search depth {}.  If the number
of visits is too large, make sure that iterative deepening is only
running when the `iterative` flag is set in the agent constructor.
Max explored size: {}
Number you explored: {}
"""

UNEXPECTED_VISIT = """
Your {} search did not visit the number of expected unique nodes at search
depth {}.
Max explored size: {}
Number you explored: {}
"""

ID_FAIL = """
Your agent explored the wrong number of nodes using Iterative Deepening and
minimax. Remember that ID + MM should check every node in each layer of the
game tree before moving on to the next layer.
"""

INVALID_MOVE = """
Your agent returned an invalid move. Make sure that your function returns
a selection when the search times out during iterative deepening.
Valid choices: {!s}
Your choice: {}
"""

TIMER_MARGIN = 15  # time (in ms) to leave on the timer to avoid timeout


def curr_time_millis():
    """Simple timer to return the current clock time in milliseconds."""
    return 1000 * timeit.default_timer()


def handler(obj, testcase, queue):
    """Handler to pass information between threads; used in the timeout
    function to abort long-running (i.e., probably hung) test cases.
    """
    try:
        queue.put((None, testcase(obj)))
    except:
        queue.put((sys.exc_info(), None))


def timeout(time_limit):
    """Function decorator for unittest test cases to specify test case timeout.
    The timer mechanism works by spawning a new thread for the test to run in
    and using the timeout handler for the thread-safe queue class to abort and
    kill the child thread if it doesn't return within the timeout.
    It is not safe to access system resources (e.g., files) within test cases
    wrapped by this timer.
    """

    def wrapUnitTest(testcase):

        @wraps(testcase)
        def testWrapper(self):

            queue = Queue()

            try:
                p = Thread(target=handler, args=(self, testcase, queue))
                p.daemon = True
                p.start()
                err, res = queue.get(timeout=time_limit)
                p.join()
                if err:
                    raise err[0](err[1]).with_traceback(err[2])
                return res
            except QueueEmptyError:
                raise TimeoutError("Test aborted due to timeout. Test was " +
                                   "expected to finish in less than {} second(s).".format(time_limit))

        return testWrapper

    return wrapUnitTest


def makeEvalTable(table):
    """Use a closure to create a heuristic function that returns values from
    a table that maps board locations to constant values. This supports testing
    the minimax and alphabeta search functions.
    THIS HEURISTIC IS ONLY USEFUL FOR TESTING THE SEARCH FUNCTIONALITY -
    IT IS NOT MEANT AS AN EXAMPLE OF A USEFUL HEURISTIC FOR GAME PLAYING.
    """

    def score(game, player):
        row, col = game.get_player_location(player)
        return table[row][col]

    return score


def makeEvalStop(limit, timer, value=None):
    """Use a closure to create a heuristic function that forces the search
    timer to expire when a fixed number of node expansions have been perfomred
    during the search. This ensures that the search algorithm should always be
    in a predictable state regardless of node expansion order.
    THIS HEURISTIC IS ONLY USEFUL FOR TESTING THE SEARCH FUNCTIONALITY -
    IT IS NOT MEANT AS AN EXAMPLE OF A USEFUL HEURISTIC FOR GAME PLAYING.
    """

    def score(game, player):
        if timer.time_left() < 0:
            raise TimeoutError("Timer expired during search. You must " +
                               "return an answer before the timer reaches 0.")
        if limit == game.counts[0]:
            timer.time_limit = 0
        return 0

    return score


def makeBranchEval(first_branch):
    """Use a closure to create a heuristic function that evaluates to a nonzero
    score when the root of the search is the first branch explored, and
    otherwise returns 0.  This heuristic is used to force alpha-beta to prune
    some parts of a game tree for testing.
    THIS HEURISTIC IS ONLY USEFUL FOR TESTING THE SEARCH FUNCTIONALITY -
    IT IS NOT MEANT AS AN EXAMPLE OF A USEFUL HEURISTIC FOR GAME PLAYING.
    """

    def score(game, player):
        if not first_branch:
            first_branch.append(game.root)
        if game.root in first_branch:
            return 1.
        return 0.

    return score


class CounterBoard(isolation.Board):
    """Subclass of the isolation board that maintains counters for the number
    of unique nodes and total nodes visited during depth first search.
    Some functions from the base class must be overridden to maintain the
    counters during search.
    """

    def __init__(self, *args, **kwargs):
        super(CounterBoard, self).__init__(*args, **kwargs)
        self.counter = Counter()
        self.visited = set()
        self.root = None

    def copy(self):
        new_board = CounterBoard(self.__player_1__, self.__player_2__,
                                 width=self.width, height=self.height)
        new_board.move_count = self.move_count
        new_board.__active_player__ = self.__active_player__
        new_board.__inactive_player__ = self.__inactive_player__
        new_board.__last_player_move__ = copy(self.__last_player_move__)
        new_board.__player_symbols__ = copy(self.__player_symbols__)
        new_board.__board_state__ = deepcopy(self.__board_state__)
        new_board.counter = self.counter
        new_board.visited = self.visited
        new_board.root = self.root
        return new_board

    def forecast_move(self, move):
        self.counter[move] += 1
        self.visited.add(move)
        new_board = self.copy()
        new_board.apply_move(move)
        if new_board.root is None:
            new_board.root = move
        return new_board

    @property
    def counts(self):
        """ Return counts of (total, unique) nodes visited """
        return sum(self.counter.values()), len(self.visited)


class MinimaxPlayerTest(unittest.TestCase):
    """ Unit tests for Minimax agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)

    def test_minimax(self):
        """ Test MinimaxPlayer.minimax interface with simple input """
        h, w = 7, 7  # board size
        test_depth = 1
        starting_location = (5, 3)
        adversary_location = (0, 0)  # top left corner
        def heuristic(g, p): return 0.  # return 0 everywhere

        # create a player agent & a game board
        agent = game_agent.MinimaxPlayer(test_depth, heuristic)
        agent.time_left = lambda: 99  # ignore timeout for fixed-depth search
        board = isolation.Board(agent, 'null_agent', w, h)

        # place two "players" on the board at arbitrary (but fixed) locations
        board.apply_move(starting_location)
        board.apply_move(adversary_location)

        for move in board.get_legal_moves():
            next_state = board.forecast_move(move)
            best_move = agent.minimax(next_state, test_depth)

            self.assertTrue(type(best_move) == tuple,
                            ("Minimax function should return a tuple"))


if __name__ == '__main__':
    unittest.main()

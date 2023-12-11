from kakuro.board import Board
from tests import Test

if __name__ == "__main__":
    board = Board(Test.TEST7)
    board.optimize()
    board.print_values()

from kakuro.node import Node


class Neighbor:
    def __init__(self, node: Node, index: int) -> None:
        self.node = node
        self.index = index


class Board:
    def __init__(self, text: str = "") -> None:
        self.board: list = self.text_to_board(text)
        self.board = self.count_spaces(self.board)
        self.board = self.find_all_values_neighbor(self.board)
        self.board = self.set_combinations(self.board)

    def count_spaces(self, board: list) -> list:
        for i in range(len(board)):
            for j in range(len((board[i]))):
                if board[i][j].right_value not in ["0", "#"]:
                    counter = 0
                    for z in range(j + 1, len(board[i])):
                        if board[i][z].right_value == "0":
                            counter += 1
                        else:
                            break
                    board[i][j].right_space = counter
                if board[i][j].down_value not in ["0", "#"]:
                    counter = 0
                    for z in range(i + 1, len(board)):
                        if board[z][j].down_value == "0":
                            counter += 1
                        else:
                            break
                    board[i][j].down_space = counter
        return board

    def find_neighbore_down(self, row: int, col: int, board: list) -> list:
        neighbor = []
        for r in range(row + 1, row + board[row][col].down_space + 1):
            for c in range(col, -1, -1):
                if board[r][c].right_value not in ["0", "#"]:
                    neigh = Neighbor(board[r][c], col - c)
                    neighbor.append(neigh)
                    break
        return neighbor

    def find_neighbore_right(self, row: int, col: int, board: list) -> list:
        neighbor = []
        for c in range(col + 1, col + board[row][col].right_space + 1):
            for r in range(row, -1, -1):
                if board[r][c].down_value not in ["0", "#"]:
                    neigh = Neighbor(board[r][c], row - r)
                    neighbor.append(neigh)
                    break
        return neighbor

    def find_all_values_neighbor(self, board: list) -> list:
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col].down_value not in ["0", "#"]:
                    self.board[row][col].neighbores_down = self.find_neighbore_down(
                        row, col, board
                    )
                if board[row][col].right_value not in ["0", "#"]:
                    self.board[row][col].neighbores_right = self.find_neighbore_right(
                        row, col, board
                    )
        return board

    def text_to_board(self, text: str) -> list:
        """ """
        board = []
        x_counter = 0
        y_counter = 0
        for i in text.split("\n"):
            b = []
            if i.strip() == "":
                continue
            y_counter = 0
            for j in i.split():
                if j.strip() == "":
                    continue
                right, down = j.strip().split("|")
                right = int(right) if right not in ["#", "0"] else right
                down = int(down) if down not in ["#", "0"] else down
                node = Node(right, down)
                node.x = x_counter
                node.y = y_counter
                b.append(node)
                y_counter += 1
            board.append(b)
            x_counter += 1
        return board

    def set_combinations(self, board: list) -> list:
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j].set_combinations()
        return board

    def optimize(self, depth: int = 3):
        for i in range(depth):
            for row in range(len(self.board)):
                for col in range(len(self.board[row])):
                    self.board[row][col].optimize()

    def print_board(self) -> None:
        for row in self.board:
            for j in row:
                print(j.down_value, "|", j.right_value, end="\t")
            print("\n")

    def print_values(self) -> None:
        for row in self.board:
            for j in row:
                if j.combination_down:
                    print(j.x, j.y, j.combination_down)

    def sort(self):
        flatten_board = []
        for i in self.board:
            for j in i:
                flatten_board.append(j)

        for i in range(len(flatten_board)):
            swapped = False
            for j in range(0, len(flatten_board) - i - 1):
                if flatten_board[j] > flatten_board[j + 1]:
                    flatten_board[j], flatten_board[j + 1] = (
                        flatten_board[j + 1],
                        flatten_board[j],
                    )
                    swapped = True
            if swapped == False:
                break
        return flatten_board

    def copy(self):
        board_copy = Board()
        board_copy.board = self.board.copy()
        return board_copy

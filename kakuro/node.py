class Node:
    def __init__(self, right_value, down_value) -> None:
        self.right_value = right_value
        self.down_value = down_value
        self.x = 0
        self.y = 0
        self.down_space = 0
        self.right_space = 0
        self.correct_value_right = []
        self.correct_value_down = []
        self.combination_right = []
        self.combination_down = []
        self.neighbores_right = []
        self.neighbores_down = []

    def __repr__(self) -> str:
        return (
            f"({self.x},{self.y}) right: {self.right_value}, down: { self.down_space}"
        )

    def __lt__(self, other):
        if len(self.combination_down) > len(other.combination_down):
            return True

        return False

    def set_correct_value_right(self):
        for i in range(len(self.combination_right)):
            for j in range(len(self.combination_right[i])):
                flag = True
                for k in range(len(self.combination_right)):
                    if self.combination_right[i][j] != self.combination_right[k][j]:
                        flag = False
                if flag:
                    self.correct_value_right[j] = self.combination_right[i][j]

    def set_correct_value_down(self):
        for i in range(len(self.combination_down)):
            for j in range(len(self.combination_down[i])):
                flag = True
                for k in range(len(self.combination_down)):
                    if self.combination_down[i][j] != self.combination_down[k][j]:
                        flag = False
                if flag:
                    self.correct_value_down[j] = self.combination_down[i][j]

    def combination(self, space: int, value: int) -> list:
        """
        find all combinations\n
        Ags:
            space(int): میخواییم به چند تا عدد افرازش کنیم\n
            value(int): چه عددی رو میخوایی بشکونی

        Returns:
            numbers(list) : لیست تمام ترکیبات ممکن
        """

        def find_combinations(n, y, current_combination, result):
            if n == 0 and y == 0:
                result.append(current_combination)
                return
            if n == 0 or y < 0:
                return
            for i in range(1, 10):
                if i not in current_combination:
                    find_combinations(n - 1, y - i, current_combination + [i], result)

        numbers = []
        find_combinations(space, value, [], numbers)
        return numbers.copy()

    def set_combinations(self):
        if self.down_space != 0:
            self.combination_down = self.combination(self.down_space, self.down_value)
            self.correct_value_down = [0 for i in range(self.down_space)]
        if self.right_space != 0:
            self.combination_right = self.combination(
                self.right_space, self.right_value
            )
            self.correct_value_right = [0 for i in range(self.right_space)]

    def remove_non_intersection(self, other, x: int, y: int) -> None:
        uniqe_self = []
        uniqe_other = []

        for row in self.combination_down:
            for element in row:
                if element not in uniqe_self:
                    uniqe_self.append(element)
        for row in other.combination_right:
            for element in row:
                if element not in uniqe_other:
                    uniqe_other.append(element)

        intersection = []
        for i in uniqe_self:
            if (
                i in uniqe_other
                and (
                    i not in self.correct_value_down or i == self.correct_value_down[x]
                )
                and (
                    i not in other.correct_value_right
                    or i == other.correct_value_right[y]
                )
            ):
                intersection.append(i)

        self_result = []
        for i in intersection:
            for row in self.combination_down:
                if i in row and row.index(i) == x:
                    self_result.append(row)
        other_result = []
        for i in intersection:
            for j in other.combination_right:
                if i in j and j.index(i) == y:
                    other_result.append(j)

        self.combination_down = self_result
        other.combination_right = other_result
        self.set_correct_value_down()
        other.set_correct_value_right()

    def optimize(self):
        for i in range(len(self.neighbores_down)):
            node, index = self.neighbores_down[i].node, self.neighbores_down[i].index
            self.remove_non_intersection(node, i, index - 1)

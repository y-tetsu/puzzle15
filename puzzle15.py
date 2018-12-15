#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
15パズルを解く
"""


def main():
    """
    動作確認
    """
    pattern = [[1, 2, 6, 3], [4, 5, 0, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    puzzle = Puzzle15(pattern)

    print(puzzle.start)
    print(puzzle.goal)

    result = puzzle.solve()

    if result == -2:
        print("can't solve")
    elif result >= 0:
        print("resolved", puzzle.step)
    else:
        print("not resolved(limit over)", puzzle.step)


class Puzzle15:
    """
    15パズルを解く
    """
    length = 4
    width = 4
    goal = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    step = -1
    max_step = 15

    def __init__(self, start):
        self.start = [[0 for i in range(self.length)] for j in range(self.width)]

        for i in range(self.length):
            for j in range(self.width):
                self.start[j][i] = start[j][i]

        self.start_patterns = [self.start]
        self.goal_patterns = [self.goal]

    def solve(self):
        """
        パズルを解く
        """
        tmp_step = 0

        # 解が存在する場合
        if self.can_solve(self.start):
            if self.is_solved():
                self.step = tmp_step

            else:
                while tmp_step < self.max_step:
                    # スタート側から次の候補を検索
                    self.start_patterns = self.search_next_patterns(self.start_patterns)
                    tmp_step += 1

                    if self.is_solved():
                        self.step = tmp_step
                        break

                    # ゴール側から次の候補を検索
                    self.goal_patterns = self.search_next_patterns(self.goal_patterns)
                    tmp_step += 1

                    if self.is_solved():
                        self.step = tmp_step
                        break

        # 解が存在しない場合
        else:
            self.step = -2

        return self.step

    def can_solve(self, in_pattern):
        """
        解が存在するか判定
        """
        pattern = [flatten for inner in in_pattern for flatten in inner]

        # ありえないパターン
        if set(pattern) != set(range(self.length * self.width)):
            return False

        # 空きの最短距離
        index = pattern.index(0)
        length = index % self.length
        width = index // self.width
        blank_distance = length + width

        # 置換のパリティ
        parity = 0
        for i in range(1, self.length * self.width - 1):
            index = pattern.index(i)

            if i != index:
                pattern[i], pattern[index] = pattern[index], pattern[i]
                parity += 1

        # 置換のパリティ（偶奇）と「空き」の最短距離の偶奇が等しい
        if parity % 2 == blank_distance % 2:
            return True

        return False

    def is_solved(self):
        """
        解が見つかったか判定
        """
        for i in self.start_patterns:
            if i in self.goal_patterns:
                return True

        return False

    def search_blank(self, pattern):
        """
        空きパネルの位置を探す
        """
        ret_i, ret_j = -1, -1
        for i in range(self.length):
            for j in range(self.width):
                if pattern[j][i] == 0:
                    ret_i, ret_j = i, j
                    break

        return ret_i, ret_j

    def search_next_patterns(self, patterns):
        """
        次の候補を検索
        """
        next_patterns = []

        for i in patterns:
            p_x, p_y = self.search_blank(i)

            # 上へ移動
            if p_y > 0:
                top = [j[:] for j in i]
                top[p_y][p_x], top[p_y - 1][p_x] = top[p_y - 1][p_x], top[p_y][p_x]
                next_patterns += [top]

            # 下へ移動
            if p_y < self.width - 1:
                bottom = [j[:] for j in i]
                bottom[p_y][p_x], bottom[p_y + 1][p_x] = bottom[p_y + 1][p_x], bottom[p_y][p_x]
                next_patterns += [bottom]

            # 左へ移動
            if p_x > 0:
                left = [j[:] for j in i]
                left[p_y][p_x], left[p_y][p_x - 1] = left[p_y][p_x - 1], left[p_y][p_x]
                next_patterns += [left]

            # 右へ移動
            if p_x < self.length - 1:
                right = [j[:] for j in i]
                right[p_y][p_x], right[p_y][p_x + 1] = right[p_y][p_x + 1], right[p_y][p_x]
                next_patterns += [right]

        return [[i[:] for i in j] for j in next_patterns]


if __name__ == '__main__':
    main()

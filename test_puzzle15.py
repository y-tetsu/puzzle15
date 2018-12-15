#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
unittest
"""

import unittest
import puzzle15


class TestPuzzle15(unittest.TestCase):
    "puzzle15 test"

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_can_solve1(self):
        """
        解けるか
        """
        pattern = [[1, 0, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        puzzle = puzzle15.Puzzle15(pattern)
        self.assertEqual(puzzle.can_solve(pattern), True)

    def test_can_solve2(self):
        """
        解けるか
        """
        pattern = [[0, 2, 1, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        puzzle = puzzle15.Puzzle15(pattern)
        self.assertEqual(puzzle.can_solve(pattern), False)

    def test_solve1(self):
        """
        解く
        """
        pattern = [[1, 0, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        puzzle = puzzle15.Puzzle15(pattern)
        self.assertEqual(puzzle.solve(), 1)

    def test_solve2(self):
        """
        解く
        """
        pattern = [[1, 2, 0, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        puzzle = puzzle15.Puzzle15(pattern)
        self.assertEqual(puzzle.solve(), 2)

    def test_solve3(self):
        """
        解く
        """
        pattern = [[1, 2, 6, 3], [4, 5, 0, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        puzzle = puzzle15.Puzzle15(pattern)
        self.assertEqual(puzzle.solve(), 3)

    def test_solve4(self):
        """
        解く
        """
        pattern = [[2, 2, 6, 3], [1, 9, 5, 7], [4, 10, 11, 15], [8, 12, 13, 14]]
        puzzle = puzzle15.Puzzle15(pattern)
        self.assertEqual(puzzle.solve(), -2)

    # def test_solve5(self):
    #     """
    #     解く
    #     """
    #     pattern = [[2, 6, 3, 7], [1, 9, 5, 15], [4, 10, 11, 0], [8, 12, 13, 14]]
    #     puzzle = puzzle15.Puzzle15(pattern)
    #     self.assertEqual(puzzle.solve(), 19)

    def test_search_blank1(self):
        """
        空きパネル位置
        """
        pattern = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        puzzle = puzzle15.Puzzle15(pattern)
        self.assertEqual(puzzle.search_blank(pattern), (0, 0))

    def test_search_blank2(self):
        """
        空きパネル位置
        """
        pattern = [[1, 0, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        puzzle = puzzle15.Puzzle15(pattern)
        self.assertEqual(puzzle.search_blank(pattern), (1, 0))

    def test_search_blank3(self):
        """
        空きパネル位置
        """
        pattern = [[1, 6, 2, 3], [4, 5, 0, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        puzzle = puzzle15.Puzzle15(pattern)
        self.assertEqual(puzzle.search_blank(pattern), (2, 1))

    def test_search_blank4(self):
        """
        空きパネル位置
        """
        pattern = [[1, 15, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 0]]
        puzzle = puzzle15.Puzzle15(pattern)
        self.assertEqual(puzzle.search_blank(pattern), (3, 3))

    def test_search_next_patterns1(self):
        """
        次の候補
        """
        pattern = [[1, 2, 3, 4], [5, 0, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        puzzle = puzzle15.Puzzle15(pattern)
        expect = [
            [[1, 0, 3, 4], [5, 2, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]],
            [[1, 2, 3, 4], [5, 9, 6, 7], [8, 0, 10, 11], [12, 13, 14, 15]],
            [[1, 2, 3, 4], [0, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]],
            [[1, 2, 3, 4], [5, 6, 0, 7], [8, 9, 10, 11], [12, 13, 14, 15]],
            ]
        result = puzzle.search_next_patterns([pattern])
        self.assertEqual(result, expect)

    def test_search_next_patterns2(self):
        """
        次の候補
        """
        pattern = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        puzzle = puzzle15.Puzzle15(pattern)
        expect = [
            [[4, 1, 2, 3], [0, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]],
            [[1, 0, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]],
            ]
        result = puzzle.search_next_patterns([pattern])
        self.assertEqual(result, expect)

    def test_search_next_patterns3(self):
        """
        次の候補
        """
        pattern = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        puzzle = puzzle15.Puzzle15(pattern)
        expect = [
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 0], [13, 14, 15, 12]],
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 15]],
            ]
        result = puzzle.search_next_patterns([pattern])
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()

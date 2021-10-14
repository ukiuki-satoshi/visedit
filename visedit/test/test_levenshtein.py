# coding: utf-8

from unittest import TestCase

from parameterized import parameterized

from visedit.utils import Levenshtein


class TestLevenshtein(TestCase):

    @parameterized.expand([
        ("sitting", "kitten", [ 
            [0, 1, 2, 3, 4, 5, 6],
            [1, 1, 2, 3, 4, 5, 6],
            [2, 2, 1, 2, 3, 4, 5],
            [3, 3, 2, 1, 2, 3, 4],
            [4, 4, 3, 2, 1, 2, 3],
            [5, 5, 4, 3, 2, 2, 3],
            [6, 6, 5, 4, 3, 3, 2],
            [7, 7, 6, 5, 4, 4, 3],
        ]),
    ])
    def test_levenshtein_table(self, src, dist, expect):
        actual = Levenshtein.leven(src, dist)
        self.assertEqual(expect, actual)


    @parameterized.expand([
        ("sitting", "kitten",
            [
                'rep',
                'noedit',
                'noedit',
                'noedit',
                'rep',
                'noedit',
                'del'
            ]
        ),
    ])
    def test_string_edit_path(self, src, dist, expect):
        cost_table = Levenshtein.leven("sitting", "kitten")
        actual = Levenshtein.find_path(cost_table)
        self.assertEqual(expect, actual)


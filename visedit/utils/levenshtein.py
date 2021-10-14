import sys
from typing import Dict, List


class Levenshtein(object):
    """
    Class for calculating levenshtein distance
    """

    @staticmethod
    def leven(s1: str, s2: str) -> Dict[int, Dict[int, int]]:
        """
        :param s1: source string
        :param s2: target string
        :return: levenshtein distance table of two strings.

        edit costs are below.
        * insert = 1
        * delete = 1
        * replace = 1
        """
        result = {}
        n, m = len(s1), len(s2)

        cost_table = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            cost_table[i][0] = i

        for j in range(m + 1):
            cost_table[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                cost = 0 if s1[i - 1] == s2[j - 1] else 1
                insert = cost_table[i-1][j] + 1
                delete = cost_table[i][j - 1] + 1
                replace = cost_table[i - 1][j - 1] + cost
                cost_table[i][j] = min(insert, delete, replace)

        result["distance"] = cost_table[n][m]
        return cost_table

    @staticmethod
    def find_path(
        cost_table: Dict[int, Dict[int, int]],
        i: int = 0,
        j: int = 0,
        padding: bool = False
    ) -> List[str]:
        """
        :cost_table: levenshtein distance table which is calculated Levenshtein.leven  # NOQA
        :i: current_position of source string
        :j: current_position of target string
        :padding: whether or not to do padding
        :return: return list of edit types
        """

        if padding:
            padded_table = []
            for k in range(len(cost_table)):
                padded_table.append(cost_table[k] + [sys.maxsize])
            padded_table.append([sys.maxsize]*len(cost_table[0]))

            cost_table = padded_table
        n = len(cost_table) - 1
        m = len(cost_table[0]) - 1

        current_cost = cost_table[i][j]

        # reach end of the strings
        if i + 1 == n and j + 1 == m:
            return []

        replace = cost_table[i+1][j+1]
        delete = cost_table[i+1][j]
        insert = cost_table[i][j + 1]

        if any(map(lambda a: a < current_cost, [delete, insert, replace])):
            # wrong path passed
            return None

        # check  not out of table
        if replace != sys.maxsize:
            ret = Levenshtein.find_path(cost_table, i+1, j+1)
            if ret is not None:
                if replace == current_cost:
                    return ["noedit"] + ret
                else:
                    return ["rep"] + ret

        # check not out of table and invalid pass
        if delete != sys.maxsize and delete > current_cost:
            ret = Levenshtein.find_path(cost_table, i+1, j)
            if ret is not None:
                return ["del"] + ret

        # check not out of table and invalid pass
        if insert is not sys.maxsize and insert > current_cost:
            ret = Levenshtein.find_path(cost_table, i, j + 1)
            if ret is not None:
                return ["ins"] + ret

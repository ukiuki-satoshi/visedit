from typing import Dict


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
    def find_path(cost_table):
        """
        :cost_table: levenshtein distance table which is calculated Levenshtein.leven  # NOQA
        :return: return list of edit types
        """

        n = len(cost_table)
        m = len(cost_table[0])

        edit_table = []
        for i in range(n):
            edit_table.append(['']*m)

        NO = ['noedit']
        REP = ['rep']
        DEL = ['del']
        INS = ['ins']

        edit_table[0][0] = []
        for i in range(1, n):
            edit_table[i][0] = DEL * i
        for j in range(1, m):
            edit_table[0][j] = INS * j

        for i in range(1, n):
            for j in range(1, m):
                replace = cost_table[i-1][j-1]
                delete = cost_table[i-1][j]
                insert = cost_table[i][j-1]
                operations = [
                    [NO if cost_table[i][j] == replace
                        else REP, replace, edit_table[i-1][j-1]],
                    [DEL, delete, edit_table[i-1][j]],
                    [INS, insert, edit_table[i][j-1]],
                ]

                op = sorted(operations, key=lambda op: op[1])[0]
                edit_table[i][j] = op[2] + op[0]
        return edit_table[-1][-1]

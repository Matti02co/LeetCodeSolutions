"""
Both time and space complexity of O(n^2).
"""

"""
What did I learn? Use of continue and a good intuition on the division operation.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        righe = defaultdict(set)
        colonne = defaultdict(set)
        quadrati = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in righe[r] or board[r][c] in colonne[c] or board[r][c] in quadrati[r//3, c//3]:
                    return False
                righe[r].add(board[r][c])
                colonne[c].add(board[r][c])
                quadrati[r//3, c//3].add(board[r][c])
        
        return True

from typing import List
# DFS
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # 判断board【row】【col】能否填入x
        def isValid(board, row, col, x):
            for k in range(9):
                if board[row][k] == x:
                    return False
                if board[k][col] == x:
                    return False
                if board[(row//3)*3 + k//3][(col//3)*3 + k%3] == x:
                    return False
            return True

        def backtrack(board, i, j):
            m, n = 9, 9
            if j == n:
                # 穷举到最后一列的话，就换到下一行重新开始
                return backtrack(board, i+1, 0)

            if i == m:
                # 找到一个可行解，出发base case
                return True

            if board[i][j] != '.':
                # 如果有预设数字，不用穷举，跳过下一列
                return backtrack(board, i, j+1)

            for x in range(1,10):
                char_x = str(x)
                # 遇到不能填下的数字就跳过
                if isValid(board, i, j, char_x) == False:
                    continue

                board[i][j] = char_x
                # 遇到可行解，立即结束
                if backtrack(board, i, j+1):
                    return True
                board[i][j] = '.'
            # 穷举完都没找到可行解，此路不通
            return False
        backtrack(board,0,0)


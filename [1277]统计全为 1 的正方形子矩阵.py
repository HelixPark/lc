# 给你一个 m * n 的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# 输出：15
# 解释： 
# 边长为 1 的正方形有 10 个。
# 边长为 2 的正方形有 4 个。
# 边长为 3 的正方形有 1 个。
# 正方形的总数 = 10 + 4 + 1 = 15.
#  
# 
#  示例 2： 
# 
#  输入：matrix = 
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# 输出：7
# 解释：
# 边长为 1 的正方形有 6 个。 
# 边长为 2 的正方形有 1 个。
# 正方形的总数 = 6 + 1 = 7.
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 300 
#  1 <= arr[0].length <= 300 
#  0 <= arr[i][j] <= 1 
#  
#  Related Topics 数组 动态规划 
#  👍 102 👎 0


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # dp:原地修改
        # matrix[i][j]记录的是：---以此点为右下角的正方形的个数
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    continue
                elif i == 0 or j == 0:
                    res += 1
                else:
                    matrix[i][j] = min(matrix[i-1][j-1],matrix[i-1][j],matrix[i][j-1]) + 1
                    res += matrix[i][j]
        return res
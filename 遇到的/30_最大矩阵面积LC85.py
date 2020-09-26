# -*- coding:utf-8 -*-
# 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
#
#  示例:
#
#  输入:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# 输出: 6
#  Related Topics 栈 数组 哈希表 动态规划
#  👍 590 👎 0

from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxarea = 0
        # 动态规划，对于每一层，利用柱状图的高度进行计算
        # dp存储每一行，连续1的个数
        dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # 0是被霸占了，1才是空地
                if matrix[i][j] == '0':
                    continue

                # 对于每行，计算连续1的个数，也就是最大宽度
                if j:
                    dp[i][j] = dp[i][j-1] + 1
                    width = dp[i][j]
                else:
                    dp[i][j] = 1
                    width = dp[i][j]

                # 以i，j为右下角建立矩形，向上推到顶
                for k in range(i,-1,-1):
                    # 找最小宽度
                    width = min(width,dp[k][j])
                    maxarea = max(maxarea, width * (i-k+1))
        return maxarea
c = Solution()
matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

c.maximalRectangle(matrix)
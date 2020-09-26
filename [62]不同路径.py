# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。 
# 
#  机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。 
# 
#  问总共有多少条不同的路径？ 
# 
#  
# 
#  例如，上图是一个7 x 3 的网格。有多少可能的路径？ 
# 
#  
# 
#  示例 1: 
# 
#  输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
#  
# 
#  示例 2: 
# 
#  输入: m = 7, n = 3
# 输出: 28 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= m, n <= 100 
#  题目数据保证答案小于等于 2 * 10 ^ 9 
#  
#  Related Topics 数组 动态规划 
#  👍 693 👎 0

import math
class Solution:
    def uniquePaths1(self, m: int, n: int) -> int:
        # 方式1：排列组合，m行n列，c（m+n-2,m-1）
        # return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))

        # 方式2：dp
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
    def uniquePaths2(self, m: int, n: int) -> int:
        # 方式2:dp,优化空间o(2n)
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j - 1]
            pre = cur[:]
        return pre[-1]

    def uniquePaths3(self, m: int, n: int) -> int:
        # 方式3:dp,优化空间o(n)
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j - 1]
        return cur[-1]
    def uniquePaths4(self, m: int, n: int) -> int:
        # 方式4：递归，超时
        if m <= 0 or n <= 0:
            return 0
        elif m == 1 or n == 1:
            return 1
        elif m == 2 and  n == 2:
            return 2
        elif (m == 3 and n == 2) or (m == 2 and n == 3):
            return 3
        res = 0
        res += self.uniquePaths4(m-1,n)
        res += self.uniquePaths4(m,n-1)
        return res

    # dp = [[0] * (n+1) for _ in range(m+1)]
    # def uniquePaths(self, m: int, n: int) -> int:
    #     # 方式4：递归，带去重复
    #     # m,n均小于100，用二维数组存下计算过的，
    #     if m <= 0 or n <= 0:
    #         return 0
    #     elif m == 1 or n == 1:
    #         return 1
    #     elif m == 2 and  n == 2:
    #         return 2
    #     elif (m == 3 and n == 2) or (m == 2 and n == 3):
    #         return 3
    #     if dp[m][n] >0:
    #         return dp[m][n]
    #
    #     dp[m-1][n] += self.uniquePaths(m-1,n)
    #     dp[m][n-1] += self.uniquePaths(m,n-1)
    #     dp[m][n] = dp[m-1][n] + dp[m][n-1]
    #     return dp[m][n]
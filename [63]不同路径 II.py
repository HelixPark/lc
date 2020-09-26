# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。 
# 
#  机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。 
# 
#  现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？ 
# 
#  
# 
#  网格中的障碍物和空位置分别用 1 和 0 来表示。 
# 
#  说明：m 和 n 的值均不超过 100。 
# 
#  示例 1: 
# 
#  输入:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
#  
#  Related Topics 数组 动态规划 
#  👍 415 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniquePathsWithObstacles2(self, obstacleGrid: List[List[int]]) -> int:
        # 方式2：dp.因为存在00位置和尾巴处是1，所以形式稍微变化
        if len(obstacleGrid) == 0:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] != 1:
                    if i == j == 0:
                        dp[i][j] = 1
                    else:
                        a, b = 0, 0
                        if i != 0:
                            a = dp[i-1][j]
                        if j != 0:
                            b = dp[i][j-1]
                        dp[i][j] = a + b

                # if obstacleGrid[i][j] == 0:
                #     dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 方式3：dp，原地修改
        if len(obstacleGrid) == 0:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    # 若有障碍物，变为0
                    obstacleGrid[i][j] = 0
                else:
                    if i == j == 0:
                        obstacleGrid[i][j] = 1
                    else:
                        a, b = 0, 0
                        if i != 0:
                            a = obstacleGrid[i-1][j]
                        if j != 0:
                            b = obstacleGrid[i][j-1]
                        obstacleGrid[i][j] = a + b
        return obstacleGrid[m-1][n-1]
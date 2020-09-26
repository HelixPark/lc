from typing import List
class Solution:
    def calculateMinimumHP1(self, dungeon: List[List[int]]) -> int:
        # 动态规划方式
        # 行数，列数
        m, n = len(dungeon), len(dungeon[0])
        # 令dp[i][j]表示从坐标(i, j)到终点所需的最小初始值.
        # 换句话说，如果到达（i,j）时，如果我们此时路径和不小于dp[i][j],就能达到终点
        dp = [[float('inf')] * (n+1) for _ in range(m+1)]
        # 边界问题
        dp[m][n-1], dp[m-1][n] = 1, 1

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1)

        return dp[0][0]

    def calculateMinimumHP2(self, dungeon: List[List[int]]) -> int:
        # DFS方式:时间超时，
        # 行数，列数
        m, n = len(dungeon), len(dungeon[0])
        def dfs(dungeon, m, n, i, j):
            # 到达终点，递归终止
            if i == m-1 and j == n-1:
                return max(1- dungeon[i][j], 1)

            # 最后一行，只能向右
            if i == m-1:
                return max(dfs(dungeon, m, n, i, j+1) - dungeon[i][j], 1)

            # 最后一列，只能向下
            if j == n-1:
                return max(dfs(dungeon, m, n, i+1, j) - dungeon[i][j], 1)

            # 中间位置，向下+向右
            # 得到(i, j)点的后续路径所要求的最低血量Math.min(dfs(i + 1, j), dfs(i, j + 1))，
            # 又因为(i, j)点本身提供血量dungeon[i][j],
            # 因此从(i, j)开始所需的最低血量为min(dfs(i + 1, j), dfs(i, j + 1)) - dungeon[i][j]。
            # 因为骑士的血量不能小于1，因此要和1取个max。
            return max(min(dfs(dungeon,m,n,i+1,j), dfs(dungeon,m,n,i,j+1)) - dungeon[i][j], 1)
        return dfs(dungeon,m,n,0,0)


    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # DFS方式:加入记忆，不超时
        # 行数，列数
        m, n = len(dungeon), len(dungeon[0])
        memo = [[0] * n for _ in range(m)]
        def dfs(dungeon, m, n, i, j):
            # 到达终点，递归终止
            if i == m-1 and j == n-1:
                return max(1- dungeon[i][j], 1)

            # 如果memo中有值，直接取出并返回，不进行后续搜索
            if memo[i][j] > 0:
                return memo[i][j]

            # 同上法，开始搜索
            minRes = 0
            if i == m-1:
                # 最后一行，只能向右
                minRes = max(dfs(dungeon, m, n, i, j+1) - dungeon[i][j], 1)
            elif j == n-1:
                # 最后一列，只能向下
                minRes = max(dfs(dungeon, m, n, i+1, j) - dungeon[i][j], 1)
            else:
                # 中间位置，向下+向右
                # 得到(i, j)点的后续路径所要求的最低血量Math.min(dfs(i + 1, j), dfs(i, j + 1))，
                # 又因为(i, j)点本身提供血量dungeon[i][j],
                # 因此从(i, j)开始所需的最低血量为min(dfs(i + 1, j), dfs(i, j + 1)) - dungeon[i][j]。
                # 因为骑士的血量不能小于1，因此要和1取个max。
                minRes = max(min(dfs(dungeon,m,n,i+1,j), dfs(dungeon,m,n,i,j+1)) - dungeon[i][j], 1)

            memo[i][j] = minRes
            return memo[i][j]

        return dfs(dungeon,m,n,0,0)

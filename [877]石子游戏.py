from typing import List
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        # dp[i][j]代表先手对piles中索引i到j的分数（这里指先手拿到的石头数量与后手数量差）
        # 由于先手有两个选择;前还是后，在两个中选择最优的那个
        # 如何计算dp[i][j]呢: max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])

        length = len(piles)
        dp = [[0] * length for _ in range(length)]

        # base case
        for i in range(length):
            dp[i][i] = piles[i]

        # i=1,代表先算两个子的时候
        for i in range(1,length):
            # 计算有多少组
            for j in range(length-i):
                # 比较j到j+i
                # p1 = piles[j] - dp[j+1][j+i]
                # p2 = piles[j+i] - dp[j][j+i-1]
                dp[j][j+i] = max(piles[j] - dp[j+1][j+i], piles[j+i] - dp[j][j+i-1])

        return dp[0][length-1] > 0

nums = [5,3,4,5]
c = Solution()
c.stoneGame(nums)
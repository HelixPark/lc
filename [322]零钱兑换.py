
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 自底向下
        # dp[i] 表示金额为i需要最少的硬币
        # dp[i] = min(dp[i], dp[i - coins[j]]) j所有硬币
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                # 金额必须比硬币面值大
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin]+1)

        # 返回数组的最后一个
        if dp[-1] != float('inf'):
            return  dp[-1]
        else:
            return -1


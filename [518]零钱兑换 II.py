from typing import List
class Solution:
    def change2(self, amount: int, coins: List[int]) -> int:

        dp = [[0] * (amount+1) for _ in range(len(coins)+1)]

        # base case：上行初始成0，最左列初始成1，无为而治
        for i in range(len(coins)+1):
            dp[i][0] = 1

        for i in range(1,len(coins)+1):
            for a in range(1,amount+1):
                if a < coins[i-1]:
                    # 剩余数额不够，硬币面值大于额度
                    dp[i][a] = dp[i-1][a]
                else:
                    # 额度够：
                    dp[i][a] = dp[i-1][a] + dp[i][a-coins[i-1]]
        return dp[len(coins)][amount]



    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] += dp[x - coin]

        return dp[amount]

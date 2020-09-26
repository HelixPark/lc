# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。 
# 
#  设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。 
# 
#  注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 
# 
#  示例 1: 
# 
#  输入: [3,3,5,0,0,3,1,4]
# 输出: 6
# 解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
#      随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。 
# 
#  示例 2: 
# 
#  输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
#      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
#  
# 
#  示例 3: 
# 
#  输入: [7,6,4,3,1] 
# 输出: 0 
# 解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。 
#  Related Topics 数组 动态规划 
#  👍 511 👎 0


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 只让交易两次，所以在第二次买的时候，价格其实是考虑用了第一次赚的钱去补贴一部分的
        # 第一二次买之前的最低价
        buy1 = buy2 = float('inf')
        profit1 = profit2 = 0
        for p in prices:
            buy1 = min(buy1, p)
            profit1 = max(profit1, p - buy1)
            buy2 = min(buy2, p - profit1) #p-pro_1是第一次的钱抵消了一部分第二次的成本
            profit2 = max(profit2, p - buy2)
        return profit2

    def maxProfit1(self, prices: List[int]) -> int:
        # 方式1：递归
        if not prices:
            return 0
        n = len(prices)

        def dfs(index, status, k):
            # 递归终止条件，数组执行到头了，或者交易了两次了
            if index == n or k == 2:
                return 0
            # 定义三个变量，分别记录[不动]、[买]、[卖]
            a, b, c = 0, 0, 0
            # 保持不动
            a = dfs(index + 1, status, k)
            if status:
                # 递归处理卖的情况，这里需要将k+1，表示执行了一次交易
                b = dfs(index + 1, 0, k + 1) + prices[index]
            else:
                # 递归处理买的情况
                c = dfs(index + 1, 1, k) - prices[index]
            # 最终结果就是三个变量中的最大值
            return max(a, b, c)

        return dfs(0, 0, 0)
    def maxProfit2(self, prices: List[int]) -> int:
        # 方式2：dfs+记忆
        if not prices:
            return 0
        # 用一个哈希表缓存重复的调用
        d = dict()
        n = len(prices)

        def dfs(index, status, k):
            if (index, status, k) in d:
                return d[index, status, k]
            if index == n or k == 2:
                return 0
            a, b, c = 0, 0, 0
            a = dfs(index + 1, status, k)
            if status:
                b = dfs(index + 1, 0, k + 1) + prices[index]
            else:
                c = dfs(index + 1, 1, k) - prices[index]
            d[index, status, k] = max(a, b, c)
            return d[index, status, k]

        return dfs(0, 0, 0)

    def maxProfit3(self, prices):
        # 方式3：dp二维数组dp[n][5],n表示天数，5表示5种不同的状态
        if not prices:
            return 0
        n = len(prices)
        if n < 2:
            return 0
        # 定义二维数组，5种状态
        dp = [[-1 for _ in range(5)] for _ in range(n)]
        # 初始化第一天的状态
        dp[0][0] = 0 #初始化状态
        dp[0][1] = -prices[0] #第一次买入
        dp[0][2] = 0 #第一次卖出
        dp[0][3] = -prices[0] #第二次买入
        dp[0][4] = 0 #第二次卖出
        for i in range(1, n):
            # dp[i][0]相当于初始状态，它只能从初始状态转换来
            dp[i][0] = 0
            # 处理第一次买入、第一次卖出
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
            # 处理第二次买入、第二次卖出
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])
        # 返回最大值
        return max(dp[-1][0], dp[-1][1], dp[-1][2], dp[-1][3], dp[-1][4])
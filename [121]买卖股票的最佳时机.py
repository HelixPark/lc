from typing import List
class Solution:
    # 直接查找，时间超时
    def maxProfit2(self, prices: List[int]) -> int:
        size = len(prices)
        max_profit = float('-inf')
        for i in range(size-1):
            in_price = prices[i]
            for j in range(i,size):
                max_profit = max(max_profit, prices[j] - in_price)
        if max_profit >= 0:
            return max_profit
        else:
            return 0

    # 一次遍历
    # 记录【今天之前买入的最小值】
    # 计算【今天之前最小值买入，今天卖出的获利】，也即【今天卖出的最大获利】
    # 比较【每天的最大获利】，取最大值即可
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for cur_price in prices:
            min_price = min(min_price,cur_price)
            max_profit = max(max_profit,cur_price - min_price)
        return max_profit

p = [7,1,5,3,6,4]
# p = [7,6,4,3,1]
s = Solution()
print(s.maxProfit(p))
# 珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。 
# 
#  珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后
# 这一小时内不会再吃更多的香蕉。 
# 
#  珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。 
# 
#  返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入: piles = [3,6,7,11], H = 8
# 输出: 4
#  
# 
#  示例 2： 
# 
#  输入: piles = [30,11,23,4,20], H = 5
# 输出: 30
#  
# 
#  示例 3： 
# 
#  输入: piles = [30,11,23,4,20], H = 6
# 输出: 23
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= piles.length <= 10^4 
#  piles.length <= H <= 10^9 
#  1 <= piles[i] <= 10^9 
#  
#  Related Topics 二分查找 
#  👍 78 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def canFinish(self,piles, speed, H):
        time = 0
        for n in piles:
            # 没吃完剩下的还得一个小时
            remain = 0
            if n % speed > 0:
                remain = 1
            time += (n // speed) + remain

            if time > H:
                return False
        return time <= H

    def minEatingSpeed1(self, piles: List[int], H: int) -> int:
        # 暴力解法
        max_speed = max(piles)
        for speed in range(1,max_speed + 1):
            # 以speed是否能在H ⼩时内吃完⾹蕉
            if self.canFinish(piles, speed, H):
                return speed
        return max_speed
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # 二分查找解法：
        # 这个for循环，是连续的空间线性搜索，可以用二分查找
        # 要求的是最⼩速度，所以可以⽤⼀个搜索左侧边界的⼆分查找来代替线性搜索
        left, right = 1, max(piles) + 1
        while left < right:
            mid = left + (right - left) // 2
            if self.canFinish(piles, mid, H):
                right = mid
            else:
                left = mid + 1
        return left


piles = [3,6,7,11]
H = 8
c = Solution()
print(c.minEatingSpeed(piles,H))
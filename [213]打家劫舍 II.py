from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 0
        if l <= 2:
            return max(nums)
        # 其实就是把环拆成两个队列，
        # 一个是从0到n - 1，另一个是从1到n，
        # 然后返回两个结果最大的。

        # 转移方程：遇到第i个房屋，若抢i，则加上i-2的值，否则就是i-1的值
        # dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])


        # 不抢第一个，dp[0] = 0, 最后一个可抢可不抢，所以循环到l
        dp1 = [0] * l
        # base case
        dp1[0], dp1[1] = 0, nums[1]

        for i in range(2,l):

            dp1[i] = max(dp1[i-1],   #不抢第i个
                        dp1[i-2] + nums[i])   #抢第i个

        # 不抢最后一个，循环到l-1
        dp2 = [0] * (l-1)
        dp2[0], dp2[1] = nums[0], max(nums[0], nums[1])

        for i in range(2,l-1):
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i])


        return max(dp1[l-1], dp2[l-2])


n = [2,3,2]
c = Solution()
print(c.rob(n))
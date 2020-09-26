
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
    #     # 动态规划的思路：将 dp 数组定义为：以 nums[i] 结尾的最长上升子序列的长度
    #     # 那么题目要求的，就是这个 dp 数组中的最大者
    #     # 以数组  [10, 9, 2, 5, 3, 7, 101, 18] 为例：
    #     # dp 的值： 1  1  1  2  2  3  4    4
    #     # 复杂度O(n2)
        if len(nums) <= 1:
            return len(nums)
        # dp数组应该全部初始化为1，因为⼦序列最少也要包含⾃⼰，所以⻓度最⼩为1
        dp = [1] * len(nums)

        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

    def lengthOfLIS2(self, nums: List[int]) -> int:
        # 动态规划的思路：将 dp 数组定义为：以 nums[i] 结尾的最长上升子序列的长度
        # 二分查找
        top = [0] * len(nums)
        # 牌堆数初始化为0
        piles = 0
        for i in range(len(nums)):
            # 要处理的扑克牌
            poker = nums[i]

            left, right = 0, piles
            while left < right:
                mid = (left + right)/2
                if top[mid] > poker:
                    right = mid
                elif top[mid] < poker:
                    left = mid
                else:
                    right = mid

            # 没有找到牌堆，则新建
            if left == piles:
                piles += 1
            # 放到牌堆顶
            top[left] = poker
        return piles
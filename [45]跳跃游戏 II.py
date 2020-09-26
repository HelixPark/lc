# 给定一个非负整数数组，你最初位于数组的第一个位置。 
# 
#  数组中的每个元素代表你在该位置可以跳跃的最大长度。 
# 
#  你的目标是使用最少的跳跃次数到达数组的最后一个位置。 
# 
#  示例: 
# 
#  输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#  
# 
#  说明: 
# 
#  假设你总是可以到达数组的最后一个位置。 
#  Related Topics 贪心算法 数组 
#  👍 630 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def jump1(self, nums: List[int]) -> int:
        # 贪心
        end, farest = 0, 0
        jumps = 0

        for i in range(len(nums)-1):
            farest = max(nums[i] + i, farest)
            if end == i:
                jumps += 1
                end = farest
        return jumps

    def dp(self,nums, p, memo):
        n = len(nums)

        # base case
        if p >= n-1:
            return 0

        # 子问题已经计算过
        if memo[p] != n:
            return memo[p]

        steps = nums[p]
        # 可以选择跳1步，两步
        for i in range(1,steps+1):
            # 穷举每个选择，计算每个子问题
            tmp = self.dp(nums, p + i, memo)
            memo[p] = min(memo[p], tmp + 1)

        return memo[p]

    def jump(self, nums: List[int]) -> int:
        #   dp[i]表示从索引i到最后一格，需要dp[i]次
        memo = [len(nums)] * len(nums)
        return self.dp(nums, 0, memo)
# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。 
# 
# 
#  返回滑动窗口中的最大值。 
# 
#  
# 
#  进阶： 
# 
#  你能在线性时间复杂度内解决此题吗？ 
# 
#  
# 
#  示例: 
# 
#  输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7] 
# 解释: 
# 
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10^5 
#  -10^4 <= nums[i] <= 10^4 
#  1 <= k <= nums.length 
#  
#  Related Topics 堆 Sliding Window 
#  👍 535 👎 0

from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums
        # 两数组一起可以提供两个块内元素的全部信息
        # right[i]是左侧块内的最大元素，
        # left[j]是右侧块内的最大元素。
        # 因此滑动窗口中的最大元素为max(right[i], left[j])。
        left, right = [0] * n, [0] * n
        left[0], right[-1] = nums[0], nums[-1]

        for i in range(1,n):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i-1], nums[i])

            j = n - i - 1
            if (j+1) % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j+1], nums[j])

        res = []
        for i in range(n-k+1):
            res.append(max(left[i+k-1], right[i]))
        return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3
c = Solution()
c.maxSlidingWindow(nums, k)

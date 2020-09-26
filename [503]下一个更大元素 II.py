# 给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第
# 一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。 
# 
#  示例 1: 
# 
#  
# 输入: [1,2,1]
# 输出: [2,-1,2]
# 解释: 第一个 1 的下一个更大的数是 2；
# 数字 2 找不到下一个更大的数； 
# 第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
#  
# 
#  注意: 输入数组的长度不会超过 10000。 
#  Related Topics 栈 
#  👍 190 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 单调栈：
        # A[1]放入栈，对于A[2]，如果A[2] > A[1]，就找到了A[1]的下一个更大元素A[2]，
        # 此时把A[1]出栈并把A[2]入栈；如果 A[2] <= A[1]，仅把 A[2] 入栈。
        # 对于 A[3]，此时栈中多个元素，那么所有比 A[3] 小的元素都找到了下一个更大元素（即 A[3]），
        # 因此可以出栈，在这之后，我们将 A[3] 入栈，以此类推
        stack, size = [], len(nums)
        res = [-1] * size

        # 因为循环数组，所以遍历次数增加
        for i in range(size * 2 - 1, -1, -1):
            while (stack and nums[stack[-1]] <= nums[i % size]):
                stack.pop()
            if stack == []:
                res[i%size] = -1
            else:
                res[i%size] = nums[stack[-1]]

            stack.append(i % size)

        return res
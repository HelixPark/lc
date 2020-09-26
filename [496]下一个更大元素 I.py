# 给定两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个
# 比其大的值。 
# 
#  nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。 
# 
#  
# 
#  示例 1: 
# 
#  输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
# 输出: [-1,3,-1]
# 解释:
#     对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
#     对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
#     对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。 
# 
#  示例 2: 
# 
#  输入: nums1 = [2,4], nums2 = [1,2,3,4].
# 输出: [3,-1]
# 解释:
#     对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
#     对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  nums1和nums2中所有元素是唯一的。 
#  nums1和nums2 的数组大小都不超过1000。 
#  
#  Related Topics 栈 
#  👍 266 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 单调栈+hash
        # 倒序遍历nums2，维护nums2中元素右边的数，
        # 如果空栈或者nums2的元素大于栈顶元素值，
        # 弹出直至寻找到大于该元素的值或者空栈为止，
        # 利用哈希记录下一个更大的值，然后将该元素压入栈中。
        # 因为nums1的元素是nums2的子集，
        # 因此，nums2求出以后，逐个哈希查找就可以了
        stack = []
        Hash = {}
        for i in range(len(nums2) - 1, -1, -1):
            x = nums2[i]
            if not stack:
                Hash[x] = -1
            else:
                while stack and x > stack[-1]:
                    stack.pop()
                Hash[x] = stack[-1] if stack else -1
            stack.append(x)

        for j in range(len(nums1)):
            nums1[j] = Hash[nums1[j]]

        return nums1
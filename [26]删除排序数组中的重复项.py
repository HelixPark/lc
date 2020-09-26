# 给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。 
# 
#  不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。 
# 
#  
# 
#  示例 1: 
# 
#  给定数组 nums = [1,1,2], 
# 
# 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 
# 
# 你不需要考虑数组中超出新长度后面的元素。 
# 
#  示例 2: 
# 
#  给定 nums = [0,0,1,1,1,2,2,3,3,4],
# 
# 函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
# 
# 你不需要考虑数组中超出新长度后面的元素。
#  
# 
#  
# 
#  说明: 
# 
#  为什么返回数值是整数，但输出的答案是数组呢? 
# 
#  请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。 
# 
#  你可以想象内部操作如下: 
# 
#  // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
# int len = removeDuplicates(nums);
# 
# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }
#  
#  Related Topics 数组 双指针 
#  👍 1529 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def removeDuplicates1(self, nums: List[int]) -> int:
        # 基础方法：一个个比较
        for i in range(len(nums)-1, 0, -1):
            tmp = nums[i]
            if nums[i-1] == tmp:
                nums.pop(i-1)
        return len(nums)

    def removeDuplicates(self, nums: List[int]) -> int:
        # 双指针（快慢指针）：slow指针在后面，fast在前面，找到一个不重复的元素就让slow前进一步，
        # 当fast遍历整个数组后，nums{0.。slow}就是不重复元素
        # 同理，有序链表去重类似，就是把赋值变为链表赋值
        n = len(nums)
        if n == 0: return 0

        slow, fast = 0, 1
        while fast < n:
            # 找到不重复
            if nums[fast] != nums[slow]:
                slow += 1
                # 维护nums[0..slow]
                nums[slow] = nums[fast]

            fast += 1

        return slow + 1



nums = [0,0,1,1,1,2,2,3,3,4]
c = Solution()
print(c.removeDuplicates(nums))
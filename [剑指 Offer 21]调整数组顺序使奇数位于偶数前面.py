# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。 
# 
#  
# 
#  示例： 
# 
#  输入：nums = [1,2,3,4]
# 输出：[1,3,2,4] 
# 注：[3,1,2,4] 也是正确的答案之一。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 50000 
#  1 <= nums[i] <= 10000 
#  
#  👍 44 👎 0


class Solution:
    def exchange1(self, nums: List[int]) -> List[int]:
        # 奇数在前，偶数在后。双指针：两边往中间走
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] % 2 != 0:
                # 直到指向为偶数
                left += 1
                continue
            if  nums[right] % 2 != 1:
                # 直到指向为奇数
                right -= 1
                continue
            # 交换
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums

    def exchange(self, nums: List[int]) -> List[int]:
        # 快慢双指针：
        # fast在前向前搜索奇数的位置，slow是指向下一个奇数存放的位置
        # fast搜索到奇数时，和slow交换，然后slow向后移动一个
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] % 2 == 1:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
        return nums

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
        # 思路：先数组排序，在定义一个i指针，再定义两个指针former、latter
        # 首先i循环，然后former、latter在i之后循环
        # 判断是否有符合条案件的三元组，若有则更新former、latter位置
        # 在former《latter的范围内若有重复的则直接跳过
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i - 1]:
                former, latter = i + 1, len(nums) - 1
                while former < latter:
                    s = nums[i] + nums[former] + nums[latter]
                    if s == 0:
                        res.append([nums[i], nums[former], nums[latter]])
                        former += 1
                        latter -= 1
                        while former < latter and nums[former] == nums[former - 1]:
                            former += 1
                        while former < latter and nums[latter] == nums[latter + 1]:
                            latter -= 1
                    elif s > 0:
                        latter -= 1
                    else:
                        former += 1
        return res

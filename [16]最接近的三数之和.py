from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 是否存在三个元素 a，b，c ，使得 a + b + c = target ？
        # 思路：先数组排序，在定义一个i指针，再定义两个指针former、latter
        # 首先i循环，然后former、latter在i之后循环
        # 判断三元组与target的距离，若有则更新former、latter位置
        nums.sort()
        minDis, res = float('inf'), []
        for i in range(len(nums)-2):
            former, latter = i + 1, len(nums) - 1
            while former < latter:
                Sum = nums[i] + nums[former] + nums[latter]
                if abs(Sum-target) < minDis:
                    minDis = abs(Sum-target)
                    res.clear()
                    res.extend([nums[i], nums[former], nums[latter]])

                if Sum > target:
                    latter -= 1
                elif Sum < target:
                    former += 1
                else:
                    # 相等即最近
                    return Sum
        return sum(res)


# nums = [-1,2,1,-4]
# target = 1
# c=Solution()
# c.threeSumClosest(nums,target)
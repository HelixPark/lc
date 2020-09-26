from typing import List
class Solution:
    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 循环短的数组，如果在长数组里面有当前值则删掉长数组的，并将当前值加入结果集
        # 超时
        if len(nums1) == 0:
            return []
        if len(nums2) == 0:
            return []

        long, short = nums1, nums2
        if len(nums1) < len(nums2):
            long, short = nums2, nums1
        res = []
        for i in short:
            if i in long:
                res.append(i)
                long.remove(i)
        return res

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 用hash存，第一个数组的元素和出现次数，
        # 遍历第二个数组，若元素在hash中出现，则hash中次数减去1并添加到res
        if len(nums1) == 0:
            return []
        if len(nums2) == 0:
            return []

        long, short = nums1, nums2
        if len(nums1) < len(nums2):
            long, short = nums2, nums1

        dict = {}
        for num in short:
            if dict.get(num) == None:
                dict[num] = 1
            else:
                dict[num] += 1

        res = []
        for num in long:
            # 在hash中能找到且次数大于0
            if dict.get(num) != None and dict[num] > 0:
                res.append(num)
                dict[num] -= 1
        return res

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
c = Solution()
c.intersect(nums1,nums2)



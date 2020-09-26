

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left[i]为i左边的元素乘积，同理
        left, right = [1] * len(nums), [1] * len(nums)

        size = len(nums)
        for i in range(1,size):
            left[i] = left[i-1] * nums[i-1]
        for j in range(size-2,-1,-1):
            right[j] = right[j+1] * nums[j+1]

        res = []
        for i in range(size):
            res.append(left[i] * right[i])
        return res
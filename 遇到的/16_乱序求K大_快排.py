import random
class Solution:
    def findKthLargest(self, nums, k):
        # kth largest is (n - k)th smallest
        length = len(nums)
        target = length - k  # 因为数组下标从零开始，有第0小的元素
        low, high = 0, length - 1

        k = random.randint(low, high)
        nums[low], nums[k] = nums[k], nums[low]
        while True:
            index = self.partition(nums, low, high)
            if index == target:
                return nums[index]
            elif index < target:
                low = index + 1
            else:
                high = index - 1


    def partition(self, nums, low, high):
        # j 慢指针，记录分割处
        pivot, j = nums[low], low
        for i in range(low + 1, high + 1):
            # 当前元素小于等于pivot
            if nums[i] <= pivot:
                j += 1
                nums[j], nums[i] = nums[i], nums[j]
        nums[low], nums[j] = nums[j], nums[low]
        return j
    # 快排
    def quickSort(self, nums, left, right):
        if left < right:
            index = self.partition(nums, left, right)
            self.quickSort(nums, left, index-1)
            self.quickSort(nums, index+1, right)


nums = [3, 2, 1, 5, 6, 4]
a = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
s = Solution()
print(s.findKthLargest(nums, 6))
print(s.findKthLargest(a, k))
s.quickSort(nums,0,len(nums)-1)
s.quickSort(a,0,len(a)-1)
print(nums)
print(a)
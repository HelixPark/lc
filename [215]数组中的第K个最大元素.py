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

    def findKthLargest2(self, nums, k):
        # 用堆排序
        # global length
        length = len(nums)  # 记录堆的大小，以为堆顶删除后，大小改变

        if k > length:
            return

        # 实现K次堆化，找到第k个最大元素
        self.buildMaxHeap(nums)
        print("建堆后的大根堆的堆顶：", nums[0])
        count = 0

        # 注意i从len（nums）- 1 至 1
        for i in range(len(nums) - 1, 0, -1):
            self.swap(nums, 0, i)  # 将堆顶的元素（最大数）放到数组的末尾i

            length -= 1  # 堆中元素-1（必须）！！
            count += 1
            if count == k:
                return nums[i]
            self.heapify(nums, 0, length)  # 重新进行堆化
        # 说明k == len(nums)
        return nums[0]

    # 建堆
    def buildMaxHeap(self, nums):
        import math
        for i in range(math.floor(len(nums) / 2), -1, -1):
            self.heapify(nums, i, len(nums))

    # 堆化
    def heapify(self, nums, i, length):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < length and nums[left] > nums[largest]:  # 注意使用到了全局变量
            largest = left
        if right < length and nums[right] > nums[largest]:
            largest = right
        if largest != i:
            self.swap(nums, i, largest)
            self.heapify(nums, largest, length)  # 递归：看孩子的孩子节点

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]


nums = [3, 2, 1, 5, 6, 4]
a = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
s = Solution()
print(s.findKthLargest(nums, k))
print(s.findKthLargest(a, k))
s.quickSort(nums,0,len(nums)-1)
s.quickSort(a,0,len(a)-1)
print(nums)
print(a)
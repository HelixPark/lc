# -*- coding:utf-8 -*-
def findKthLargest2(self, nums, k):
    # 用堆排序    # LC215
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
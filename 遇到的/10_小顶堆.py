# -*- coding:utf-8 -*-
# utf-8
    # 将待排序序列构造成一个大顶堆，此时，整个序列的最大值就是堆顶的根节点。
    # 将其与末尾元素进行交换，此时末尾就为最大值。
    # 然后将剩余n-1个元素重新构造成一个堆，这样会得到n个元素的次小值。
    # 如此反复执行，便能得到一个有序序列了
    # a.将无需序列构建成一个堆，根据升序降序需求选择大顶堆或小顶堆;
    # b.将堆顶元素与末尾元素交换，将最大元素"沉"到数组末端;
    # c.重新调整结构，使其满足堆定义，然后继续交换堆顶元素与当前末尾元素，反复执行调整 + 交换步骤，直到整个序列有序。
def heapify(nums, n, i):
    # 大顶堆
    minor = i
    left = 2 * i + 1
    right = 2 * i + 2
    # xiao顶堆：交换位置
    if left < n and nums[i] > nums[left]:
        minor = left

    if right < n and nums[minor] > nums[right]:
        minor = right

    if minor != i:
        nums[i], nums[minor] = nums[minor], nums[i]

        heapify(nums, n, minor)

def heapSort(nums):
    n = len(nums)

    # 建立minheap
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # 一个个交换元素
    for i in range(n-1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

nums = [1,3,2,5,7,6]

heapSort(nums)
print(nums)
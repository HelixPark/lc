
def selectSort(nums):
    n = len(nums)
    for i in range(n):
        index = i
        # 找到最小元素的下标
        for j in range(i, n):
            if nums[j] < nums[index]:
                index = j

        # 交换元素
        tmp = nums[index]
        nums[index] = nums[i]
        nums[i] = tmp

nums = [1,3,2,5,7,6]
selectSort(nums)
print(nums)
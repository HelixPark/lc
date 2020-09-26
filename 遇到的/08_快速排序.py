# uft-8
def Index(nums, left, right):

    i, j = left, right
    base = nums[left]

    while i < j:
        # 从右向左找第一个小于base的数
        while i < j and nums[j] >= base:
            j -= 1
        if i < j:
            nums[i] = nums[j]
            i += 1

        # 从左向右找第一个大于base的数
        while i < j and nums[i] < base:
            i += 1
        if i < j:
            nums[j] = nums[i]
            j -= 1
    nums[i] = base
    return i

def partition(nums, left, right):
    i = left - 1
    base = nums[right]

    for j in range(left, right):
        # 当前元素小于或等于base
        if nums[j] <= base:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i+1], nums[right] = nums[right], nums[i+1]
    return i+1

def quickSort(nums, left, right):
    if left < right:
        # index = Index(nums, left, right)
        index = partition(nums, left, right)

        quickSort(nums,left,index-1)
        quickSort(nums,index+1,right)
        # print(nums)

def findkth(num, low, high, k):  # 找到数组里第k个数
    index = partition(num, low, high)
    # print((partition(num, low, high))[1])
    if index == k: return num[index]
    if index < k:
        return findkth(num, index + 1, high, k)
    else:
        return findkth(num, low, index - 1, k)


print(findkth([6, 1, 3, 9, 2], 0, len([6, 1, 3, 9, 2]) - 1, 0))

# nums = [1,4,2,5,7,6]
nums = [10, 7, 8, 9, 1, 5]
# quickSort(nums,0, len(nums)-1)
print(nums)
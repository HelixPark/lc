
def index(nums,left,right):
    i, j = left, right
    base = nums[left]
    # 重新排序数列，所有比基准值小的元素摆放在基准前面，
    # 所有比基准值大的元素摆在基准后面
    while i < j:
        # 从右向左找到比base小的数
        while i < j and nums[j] >= base:
            j -= 1
        if i < j:
            nums[i] = nums[j]
            i += 1
        # 从左往右找到比base大的数
        while i < j and nums[i] < base:
            i += 1
        if i < j:
            nums[j] = nums[i]
            j -= 1
    nums[i] = base
    return i

def quickSort(nums, left, right):
    if left < right:
        k = index(nums, left, right)
        quickSort(nums,left,k-1)
        quickSort(nums,k+1,right)

def topK(nums,k):
    length = len(nums)
    target = length - k
    low, high = 0, length-1

    # 数组小标从0开始，要减去1
    nums[low], nums[k-1] = nums[k-1], nums[low]
    while True:
        idx = index(nums,low,high)
        if idx == target:
            return nums[idx]
        elif idx < target:
            low = idx + 1
        else:
            high = idx - 1


nums = [1,4,2,5,7,6]
print(topK(nums,2))
print(topK(nums,6))
quickSort(nums,0,len(nums)-1)

print(nums)
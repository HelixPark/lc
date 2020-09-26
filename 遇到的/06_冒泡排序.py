
def bubbleSort(nums):
    n = len(nums)
    for i in range(0,n):
        # 前面的大于后面的则进行交换,每次大的往后移动
        for j in range(0, n - i -1):
            if nums[j] > nums[j+1]:
                tmp = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = tmp
        print(nums)
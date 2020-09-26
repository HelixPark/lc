
def insertSort(nums):
    n = len(nums)
    for i in range(1,n):
        # Nums[0]有序，1无序
        # 无序序列的元素小于有序序列的最后一个时，移动有序表再插入
        if nums[i] < nums[i-1]:
            tmp = nums[i]
            j = i - 1
            # 从右往左移动有序表
            while tmp < nums[j] and j > -1:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = tmp
    print(nums)
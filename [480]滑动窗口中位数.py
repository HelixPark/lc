# 中位数是有序序列最中间的那个数。如果序列的大小是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。 
# 
#  例如： 
# 
#  
#  [2,3,4]，中位数是 3 
#  [2,3]，中位数是 (2 + 3) / 2 = 2.5 
#  
# 
#  给你一个数组 nums，有一个大小为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1 位。你的任务是找出每次窗口移动后得到的新窗
# 口中元素的中位数，并输出由它们组成的数组。 
# 
#  
# 
#  示例： 
# 
#  给出 nums = [1,3,-1,-3,5,3,6,7]，以及 k = 3。 
# 
#  窗口位置                      中位数
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       1
#  1 [3  -1  -3] 5  3  6  7      -1
#  1  3 [-1  -3  5] 3  6  7      -1
#  1  3  -1 [-3  5  3] 6  7       3
#  1  3  -1  -3 [5  3  6] 7       5
#  1  3  -1  -3  5 [3  6  7]      6
#  
# 
#  因此，返回该滑动窗口的中位数数组 [1,-1,-1,3,5,6]。 
# 
#  
# 
#  提示： 
# 
#  
#  你可以假设 k 始终有效，即：k 始终小于输入的非空数组的元素个数。 
#  与真实值误差在 10 ^ -5 以内的答案将被视作正确答案。 
#  
#  Related Topics Sliding Window 
#  👍 104 👎 0

class Solution:
    def medianSlidingWindow1(self, nums: List[int], k: int) -> List[float]:
        # 二分法，需要借助bisect这个库（前提数组有序）
        import bisect
        arr,res,left = [],[],0
        for right in range(len(nums)):
            # 按排序位置插入
            bisect.insort(arr, nums[right])
            while len(arr) > k:
                arr.pop(bisect.bisect_left(arr, nums[left]))
                left += 1
            if len(arr) == k:
                res.append((arr[k // 2] + arr[(k - 1) // 2]) / 2.0)
        return res
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # 维护大小为k的窗口有序，并用二分法插入新的元素。直接套用 sliding window 模板
        import bisect
        lo, hi = 0, 0
        ans = []
        window = []
        # 套用 sliding window 模板
        while hi < len(nums):
            # 第一步，入窗就完事了
            bisect.insort_left(window, nums[hi])
            # 第二步，维护窗口，该出窗得出窗
            while len(window) > k:
                # 出窗
                window.pop(bisect.bisect_left(window, nums[lo]))
                # 窗口左端收缩
                lo += 1
            # 第三步，做该做的事
            if len(window) == k:
                # 注意这个求中位数的表达式，无论len(window)奇偶都如此
                ans.append((window[k // 2] + window[(k - 1) // 2]) / 2)
            # 最后，窗口右端始终右移，在路上
            hi += 1
        return ans
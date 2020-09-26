# 搜索旋转数组。给定一个排序后的数组，包含n个整数，但这个数组已被旋转过很多次了，次数不详。请编写代码找出数组中的某个元素，假设数组元素原先是按升序排列的。若
# 有多个相同元素，返回索引值最小的一个。 
# 
#  示例1: 
# 
#   输入: arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 5
#  输出: 8（元素5在该数组中的索引）
#  
# 
#  示例2: 
# 
#   输入：arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 11
#  输出：-1 （没有找到）
#  
# 
#  提示: 
# 
#  
#  arr 长度范围在[1, 1000000]之间 
#  
#  Related Topics 数组 二分查找 
#  👍 28 👎 0

from typing import List
class Solution:
    def search(self, arr: List[int], target: int) -> int:
        left, right = 0, len(arr)-1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < arr[left]:
                # 都是先比较纯升序那段：target比中值大且比right小，则往右边走，否则左走
                if target >= arr[left] or target <= arr[mid]:
                    right = mid
                else:
                    left = mid + 1
            # 中值大于left，说明旋转点在mid后面，左边升序
            elif arr[mid] > arr[left]:
                # 都是先比较纯升序那段，target小于mid且大于left，往左边走，否则右边（含旋转点）走
                if target <= arr[mid] and target >= arr[left]:
                    right = mid
                else:
                    left = mid + 1
            elif arr[left] == arr[mid]:
                # 如果左值等于中值，可能是已经找到了目标，也可能是遇到了重复值
                if arr[left] != target:
                    left += 1  #重复值
                else:
                    right = left  #找到了，

        if arr[left] == target:
            return left
        else:
            return -1
# nums = [1,1,1,1,1,2,1,1,1]
nums = [5,5,5,1,2,3,4,5]
c = Solution()
c.search(nums,5)
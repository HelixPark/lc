# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2
# ] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。 
# 
#  示例 1： 
# 
#  输入：[3,4,5,1,2]
# 输出：1
#  
# 
#  示例 2： 
# 
#  输入：[2,2,2,0,1]
# 输出：0
#  
# 
#  注意：本题与主站 154 题相同：https://leetcode-cn.com/problems/find-minimum-in-rotated-sor
# ted-array-ii/ 
#  Related Topics 二分查找 
#  👍 153 👎 0

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left, right = 0, len(numbers)-1
        while left < right:
            mid = left + (right - left) // 2
            if numbers[mid] > numbers[right]:   #最小值在右边，往右边走
                left = mid + 1
            elif numbers[mid] < numbers[right]:   #最小值在左边，往左边走
                right = mid
            else:
                # 相等时，有重复，直接right-1
                right -= 1
        return numbers[left]
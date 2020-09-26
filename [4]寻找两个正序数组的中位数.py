# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。 
# 
#  请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。 
# 
#  你可以假设 nums1 和 nums2 不会同时为空。 
# 
#  
# 
#  示例 1: 
# 
#  nums1 = [1, 3]
# nums2 = [2]
# 
# 则中位数是 2.0
#  
# 
#  示例 2: 
# 
#  nums1 = [1, 2]
# nums2 = [3, 4]
# 
# 则中位数是 (2 + 3)/2 = 2.5
#  
#  Related Topics 数组 二分查找 分治算法 
#  👍 3232 👎 0


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 方式1：若没限制在o(log(m+n)),使用o(m+n),则可两个指针分别指向两个数组，比较指针下的元素大小，一共移动(m+n+1)/2次
        # 方式2：变相换成找k小的元素，k为合并后数组的中位数索引
        # 取两个数组的第k/2个元素进行比较，如果数组1的元素小于数组2的元素，则说明数组1中的前k/2个元素不可能成为第k个元素的候选，
        # 所以将数组1中的前k/2个元素去掉，组成新数组和数组2求第k- k/2小的元素，
        # 因为我们把前k/2个元素去掉了，所以相应的k值也应该减小。
        def findKth(nums1,nums2,k):
            size1, size2 = len(nums1), len(nums2)
            if size1 > size2:
                return findKth(nums2,nums1,k)
            if not nums1:
                return nums2[k-1]
            if k == 1:
                return min(nums1[0], nums2[0])
            i, j = min(k//2, size1) - 1, min(k//2, size2) - 1
            if nums1[i] > nums2[j]:
                return findKth(nums1, nums2[j+1:],k-j-1)
            else:
                return findKth(nums1[i+1:],nums2,k-i-1)
        l1, l2 = len(nums1), len(nums2)
        left, right = (l1+l2+1)//2, (l1+l2+2)//2
        former = findKth(nums1, nums2,left)
        latter = findKth(nums1,nums2,right)
        return (former+latter) / 2

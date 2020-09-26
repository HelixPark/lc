import sys
from typing import List
class Solution:
    def trap1(self, height: List[int]) -> int:
    # leetcode submit region end(Prohibit modification and deletion)
        left, right = 0, len(height) - 1
        ds = 0
        h = 0
        while left <= right:
            if height[left] < height[right]:
                if height[left] > h:
                    ds += (height[left] - h) * (right - left + 1)
                    h = height[left]
                left += 1
            else:
                if height[right] > h:
                    ds += (height[right] - h) * (right - left + 1)
                    h = height[right]
                right -= 1
        return ds - sum(height)

    def trap2(self, height: List[int]) -> int:
        # 暴力解法：超时
        n = len(height)
        res = 0
        for i in range(1, n-1):
            left, right = 0, 0
            # 寻找左边最高的柱子
            for j in range(i,-1,-1):
                left = max(left, height[j])

            # 寻找右边最高的柱子
            for j in range(i,n,1):
                right = max(right, height[j])
            # i处的雨水取决于左右两边最低的那个柱子 - 当前高度
            res += min(left, right) - height[i]
        return res

    def trap3(self, height: List[int]) -> int:
        # 带记忆的暴力，数组r_max和l_max充当记忆，
        # l_max[i]表⽰位置i左边最⾼的柱⼦⾼度，r_max[i]表⽰位置i右边最⾼的柱⼦⾼度。
        # 预先把这两个数组计算好，避免重复计算
        n = len(height)
        if n <= 2:
            return 0
        left_max, right_max = [], []

        left_max.append(height[0])
        right_max.append(height[n-1])

        # 从左向右计算l_max
        for i in range(1,n):
            left_max.append(max(left_max[i - 1], height[i]))
        # 从右向左计算r_max:逆向
        for i in range(n-2,-1,-1):
            right_max.insert(0, max(right_max[0], height[i]))

        res = 0
        for i in range(1, n-1):
            res += min(left_max[i], right_max[i]) - height[i]
        return res

    def trap(self, height: List[int]) -> int:
        # 双指针法
        n = len(height)
        if n <= 2:
            return 0
        # leftmax是height[0..left]的最高高度，右边height[right..end]同理
        left, right = 0, n - 1
        left_max, right_max = height[0], height[-1]

        res = 0
        while left <= right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max:
                res += left_max - height[left]
                left += 1
            else:
                res += right_max - height[right]
                right -= 1
        return res


h = [0,1,0,2,1,0,1,3,2,1,2,1]
c = Solution()
print(c.trap(h))
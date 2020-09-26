# -*- coding:utf-8 -*-
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
#  求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
#
#
#
#
#  以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
#
#
#
#
#
#  图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
#
#
#
#  示例:
#
#  输入: [2,1,5,6,2,3]
# 输出: 10
#  Related Topics 栈 数组
#  👍 870 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
# utf-8
class Solution:
    def largestRectangleArea1(self, heights: List[int]) -> int:
        # 暴力解：向两端延伸
        # 依次遍历柱形的高度，对于每一个高度分别向两边扩散，
        # 求出以当前高度为矩形的最大宽度多少
        # 左边看一下，看最多能向左延伸多长，
        # 找到大于等于当前柱形高度的最左边元素的下标
        # 右边同理
        n = len(heights)
        res = 0

        for i in range(n):
            cur_height = heights[i]

            left = i
            while left > 0 and heights[left-1] >= cur_height:
                left -= 1

            right = i
            while right < n-1 and heights[right+1] >= cur_height:
                right += 1

            res = max(res, (right - left + 1) * cur_height)
        return res

    def largestRectangleArea2(self, heights: List[int]) -> int:
        # 单调栈1：索引入栈
        size = len(heights)
        res = 0

        stack = []

        for i in range(size):
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]

                while len(stack) > 0 and cur_height == heights[stack[-1]]:
                    stack.pop()

                if len(stack) > 0:
                    cur_width = i - stack[-1] - 1
                else:
                    cur_width = i

                res = max(res, cur_height * cur_width)
            stack.append(i)

        while len(stack) > 0 is not None:
            cur_height = heights[stack.pop()]
            while len(stack) > 0 and cur_height == heights[stack[-1]]:
                stack.pop()

            if len(stack) > 0:
                cur_width = size - stack[-1] - 1
            else:
                cur_width = size
            res = max(res, cur_height * cur_width)

        return res

    def largestRectangleArea(self, heights: List[int]) -> int:
        # 单调栈2：维护一个单调递增栈,存放的是索引
        # heights头和heights尾各加一个0,方便计算

        stack, res = [], 0
        heights = [0] + heights + [0]

        for i in range(len(heights)):
            # 比较栈顶元素和当前元素，若大于则出栈，否则入栈
            # while循环，找到栈内比当前元素大的（第一个比当前小的停止）
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i-stack[-1]-1) * heights[tmp])
            stack.append(i)
        return res

c = Solution()
heights = [2,1,5,6,2,3]
print(c.largestRectangleArea(heights))


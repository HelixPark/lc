from typing import List
# utf-8
# 输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        # 按照区间的start升序排列，
        intervals.sort(key=lambda intv: intv[0])
        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            curr = intervals[i]
            # 比较当前的start和上一个的end大小
            pre = res[-1]

            if curr[0] <= pre[1]:
                # 说明有重叠,找最大
                pre[1] = max(pre[1], curr[1])
            else:
                res.append(curr)
        return res

nums = [[1,3],[3,4],[2,6],[8,10],[15,18]]
c = Solution()
c.merge(nums)
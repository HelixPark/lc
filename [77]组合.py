from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first = 1, curr = []):
            # 符合条件：组合完成
            if len(curr) == k:
                # 这里加return相当于尾巴剪枝，不遍历那么深，不加也run，时间长点儿
               return res.append(curr[:])

            # 遍历选择列表，以first为起点，也是相当于剪枝，排除之前索引过的数字
            for i in range(first,n+1):
                # 选择：把第i个添加到curr
                curr.append(i)
                # 回溯
                backtrack(i+1,curr)
                # 撤销选择:默认最后一个
                curr.pop()


        res = []
        backtrack()
        return res

n, k = 4, 2
c = Solution()
c.combine(n,k)
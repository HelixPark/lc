from typing import List
class Solution:
    def permute1(self, nums: List[int]) -> List[List[int]]:
        # 全排列：只需交换元素位置即可，不用curr数组
        def backtrack(first = 0):
            # 符合条件，排列完成
            if first == l:
                return res.append(nums[:])

            # 遍历选择列表
            for i in range(first,l):
                # 选择：维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 回溯
                backtrack(first+1)
                # 撤销选择
                nums[first], nums[i] = nums[i], nums[first]


        res, l = [], len(nums)
        backtrack()
        return res

    # DFS全排列:标准
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 全排列：first可代表深度，这里描述为数组长度
        def backtrack(curr):
            # 符合条件，排列完成
            if len(curr) == l:
                return res.append(curr[:])

            # 遍历选择列表
            for i in range(0,l):
                # 检查是否被访问过
                if visited[i] == True:
                    continue
                # 选择:
                curr.append(nums[i])
                visited[i] = True
                # 回溯
                backtrack(curr)
                # 撤销选择
                curr.pop()
                visited[i] = False

        res, l = [], len(nums)
        visited = [False] * l
        backtrack([])
        return res

nums = [1,2,3]
c = Solution()
c.permute(nums)


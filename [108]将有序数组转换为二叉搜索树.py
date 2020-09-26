from typing import List
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # 把前缀和nums[0..i] 加⼊并记录出现次数

        return self.dfs(nums, 0, len(nums) - 1)

    def dfs(self, nums: List[int], left: int, right: int) -> TreeNode:
        if (left <= right):
            mid = left + (right - left) // 2
            root = TreeNode(nums[mid])
            root.left = self.dfs(nums, left, mid - 1)
            root.right = self.dfs(nums, mid + 1, right)
            return root

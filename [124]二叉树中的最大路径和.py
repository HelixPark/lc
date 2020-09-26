


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = float('-inf')
    def maxPathSum(self, root: TreeNode) -> int:

        def dfs(root):
            if not root:
                return 0

            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于0时，才会选取对应子节点
            left = max(dfs(root.left), 0)
            right = max((dfs(root.right)),0)

            # 该节点的最大路径和取决于该节点的值和其左右子节点的贡献值
            self.res = max(self.res, left + right + root.val)
            # 返回节点的最大贡献值
            return max(left,right) + root.val

        dfs(root)
        return self.res
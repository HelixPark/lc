# 给定一棵二叉搜索树，请找出其中第k大的节点。 
# 
#  
# 
#  示例 1: 
# 
#  输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# 输出: 4 
# 
#  示例 2: 
# 
#  输入: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# 输出: 4 
# 
#  
# 
#  限制： 
# 
#  1 ≤ k ≤ 二叉搜索树元素个数 
#  Related Topics 树 
#  👍 68 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest1(self, root: TreeNode, k: int) -> int:
        # 二叉搜索树的中序遍历为升序,所以用中序的倒序
        # 递归遍历时计数，统计当前节点的序号；
        # 递归到第k个节点时，应记录结果resres ；
        # 记录结果后，后续的遍历即失去意义，应提前终止（即返回）
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            if self.k == 0:
                return
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            dfs(root.left)

        self.k, self.res = k, 0
        dfs(root)
        return self.res
    def kthLargest(self, root: TreeNode, k: int) -> int:
        # 右根左，非递归遍历
        stack, p, count = [], root, 0
        while p or stack:
            while p:
                stack.append(p)
                p = p.right
            if stack:
                cur = stack.pop()
                count += 1
                if count == k:
                    return cur.val
                p = cur.left

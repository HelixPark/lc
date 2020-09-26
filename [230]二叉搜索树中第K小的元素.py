# 给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。 
# 
#  说明： 
# 你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。 
# 
#  示例 1: 
# 
#  输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# 输出: 1 
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
# 输出: 3 
# 
#  进阶： 
# 如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？ 
#  Related Topics 树 二分查找 
#  👍 282 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # 递归：构造BST的中序遍历序列，k-1个元素就是k小的元素
        def inorder(r):
            return inorder(r.left) + [r.val] + \
                   inorder(r.right) if r else []
        return inorder(root)[k - 1]

    def kthSmallest1(self, root: TreeNode, k: int) -> int:
        # 迭代：不用遍历整个数，使用栈
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                # 找到了就停止
                return root.val
            root = root.right

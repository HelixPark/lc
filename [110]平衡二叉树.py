# 给定一个二叉树，判断它是否是高度平衡的二叉树。 
# 
#  本题中，一棵高度平衡二叉树定义为： 
# 
#  
#  一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。 
#  
# 
#  示例 1: 
# 
#  给定二叉树 [3,9,20,null,null,15,7] 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7 
# 
#  返回 true 。 
#  
# 示例 2: 
# 
#  给定二叉树 [1,2,2,3,3,null,null,4,4] 
# 
#         1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
#  
# 
#  返回 false 。 
# 
#  
#  Related Topics 树 深度优先搜索 
#  👍 463 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 自顶向下的递归:遍历一个节点，先计算左右子树的高度
        # 小于1则递归遍历左和右节点，判断是否平衡
        # 时间o(nn), o(n)
        def height(root):
            if not root:
                return 0
            return max(height(root.left),height(root.right)) + 1
        if not root:
            return True
        return abs(height(root.left) - height(root.right)) <= 1 \
               and self.isBalanced(root.left) and self.isBalanced(root.right)

    def isBalanced1(self, root: TreeNode) -> bool:
        # 自底而上递归o(n),o(n)
        def height(root):
            if not root:
                return 0

            left = height(root.left)
            right = height(root.right)
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            else:
                return max(left, right) + 1
        return height(root) >= 0
    def isBalanced2(self, root: TreeNode) -> bool:
        # 自底而上递归，带提前阻断（剪枝）o(n),o(n)
        def recur(root):
            if not root:
                return 0
            left = recur(root.left)
            if left == -1:return -1  #提前阻断
            right = recur(root.right)
            if right == -1:return -1
            if abs(left - right) < 2:
                return max(left, right) + 1
            else:
                return -1
        return recur(root) != -1

# 翻转一棵二叉树。 
# 
#  示例： 
# 
#  输入： 
# 
#       4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9 
# 
#  输出： 
# 
#       4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1 
# 
#  备注: 
# 这个问题是受到 Max Howell 的 原问题 启发的 ： 
# 
#  谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。 
#  Related Topics 树 
#  👍 631 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 方式1：递归
        if not root:
            return root
        # 将当前节点的左右子树交换
        root.left, root.right = root.right, root.left
        # 递归交换当前节点的 左子树和右子树
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    def invertTree1(self, root: TreeNode) -> TreeNode:
        # 方式2：迭代，用BFS和栈
        if not root:
            return None
        # 将二叉树中的节点逐层放入队列中，再迭代处理队列中的元素
        queue = [root]
        while queue:
            # 每次都从队列中拿一个节点，并交换这个节点的左右子树
            cur = queue.pop(0)
            cur.left, cur.right = cur.right, cur.left
            # 如果左子树不为空，则放入队列等待后续处理
            if cur.left:
                queue.append(cur.left)
            # 如果右子树不为空，则放入队列等待后续处理
            if cur.right:
                queue.append(cur.right)
        return root
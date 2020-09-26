# 给定一个二叉树，返回它的中序 遍历。 
# 
#  示例: 
# 
#  输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# 
# 输出: [1,3,2] 
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 哈希表 
#  👍 657 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        # 递归方式1
        if root == None:
            return []
        return self.inorderTraversal1(root.left) \
               + [root.val] \
               + self.inorderTraversal1(root.right)
    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        # 递归方式2: 可修改条件
        def dfs(cur):
            if cur == None:
                return []
            dfs(cur.left)
            res.append(cur.val)
            dfs(cur.right)

        res = []
        dfs(root)
        return res

    def inorderTraversal3(self, root: TreeNode) -> List[int]:
        # 迭代2：迭代1不适用中序
        res, stack = [], []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
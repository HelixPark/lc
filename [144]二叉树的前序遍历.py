# 给定一个二叉树，返回它的 前序 遍历。 
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
# 输出: [1,2,3]
#  
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 
#  👍 356 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        # 递归方式1:标准模板
        if root == None:
            return []
        return [root.val] \
               + self.preorderTraversal1(root.left) \
               + self.preorderTraversal1(root.right)


    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        # 递归方式2：通用模板，可修改添加条件
        def dfs(cur):
            if not cur:
                return
            res.append(cur.val)
            dfs(cur.left)
            dfs(cur.right)
        res = []
        dfs(root)
        return res

    def preorderTraversal3(self, root: TreeNode) -> List[int]:
        # 迭代方式1：DFS(只适合前和后，中序用迭代2)
        # 从根节点开始，每次迭代弹出当前栈顶元素，并将其孩子节点压入栈中，
        # 先压右孩子再压左孩子
        if root == None:
            return []
        # 维护一个栈，先放右再放左
        stack, res = [root], []
        while len(stack) > 0:
            root = stack.pop()
            if root != None:
                res.append(root.val)
                if root.right != None:
                    stack.append(root.right)
                if root.left != None:
                    stack.append(root.left)
        return res

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 迭代2：前中后都可用，维护一个栈空间
        res, stack = [], []
        cur = root
        while stack or cur:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        return res

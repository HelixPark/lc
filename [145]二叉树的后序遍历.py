# 给定一个二叉树，返回它的 后序 遍历。 
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
# 输出: [3,2,1] 
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 
#  👍 387 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        # 递归方式1:标准模板
        if root == None:
            return []
        return self.postorderTraversal1(root.left) \
               + self.postorderTraversal1(root.right) \
               + [root.val]

    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        # 递归方式2：通用模板，可修改添加条件
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            dfs(cur.right)
            res.append(cur.val)

        res = []
        dfs(root)
        return res

    def postorderTraversal3(self, root: TreeNode) -> List[int]:
        # 迭代方式1：DFS(只适合前和后，中序用迭代2)
        # 从根节点开始，每次迭代弹出当前栈顶元素，并将其孩子节点压入栈中，
        # 先压zuo孩子再压you孩子
        if root == None:
            return []
        # 维护一个栈，先放右再放左
        stack, res = [root], []
        while len(stack) > 0:
            root = stack.pop()
            if root != None:
                if root.left != None:
                    stack.append(root.left)
                if root.right != None:
                    stack.append(root.right)
                res.append(root.val)
        return res[::-1]

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 迭代2：前中后都可用，维护一个栈空间
        res, stack = [], []
        cur = root
        while stack or cur:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            cur = cur.left
        return res[::-1]

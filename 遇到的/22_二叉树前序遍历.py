# -*- coding:utf-8 -*-
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
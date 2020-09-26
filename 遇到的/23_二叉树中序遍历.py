# -*- coding:utf-8 -*-
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
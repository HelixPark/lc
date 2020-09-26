# -*- coding:utf-8 -*-
class Solution:
    def preorder1(self, root: 'Node') -> List[int]:
        # 递归1：
        if not root:
            return []
        res = [root.val]
        for node in root.children:
            res.extend(self.preorder(node))
        return res
    def preorder2(self, root: 'Node') -> List[int]:
        # 递归2
        res = []
        def dfs(root):
            if not root:
                return
            res.append(root.val)
            for child in root.children:
                dfs(child)
        dfs(root)
        return res
    def preorder(self, root: 'Node') -> List[int]:
        # 迭代
        if not root:
            return []
        s = [root]
        res = []
        while s:
            node = s.pop()
            res.append(node.val)
            s.extend(node.children[::-1])
        return res
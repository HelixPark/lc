
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 迭代：借助一个队列
        if root == None:
            return []
        res, queue = [], [root]
        while queue:
            size = len(queue)
            tmp = []
            for _ in range(size):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res

    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        # 递归
        if not root:
            return []
        res = []
        def dfs(index, r):
            if len(res) < index:
                res.append([])
            res[index-1].append(r.val)
            if r.left:
                dfs(index+1, r.left)
            if r.right:
                dfs(index+1, r.right)
        dfs(1,root)
        return res

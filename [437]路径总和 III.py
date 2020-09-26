

class Solution:
    def __init__(self):
        self.res = 0

    def dfs(self, root, sum):
        if not root:
            return

        if sum == root.val:
            self.res += 1
        self.dfs(root.left, sum - root.val)
        self.dfs(root.right, sum - root.val)

    def pathSum(self, root: TreeNode, sum: int) -> int:
        # 先序递归遍历每个节点
        # 以每个节点作为起始节点DFS寻找满足条件的路径
        if not root:
            return self.res
        self.dfs(root,sum)

        self.pathSum(root.left,sum)
        self.pathSum(root.right,sum)
        return self.res


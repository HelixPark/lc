
class Solution:
    def hasPathSum1(self, root: TreeNode, sum: int) -> bool:
        # 方式1：递归DFS
        if not root:
            return False
        # 达到叶子节点，和为sum，则说明存在
        if not root.left and not root.right:
            return sum == root.val

        return self.hasPathSum(root.left, sum - root.val) or \
               self.hasPathSum(root.right, sum - root.val)
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # BFS：使用队列
        if not root:
            return False
        que = collections.deque()
        que.append((root, root.val))
        while que:
            node, path = que.popleft()
            if not node.left and not node.right and path == sum:
                return True
            if node.left:
                que.append((node.left, path + node.left.val))
            if node.right:
                que.append((node.right, path + node.right.val))
        return False
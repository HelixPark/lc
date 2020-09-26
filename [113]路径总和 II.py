
class Solution:
    def pathSum1(self, root: TreeNode, sum: int) -> List[List[int]]:
        # 递归DFS
        if not root:
            return []
        if not root.left and not root.right:
            if root.val == sum:
                return [[sum]]
            else:
                return []

        left = self.pathSum(root.left, sum - root.val)
        right = self.pathSum(root.right, sum - root.val)

        return [[root.val] + ans for ans in left + right]
    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        # BFS
        if not root:
            return []

        stack = [(root, [root.val])]
        res = list()
        while stack:
            node, tmp = stack.pop(0)
            if not node.left and not node.right and sum(tmp) == sum_:
                res.append(tmp)
            if node.left:
                stack.append((node.left, tmp + [node.left.val]))
            if node.right:
                stack.append((node.right, tmp + [node.right.val]))

        return res










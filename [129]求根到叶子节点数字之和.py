# 给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。 
# 
#  例如，从根到叶子节点路径 1->2->3 代表数字 123。 
# 
#  计算从根到叶子节点生成的所有数字之和。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例 1: 
# 
#  输入: [1,2,3]
#     1
#    / \
#   2   3
# 输出: 25
# 解释:
# 从根到叶子节点路径 1->2 代表数字 12.
# 从根到叶子节点路径 1->3 代表数字 13.
# 因此，数字总和 = 12 + 13 = 25. 
# 
#  示例 2: 
# 
#  输入: [4,9,0,5,1]
#     4
#    / \
#   9   0
#  / \
# 5   1
# 输出: 1026
# 解释:
# 从根到叶子节点路径 4->9->5 代表数字 495.
# 从根到叶子节点路径 4->9->1 代表数字 491.
# 从根到叶子节点路径 4->0 代表数字 40.
# 因此，数字总和 = 495 + 491 + 40 = 1026. 
#  Related Topics 树 深度优先搜索 
#  👍 195 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers1(self, root: TreeNode) -> int:
        # 方式1：dfs
        def dfs(root,pathSum):
            if root == None:
                return
            # 进入下一层，位权升级
            pathSum *= 10
            pathSum += root.val
            if root.left == None and root.right == None:
                # 遇到叶子节点，添加到结果中
                self.res += pathSum
                return
            dfs(root.left, pathSum)
            dfs(root.right, pathSum)
        self.res = 0
        dfs(root,0)
        return self.res

    def sumNumbers2(self, root: TreeNode) -> int:
        # 方式2：dfs
        if not root: return 0
        self.sum = 0

        def dfs(node, sum):
            if node.left:
                dfs(node.left, sum + str(node.left.val))
            if node.right:
                dfs(node.right, sum + str(node.right.val))
            if not node.left and not node.right:
                self.sum += int(sum)
        dfs(root, str(root.val))
        return self.sum

    def sumNumbers3(self, root: TreeNode) -> int:
        # 方式3：BFS
        if not root: return 0
        stack = [(root, str(root.val))]
        res = 0
        while stack:
            node, sum = stack.pop(0)
            if node.left:
                stack.append((node.left, sum + str(node.left.val)))
            if node.right:
                stack.append((node.right, sum + str(node.right.val)))
            if not node.left and not node.right:
                res += int(sum)
        return res
    def sumNumbers(self, root: TreeNode) -> int:
        # 方式4：BFS和deque，比三优化了一下
        if not root:
            return 0
        queue = deque()
        queue.append((root, root.val))
        res = 0
        while len(queue) > 0:
            node, curr_val = queue.popleft()
            if node.left:
                # 继续BFS
                queue.append((node.left, curr_val * 10 + node.left.val))
            if node.right:
                # 继续BFS
                queue.append((node.right, curr_val * 10 + node.right.val))
            if not node.left and not node.right:
                # 找到了一个leaf node，累计结果
                res += curr_val
        return res
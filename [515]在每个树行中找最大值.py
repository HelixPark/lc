# 您需要在二叉树的每一行中找到最大的值。 
# 
#  示例： 
# 
#  
# 输入: 
# 
#           1
#          / \
#         3   2
#        / \   \  
#       5   3   9 
# 
# 输出: [1, 3, 9]
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 
#  👍 91 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        # 求树的每层的最大值
        # 方式1：递归dfs
        res = []
        def dfs(root, depth):
            if not root: return
            if len(res) <= depth:
                res.append(float("-inf"))
            res[depth] = max(res[depth], root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 0)
        return res

    def largestValues2(self, root: TreeNode) -> List[int]:
        # 方式2：bfs队列
        if not root: return []
        q,res = collections.deque([root]), []
        while q:
            size = len(q)
            res.append(float("-inf"))
            for i in range(size):
                node = q.popleft()
                res[-1] = max(res[-1], node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return res

    def largestValues3(self, root: TreeNode) -> List[int]:
        # 方法3：迭代
        if not root: return []
        res, cur = [], [root]
        while cur:
            nxt = []
            res.append(float("-inf"))
            for node in cur:
                res[-1] = max(res[-1], node.val)
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
            cur = nxt
        return res
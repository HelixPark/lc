# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。 
# 
#  
# 
#  示例： 
# 二叉树：[3,9,20,null,null,15,7], 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回其层次遍历结果： 
# 
#  [
#   [3],
#   [9,20],
#   [15,7]
# ]
#  
#  Related Topics 树 广度优先搜索 
#  👍 574 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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

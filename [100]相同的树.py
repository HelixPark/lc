# 给定两个二叉树，编写一个函数来检验它们是否相同。 
# 
#  如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。 
# 
#  示例 1: 
# 
#  输入:       1         1
#           / \       / \
#          2   3     2   3
# 
#         [1,2,3],   [1,2,3]
# 
# 输出: true 
# 
#  示例 2: 
# 
#  输入:      1          1
#           /           \
#          2             2
# 
#         [1,2],     [1,null,2]
# 
# 输出: false
#  
# 
#  示例 3: 
# 
#  输入:       1         1
#           / \       / \
#          2   1     1   2
# 
#         [1,2,1],   [1,1,2]
# 
# 输出: false
#  
#  Related Topics 树 深度优先搜索 
#  👍 469 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 两个二叉树相同，当且仅当两个二叉树的结构完全相同，且所有对应节点的值相同。
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 递归DFS：先判断跟，若相同，再判断左右子节点
        # 都为空，相同
        if not p and not q:
            return True
        # 一个空，另一个不空，不同
        if not p or not q:
            return False
        # 根相同，数值不同，也不同
        if p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) \
               and self.isSameTree(p.right, q.right)

    def isSameTree1(self, p: TreeNode, q: TreeNode) -> bool:
        # BFS:使用两个队列分别存储两个二叉树的节点。
        # 初始时将两个二叉树的根节点分别加入两个队列。每次从两个队列各取出一个节点比较
        if not p and not q:
            return True
        if not p or not q:
            return False

        queue1 = collections.deque([p])
        queue2 = collections.deque([q])

        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            # 节点值不同，一定不同
            if node1.val != node2.val:
                return False
            # 再判断两个节点的子节点是否为空
            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right

            if (not left1) ^ (not left2):
                return False
            if (not right1) ^ (not right2):
                return False
            # 结构相同，把子节点加入队列
            if left1:
                queue1.append(left1)
            if right1:
                queue1.append(right1)
            if left2:
                queue2.append(left2)
            if right2:
                queue2.append(right2)
        # 结束时两个队列同时为空，则两个二叉树相同
        return not queue1 and not queue2




# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。 
# 
#  示例: 
# 
#  输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
# 
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 
#  👍 319 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # DFS：是先访问右子树。那么对于每一层来说，
        # 在这层见到的第一个结点一定是最右边的结点。
        # 存储在每个深度访问的第一个结点，知道了树的层数，就可以得到最终的结果数组
        rightmost_value_at_depth = dict()  # 深度为索引，存放节点的值
        max_depth = -1

        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()

            if node is not None:
                # 维护二叉树的最大深度
                max_depth = max(max_depth, depth)

                # 如果不存在对应深度的节点我们才插入
                rightmost_value_at_depth.setdefault(depth, node.val)

                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]

    def rightSideView1(self, root: TreeNode) -> List[int]:
        # BFS：层次遍历，对每一层来说，最右边的节点（最后遍历到的）就是右视图
        rightmost_value_at_depth = dict()  # 深度为索引，存放节点的值
        max_depth = -1

        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()

            if node is not None:
                # 维护二叉树的最大深度
                max_depth = max(max_depth, depth)

                # 由于每一层最后一个访问到的节点才是我们要的答案，因此不断更新对应深度的信息即可
                rightmost_value_at_depth[depth] = node.val

                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))

        return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]
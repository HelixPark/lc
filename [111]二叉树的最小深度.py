

class Solution:
    def minDepth1(self, root: TreeNode) -> int:
        # 非递归解法：BFS
        # 如果某一层的某个节点没有子节点，返回这个节点的层数
        if not root:
            return 0

        q = []  #队列栈
        q.append(root)
        # root本身就是一层
        depth = 1
        while len(q) != 0:
            sz = len(q)
            # 将当前队列中的所有节点向四周扩散
            for i in range(sz):
                # 先弹出左边(低索引)
                curNode = q.pop(0)
                # 判断是否达到终点
                if curNode.left == None and curNode.right == None:
                    return depth
                # 将curNode的相邻节点加入队列
                if curNode.left != None:
                    q.append(curNode.left)
                if curNode.right != None:
                    q.append(curNode.right)
            depth += 1
        return -1


    def minDepth(self, root: TreeNode) -> int:
        # 递归DFS：返回Math.min(左子树的深度，右子树的深度)+1，
        # 但有一个问题，如果左右子树都不为空或者都为空是没问题的。
        # 但如果左右子树一个为空一个不为空，就会有问题了，
        # 因为为空的那个子节点的深度是0，我们不能用它，所以这里要有个判断。
        if root == None:
            return 0
        leftDepth = self.minDepth(root.left)      # 左子树的最小深度
        rigthDepth = self.minDepth(root.right)    # 右子树的最小深度
        # 如果left和right都为0，返回1即可
        # 如果left和right只有一个为0，说明只有一个子结点，只需要返回它另一个子节点的最小深度 + 1
        # 如果left和right都不为0，说明有两个子节点，我们只需要返回最小深度的 + 1
        if leftDepth and rigthDepth:
            return min(leftDepth, rigthDepth) + 1
        else:
            return leftDepth + rigthDepth + 1

class Solution:
    def rob(self, root: TreeNode) -> int:
        
        # 递归思想,python超时
        # 能盗取的最高金额为(抢劫i节点 + 抢劫i节点的左孩子的左右子树 + 抢劫i节点的右孩子的左右子树)
        # 与(抢劫i节点的左子树 + 抢劫i节点的右子树的和) 的最大值

        if root == None:
            return 0

        val = 0
        if root.left != None:
            val = self.rob(root.left.left) + self.rob(root.left.right) + val

        if root.right != None:
            val = self.rob(root.right.left) + self.rob(root.right.right) + val

        return max(self.rob(root.left) + self.rob(root.right), val + root.val)

        # DP思想:树状DP
        # 定义一个数组res, 长度为2,
        # res[0]表示 不抢 该节点可获得最大值, res[1]表示 抢 劫该节点可获得最大值
        # 方法helper(r)意为：在以root为根节点的树中, 返回抢劫根节点与不抢劫根节点可获得的最大值

        # def helper(root):
        #     # root == None, 边界条件，为空时跳出
        #     if not root:
        #         return [0,0]
        #
        #
        #     # root.left不为空,
        #     # 以root.left为root的树，计算抢劫这个root时与不抢劫这个root 可获得的最大金额
        #     # left[0]则为不抢root可获得的最大金额, left[1]则为抢劫root可获得的最大金额
        #     if root.left:
        #         l = helper(root.left)
        #     else:
        #         l = [0, 0]
        #
        #     if root.right:
        #         r = helper(root.right)
        #     else:
        #         r = [0, 0]
        #
        #     res = [0,0]
        #
        #     # 计算不偷这个root时的最大金额（左右树随便抢不抢）
        #     res[0] = max(l[0], l[1]) + max(r[0], r[1])
        #     # 偷这个root，（这个root的左右树不能被抢）
        #     res[1] = root.val + l[0] + r[0]
        #     return res
        #
        #
        # res = helper(root)
        # return max(res)


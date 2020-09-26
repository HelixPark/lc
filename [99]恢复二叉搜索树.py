
class Solution:
    def recoverTree1(self, root: TreeNode) -> None:
        # 中序遍历后排序，交换等
        res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root)
            inorder(root.right)
        inorder(root)

        # 排序，交换
        # 扫面遍历的结果，找出可能存在错误交换的节点x和y
        x, y = None, None
        pre = res[0]
        for i in range(1,len(res)):
            if pre.val > res[i].val:
                y = res[i]
                if not x:
                    x = pre
            pre = res[i]
        # 如果x和y不为空，则交换这两个节点值，恢复二叉搜索树
        if x and y:
            x.val, y.val = y.val, x.val


    def recoverTree2(self, root: TreeNode) -> None:
        # 迭代中序遍历
        stack = []
        x, y, pred = None, None, None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if pred and root.val < pred.val:
                y = root
                if x is None:
                    x = pred
                else:
                    break
            pred = root
            root = root.right
        x.val, y.val = y.val, x.val



    def recoverTree(self, root: TreeNode) -> None:
        def dfs(root):
            if root is None:
                return

            nonlocal x, y, pred
            dfs(root.left)
            if pred and root.val < pred.val:
                y = root
                if x is None:
                    x = pred
                else:
                    return
            pred = root
            dfs(root.right)

        x, y, pred = None, None, None
        dfs(root)
        x.val, y.val = y.val, x.val


        


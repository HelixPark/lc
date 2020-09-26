

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None

        # 后续遍历最后一个就是根节点
        root = TreeNode(postorder[-1])

        # 在中序遍历中找到root的索引，左边的左子树，右边的是右子树
        root_index = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])

        root.right = self.buildTree(inorder[root_index+1:], postorder[root_index:-1])

        return root
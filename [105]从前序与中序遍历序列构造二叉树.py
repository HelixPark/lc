
from typing import List
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def buildTree1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 官方的比较麻烦：使用了hash，耗时短
        def myBuildTree(pre_left:int, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None

            # 前序遍历中的第一个节点就是根节点
            pre_root = pre_left
            # 在中序遍历中定位根节点de 索引
            in_root = indexDict[preorder[pre_root]]

            # 先吧根节点建立起来
            root = TreeNode(preorder[pre_root])
            # 得到左子树中节点数组
            size_left_subtree = in_root - in_left
            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就
            # 对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = myBuildTree(pre_left + 1, pre_left + size_left_subtree,
                                     in_left, in_root - 1)

            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就
            # 对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(pre_left + size_left_subtree + 1, pre_right,
                                     in_root + 1, in_right)
            return root


        n = len(preorder)
        # 中序构造哈希映射，帮助我们快速定位根节点,健值存的索引
        indexDict = {element:i for i, element in enumerate(inorder)}

        return myBuildTree(0, n-1, 0, n-1)



    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 简洁，耗时长
        if len(inorder) == 0:
            return None

        # 前序遍历的第一个值为根节点
        root = TreeNode(preorder[0])

        # 因为没有重复的元素，直接根据值查找根节点在中序遍历中的位置索引，：找根
        root_index = inorder.index(preorder[0])

        # 构建左子树，
        root.left = self.buildTree(preorder[1:root_index+1], inorder[:root_index])
        # 构建右子树
        root.right = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])

        return root
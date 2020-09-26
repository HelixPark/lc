# 手动创建二叉树

# 先建立二叉树的节点，有一个data数据域，left，right 两个指针域
# 在建立树：主要是根，把节点相连
# 把建立好的节点和根链接起来

# encoding:utf-8
# 建立节点
class TreeNode(object):
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# 建立根
class BTree(object):
    def __init__(self, root = None):
        self.root = root

# 节点和根相连(手动）
node1 = TreeNode(value=1)
node2 = TreeNode(2,node1,None)  #node1为node2的左孩子，右孩子为None
node3 = TreeNode(value=3)
node4 = TreeNode(value=4)
node5 = TreeNode(5, node3, node4)   #node3、node4为node5的左右孩子
node6 = TreeNode(6,node2,node5)
node7 = TreeNode(7,node6,None)
node8 = TreeNode(value=8)
root = TreeNode('root',node7,node8)

bt = BTree(root)

# 打印二叉树
# print(bt)

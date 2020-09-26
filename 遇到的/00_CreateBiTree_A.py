# 自动创建二叉树

# 节点
class TreeNode():
    def __init__(self,value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
# 手动创建
class BTree():
    def __init__(self,root = None):
        self.root = root

    def is_empty(self):
        return self.root == None

    def create(self):
        tmp = input('enter a value:')

        if tmp is '#':
            return None

        new_node = TreeNode(value = tmp)

        if self.root is None:
            self.root = new_node

        new_node.left = self.create()
        new_node.right = self.create()

    # 先序遍历
    def preOrder(self, node):
        if node is not None:
            print(node.value, end=' ')
            self.preOrder(node.left)
            self.preOrder(node.right)

    # 中序遍历
    def inOrder(self, node):
        if node is not None:
            self.inOrder(node.left)
            print(node.value, end=' ')
            self.inOrder(node.right)

    # 后序遍历
    def postOrder(self, node):
        if node is not None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.value, end=' ')

    def printALL(self, node):
        print("先序遍历: ", end="->")
        self.preOrder(node)
        print('\n')
        print("中序遍历: ", end="->")
        self.inOrder(node)
        print('\n')
        print("后序遍历: ", end="->")
        self.postOrder(node)
        print('\n')

# 自动创建二叉树
class BTree2():
    def __init__(self,data_list,root = None):
        # 初始化传入列表的迭代器
        self.data_list = iter(data_list)
        self.root = root

    def create(self):

        # 步进获取下一个元素
        next_data = next(self.data_list)

        # 如果为#，则为None
        if next_data is '#':
            return None

        new_node = TreeNode(next_data)

        if self.root is None:
            self.root = new_node

        new_node.left = self.create()
        new_node.right = self.create()

        return new_node

    # 先序遍历
    def preOrder(self,node):
        if node is not None:
            print(node.value, end=' ')
            self.preOrder(node.left)
            self.preOrder(node.right)
    # 中序遍历
    def inOrder(self,node):
        if node is not None:
            self.inOrder(node.left)
            print(node.value, end=' ')
            self.inOrder(node.right)
    # 后序遍历
    def postOrder(self,node):
        if node is not None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.value, end=' ')

    def printALL(self,node):
        print("先序遍历: ", end="->")
        self.preOrder(node)
        print('\n')
        print("中序遍历: ", end="->")
        self.inOrder(node)
        print('\n')
        print("后序遍历: ", end="->")
        self.postOrder(node)
        print('\n')

def f1():
    bt = BTree()
    root = bt.create()
    bt.printALL(root)
    # 方式1
    # bt = BTree()
    # bt.create()
    # 按先序遍历一个个输入数(带#)，得出二叉树，和M.py的树一样
    # enter a value:9
    # enter a value:7
    # enter a value:6
    # enter a value:2
    # enter a value:1
    # enter a value:'#'
    # enter a value:'#'
    # enter a value:'#'
    # enter a value:5
    # enter a value:3
    # enter a value:'#'
    # enter a value:'#'
    # enter a value:4
    # enter a value:'#'
    # enter a value:'#'
    # enter a value:'#'
    # enter a value:8
    # enter a value:'#'
    # enter a value:'#'
    # 生成的二叉树
    # ------------------------
    #          root
    #       7        8
    #     6
    #   2   5
    # 1    3 4
    #
    # -------------------------


def f2():

    # 方式2：按先序遍历（带#）输入一串数据自动建树
    # 还有一个一整行输入好；自动建树
    # 97621###53##4###8###
    # abd#g###ce##fh###

    # data = 'abd#g###ce##fh###'
    data = '97621###53##4###8###'
    # data = input("Please input the node value: ")

    data_list = list(data)
    bt = BTree2(data_list)
    root = bt.create()
    bt.printALL(root)

if __name__ == '__main__':
    f2()
    # f1()




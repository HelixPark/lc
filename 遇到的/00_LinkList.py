nums = [1,2,3,4,5,6]
# encoding = 'utf-8'
# 首先创建一个结点类
class LinkNode:
    def __init__(self,value):
        self.value = value
        self.next = None

# 然后创建一个单链表的类
class SingleLinkList:
    def __init__(self):
        # 这里头结点和第一个节点是同一个指向
        self.head = None

    # 判断链表是否为空
    def isEmpty(self):
        return self.head is None

    # 获取单链表长度
    def length(self):
        cur = self.head
        count = 0

        while cur is not None:
            count += 1
            cur = cur.next
        return count

    # 在链表的头部添加元素
    def addHead(self,data):
        # 创建一个新节点
        newNode = LinkNode(data)

        newNode.next = self.head
        self.head = newNode

    # 在链表的尾部添加元素
    # 考虑两种情况：链表为空、链表不为空
    # 当链表为空的时候，我们只能将这个新结点插入到头结点的位置
    # 当链表不为空的时候，我们就需要将指针移动到链表的最后，
    # 然后将新结点插入到最后那一个结点的下一个位置，也就是添加到最后。
    def addRear(self,data):
        newNode = LinkNode(data)

        # head为空，就直接插入
        if self.isEmpty():
            self.head = newNode
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next   #cur停留在最后一个node

            cur.next = newNode   #新节点直接加后面

    # 在链表的指定位置添加元素:四种情况
    # 出错情况（索引小于0或大于总长度）、插入到头部的情况（index为0）
    # 、插入到尾部的情况（index为length）、插入到中间的情况
    def insertNode(self,index,data):
        # 先创建一个新节点
            # 出错情况
        if index < 0 or index > self.length():
            return False
            # 头部情况
        elif index == 0:
            self.addHead(data)
            # 尾部情况
        elif index == self.length():
            self.addRear(data)
            # 中间情况
        else:
            cur = self.head
            count = 1
            while count < index - 1:
                cur = cur.next
                count += 1

            newNode = LinkNode(data)
            # 插入
            newNode.next = cur.next
            cur.next = newNode

    # 查找指定结点是否存在
    def isExist(self,data):
        cur = self.head
        while cur is not None:
            if cur.data == data:
                return True
            else:
                cur = cur.next
        return False

    # 遍历整个链表
    def travel(self):
        cur = self.head
        while cur:
            print(cur.value)
            cur = cur.next

    # 单链表逆序1：就地逆序
    # 在遍历链表的时候，修改当前节点指针域的指向，使其指向他的前驱节点，
    # 这就需要三个指针变量保存结点指针域：当前结点、前驱结点和后继结点
    # 只需要对链表进行一次遍历，因此时间复杂度为O(N)，N为链表的长度。
    # 此种方法需要两个额外的变量储存前驱结点和后继结点，所以它的空间复杂度为O(1)。
    def reverse1(self):
        if self.head == None or self.head.next == None:
            return

        cur = self.head  #当前节点
        nxt = self.head.next  #后继节点
        pre = cur # 前驱节点

        cur.next = None
        cur = nxt
        while cur.next != None:
            # pre, cur, nxt依次
            nxt = cur.next   # 保留下一个节点
            cur.next = pre    #pre节点挂在cur后
            # 依次后移
            pre = cur  #因为指向已经反了，不能用next
            cur = nxt
        # 最后一个进不了循环，在外面整
        cur.next = pre
        self.head = cur

    # 单链表逆序1：插入法逆序
    # 从链表的第二个结点开始，把遍历到的结点插入到头结点的后面，直到遍历结束。
    def reverse2(self):
        if self.head == None or self.head.next == None:
            return

        cur = self.head.next  #cur指向head节点
        self.head = None  #切换head(1)到2的指向


        while cur != None:
            nxt = cur.next
            cur.next = self.head.next
            self.head.next = cur
            cur = nxt







    # 1 2 3 4 5 6 变成1 6 2 5 3 4
    # 单链表逆序：
    def rechange(self):
        print()




linklist = SingleLinkList()
print(linklist.isEmpty())
linklist.addHead(3)
linklist.addHead(2)
linklist.addHead(1)
linklist.addRear(4)
linklist.addRear(5)
linklist.addRear(6)
# linklist.insertNode(3,7)
# linklist.insertNode(0,8)
# linklist.insertNode(8,9)
linklist.travel()
print('ss')
linklist.reverse2()
linklist.travel()

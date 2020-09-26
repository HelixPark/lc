
#   python，两个栈，入队列的时候就append，
#   索引0为栈顶
#   弹出队首元素时，将栈1的元素逐一弹出并压入栈2，(此时1和2中的顺序相反)
#   再将栈2栈尾元素弹出，然后再将该栈2中元素逐一弹出放回原来的栈1
#   即在原栈1的0位置删除了
class CQueue:
    # 维护两个栈，第一个栈支持插入操作，第二个栈支持删除操作
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def appendTail(self, value: int) -> None:
        self.s1.append(value)


    def deleteHead(self) -> int:
        if len(self.s1) == 0:
            return -1
        # 把s1的倒腾到s2中
        while self.s1:
            self.s2.append(self.s1.pop())
        # 弹出最顶端的res
        res = self.s2.pop()
        # 再把s2恢复到s1中
        while self.s2:
            self.s1.append(self.s2.pop())
        return res
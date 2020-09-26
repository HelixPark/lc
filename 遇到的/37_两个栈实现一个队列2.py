# -*- coding:utf-8 -*-

class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    # LC232

    def push(self, x: int) -> None:
        # 入队直接入
        self.s1.append(x)

    # 从队列首部移除元素
    def pop(self) -> int:
        # 出队先检查s2是否为空。若为空则先清空，再把s1倒腾到s2
        while len(self.s2) != 0:
            self.s2.pop()
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())
        # 此时s2的栈顶就是res
        res = self.s2.pop()
        # 再把s2倒腾回s1
        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())
        return res

    # 返回队列首部元素，不移除
    def peek(self) -> int:
        # 出队先检查s2是否为空。若为空则先清空，再把s1倒腾到s2
        while len(self.s2) != 0:
            self.s2.pop()
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())
        # 此时s2的栈顶就是res
        res = self.s2.pop()
        self.s2.append(res)
        # 再把s2倒腾回s1
        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())
        return res

    def empty(self) -> bool:
        if len(self.s1) > 0:
            return False
        else:
            return True
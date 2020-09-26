# -*- coding:utf-8 -*-
class MyStack:
    # 双队列实现，LC225
    # 单队列：反转前n-1个元素(依次添加到n后面.q.append(q.pop(0)))，栈顶元素始终保留在队首
    def __init__(self):
        self.d1 = []
        self.d2 = []

    def push(self, x: int) -> None:
        self.d1.append(x)

    def pop(self) -> int:
        # 先把2清空
        while len(self.d2) != 0:
            self.d2.pop()
        # 将1转移到2
        while len(self.d1) > 1:
            self.d2.append(self.d1.pop(0))
            # self.d2.append(self.d1.popleft())
        # 最后一个d1的就是res
        res = self.d1.pop(0)
        while len(self.d2) > 0:
            self.d1.append(self.d2.pop(0))
        return res

    def top(self) -> int:
        # 先把2清空
        while len(self.d2) != 0:
            self.d2.pop()
        # 将1转移到2
        while len(self.d1) > 1:
            self.d2.append(self.d1.pop(0))
            # self.d2.append(self.d1.popleft())
        # 最后一个d1的就是res
        res = self.d1.pop(0)
        self.d2.append(res)
        while len(self.d2) > 0:
            self.d1.append(self.d2.pop(0))
        return res

    def empty(self) -> bool:
        if len(self.d1) > 0:
            return False
        else:
            return True
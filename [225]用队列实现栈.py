# 使用队列实现栈的下列操作： 
# 
#  
#  push(x) -- 元素 x 入栈 
#  pop() -- 移除栈顶元素 
#  top() -- 获取栈顶元素 
#  empty() -- 返回栈是否为空 
#  
# 
#  注意: 
# 
#  
#  你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合
# 法的。 
#  你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。 
#  你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。 
#  
#  Related Topics 栈 设计 
#  👍 219 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class MyStack:
    # 双队列实现，
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



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# leetcode submit region end(Prohibit modification and deletion)

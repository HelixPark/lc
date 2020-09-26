# 使用栈实现队列的下列操作： 
# 
#  
#  push(x) -- 将一个元素放入队列的尾部。 
#  pop() -- 从队列首部移除元素。 
#  peek() -- 返回队列首部的元素。 
#  empty() -- 返回队列是否为空。 
#  
# 
#  
# 
#  示例: 
# 
#  MyQueue queue = new MyQueue();
# 
# queue.push(1);
# queue.push(2);  
# queue.peek();  // 返回 1
# queue.pop();   // 返回 1
# queue.empty(); // 返回 false 
# 
#  
# 
#  说明: 
# 
#  
#  你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
#  
#  你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。 
#  假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。 
#  
#  Related Topics 栈 设计 
#  👍 222 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []


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



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# leetcode submit region end(Prohibit modification and deletion)

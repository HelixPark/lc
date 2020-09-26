class DLinkedNode:
    def __init__(self,key=0,value =0):
        self.key = key
        self.value = value
        # 双向链表
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果key存在，先通过hash定位，再已到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 若不存在，创造一个节点，添加到hash表
            node = DLinkedNode(key,value)
            self.cache[key] = node
            # 添加到头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 超出容量，删除尾部，
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果key存在，hash定位，再修改value，移动到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node




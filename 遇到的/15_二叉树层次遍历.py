def levelOrder(root):
    res, queue = [], [root]
    while queue:
        size, tmp = len(queue), []
        for i in range(size):
            node = queue.pop(0)
            tmp.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(tmp)
    res.reverse()

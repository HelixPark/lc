

def zuijin(root, p, q):
    if not root or root == p or root == q:
        return root

    left = zuijin(root.left, p, q)
    right = zuijin(root.right, p, q)

    if not left:
        return right
    if not right:
        return left
    return root
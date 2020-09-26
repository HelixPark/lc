
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # 方式1：递归:要么相同，要么是左或者右子树相同
        # 判断st相等，三个条件and：根节点相等，s的左和t的左相等，s的右和t的右相等
        # 判断t是s的子树，三个条件or：s和t相等，or t是s的左子树，or t是s的右子树
        if s == None and t == None:
            return True

        if s == None or t == None:
            return False

        return self.isSameTree(s,t) \
               or self.isSubtree(s.left,t) \
               or self.isSubtree(s.right,t)

    def isSameTree(self,s,t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val \
            and self.isSameTree(s.left, t.left) \
            and self.isSameTree(s.right, t.right)

    def isSubtree1(self, s: TreeNode, t: TreeNode) -> bool:
        # 暴力法：遇到s的每个节点，先认为是否为t的根，o(s *t)
        def check(cur, t):
            if not cur and not t:return True
            if not cur or not t:return False
            if cur.val != t.val:return False
            return check(cur.left, t.left) and check(cur.right, t.right)
        def dfs(s, t):
            if not s:return False
            return check(s,t) or dfs(s.left,t) or dfs(s.right,t)
        return dfs(s,t)
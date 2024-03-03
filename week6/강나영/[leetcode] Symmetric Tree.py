# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        q = deque([(root.left, root.right)])
        while q:
            l, r = q.popleft()
            if l and r and l.val == r.val:
                q.extend([(l.right, r.left), (l.left, r.right)])
            elif l == r:
                continue
            else:
                return False
        return True
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        tmpl = root.left
        tmpr = root.right
        root.left = NULL






node0 = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(5)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(6)
node0.left = node1
node0.right = node2
node1.left = node3
node1.right = node4
node2.right = node5

S = Solution()
S.flatten(node0)

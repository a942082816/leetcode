# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        def doBST(node):
            if not node:
                return None
            if node.val < L:
                return doBST(node.right)
            elif node.val > R:
                return doBST(node.left)
            else:
                tempNode = TreeNode(node.val)
                tempNode.left = doBST(node.left)
                tempNode.right = doBST(node.right)
                return tempNode
        return doBST(root)
    

S =Solution()

node1 = TreeNode(1)
node2 = TreeNode(0)
node3 = TreeNode(2)

node1.left = node2
node1.right = node3

ret = S.trimBST(node1, 1, 2)
print(S.trimBST(node1, 1, 2))


import bisect# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        dictA = {}
        for i, v in enumerate(inorder):
            dictA[v] = i

        def buildSubTree(preorder, inorder):

            if not preorder:
                return None
            node = TreeNode(preorder[0])
            if len(preorder) == 1:
                return node
            else:
                leftCount = dictA[node.val] - dictA[inorder[0]]
                node.left = buildSubTree(preorder[1:  1 + leftCount], inorder[:leftCount])
                node.right = buildSubTree(preorder[leftCount+1:], inorder[leftCount+1:])
            return node
        retNode = buildSubTree(preorder, inorder)
        return retNode

S = Solution()
#a1 = [5,4,1,2,3]
#a2 = [1,2,3,4,5]
a1 = [3,9,20,15,7]
a2 = [9,3,15,20,7]
node = S.buildTree(a1, a2)
print(node.val)
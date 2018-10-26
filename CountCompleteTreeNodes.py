class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        count1 = 0
        count2 = 0
        letfNode = root.left
        rightNode = root.right
        while letfNode:
            count1 += 1
            letfNode = letfNode.left
        while rightNode:
            count2 += 1
            rightNode = rightNode.right
        if count1 == count2:
            return pow(2, count1+1) - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) +1

S = Solution()
node =TreeNode(1);
ret = S.countNodes(node)
print(ret)

        

        
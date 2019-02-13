# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict
#DFS
class Solution:
    def hasPathSum(self, root: 'TreeNode', sum: 'int') -> 'bool':
        if not root:
            return False
        stack = []
        mapNodeSum = defaultdict(int)
        mapFather = {}
        mapFather[root] = None
        stack.append(root)
        while stack:
            node = stack[-1]
            stack.pop()
            mapNodeSum[node] = mapNodeSum[mapFather[node]] + node.val
            if node.left:
                stack.append(node.left)
                mapFather[node.left] = node
            if node.right:
                stack.append(node.right)
                mapFather[node.right] = node

            if not node.left and not node.right:
                if mapNodeSum[node] == sum:
                    return True
        return False
            
        
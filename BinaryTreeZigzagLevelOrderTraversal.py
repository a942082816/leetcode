class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import queue
class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = queue.Queue()
        q.put((root, 1))
        retList = []
        while not q.empty():
            node = q.get()
            if not node[0]:
                continue
            q.put((node[0].left, node[1]+1))
            q.put((node[0].right, node[1]+1))
            if len(retList) < node[1]:
                retList.append([])
            retList[node[1]-1].append(node[0].val)
        for i,v in enumerate(retList):
            if i % 2 != 0:
                v.reverse()
        return retList


S = Solution()
node = TreeNode(3)
node1 = TreeNode(9)
node2 = TreeNode(20)
node3 = TreeNode(15)
node4 = TreeNode(7)

node.left = node1
node.right = node2
node2.left = node3
node2.right = node4
print(S.zigzagLevelOrder(node))






        
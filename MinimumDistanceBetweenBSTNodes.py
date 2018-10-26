import queue
class Solution:
    def maxOfTree(self,root):
        if not root:
            return -999999
        temp = root
        while temp.right:
            temp =temp.right
        return temp.val
    def minOfTree(self, root):
        if not root:
            return 999999
        temp = root
        while temp.left:
            temp = temp.left
        return temp.val
    def minDiffInBST1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = queue.Queue()
        q.put(root)
        minN = 999999
        while not q.empty():
            node = q.get()
            temp = min((node.val - self.maxOfTree(node.left)),(self.minOfTree(node.right)- node.val))
            print(temp)
            if temp < minN:
                minN = temp
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        return minN

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        listA = []

        def midOrder(root):
            if not root:
                return
            midOrder(root.left)
            listA.append(root.val)
            midOrder(root.right)
        
        midOrder(root)
        minN = listA[1] - listA[0]
        for i in range(2, len(listA)):
            temp = listA[i] -listA[i-1]
            if temp < minN:
                minN = temp
        return minN



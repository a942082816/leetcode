#要求O(n), 穷举法pass, 由于是亦或, max的组合应为一个大值一个小值(无思路)
#disscuss 使用前缀树, 二进制只有两位,可以构建前缀树, 构建树的时间复杂度为O(32n) 查找复杂度为O(32n)

class Node:
    def __init__(self, num , i=-1):
        self.left = None # 0
        self.right = None # 1
        self.value = num
        self.index = i


class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 构造前缀树
        root = Node(0)
        for i, n in enumerate(nums):
            tempNode = root
            for j in range(31, -1 , -1):
                temp = n & (1 << j)
                new = Node(temp)
                if j == 0:
                    new.index = i
                if temp == 0:
                    if not tempNode.left:
                        tempNode.left = new
                    tempNode = tempNode.left
                else:
                    if not tempNode.right:
                        tempNode.right = new
                    tempNode = tempNode.right
        # 挨个找最大值
        maxNum = 0
        level = -1
        for i, n in enumerate(nums):
            tempNode = root
            for j in range(31, -1, -1):
                temp = n & (1 << j)
                if temp == 0: # 如果当前位为0  那么要想达到最大值, 应该找同一level 有右子树的节点,类似于贪心
                    if tempNode.right:
                        tempNode = tempNode.right
                    else:
                        tempNode = tempNode.left
                else:
                    if tempNode.left:
                        tempNode = tempNode.left
                    else:
                        tempNode = tempNode.right
                if j == 0:
                    if maxNum < (n ^ nums[tempNode.index]):
                        maxNum = n ^ nums[tempNode.index]
        return maxNum

S = Solution()
maxN = S.findMaximumXOR([3, 10, 5, 25, 2, 8])
print(maxN)
                    
                    
                    
                

                





        
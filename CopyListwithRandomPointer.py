# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        temp = head
        dictA = {}
        listA = []
        index = 0
        while temp:
            listA.append(RandomListNode(temp.label))
            dictA[temp] = index
            temp = temp.next
            index += 1
        temp1 = head
        listB = []
        while temp1:
            if not temp1.random:
                listB.append(None)
            else:
                listB.append(dictA[temp1.random])
            temp1 = temp1.next

        for i in range(len(listA)):
            if i == len(listA) - 1:
                listA[i].next = None
            else:
                listA[i].next = listA[i+1]
            if not listB[i]:
                listA[i].random =None
            else:
                listA[i].random = listA[listB[i]]
        headT = listA[0]
        return headT




a1 =RandomListNode(-1)
a2 =RandomListNode(-2)

a1.next = a2
a1.random = a1

a2.next=None
a2.random =None

S = Solution()
p = S.copyRandomList(a1)
print(p.label)
print(p.random.label)
            

class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict1 = {}
        for i in range(len(list1)):
            dict1[list1[i]] = i
        index = 0
        temp = 10000
        listB = []
        for i in range(len(list2)):
            if temp < 10000 and i > temp+len(list1):
                break
            if list2[i] in dict1:
                sumN = i + dict1[list2[i]]
                if sumN  < temp:
                    listB = []
                    temp = sumN
                    listB.append(list2[i])
                elif sumN == temp:
                    listB.append(list2[i])    
        return listB 

S = Solution()
l1 = ["vacag","KFC"]
l2 = ["fvo","xrljq","jrl","KFC"]
print(S.findRestaurant(l1,l2))



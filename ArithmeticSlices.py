class Solution:
    def getNum(self,n):
        if n < 2:
            return 0
        if n == 2:
            return 1
        return int(n*(n-1)/2) 
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        listB = []
        for i in range(1,len(A)):
            listB.append(A[i] - A[i-1])

        temp = listB[0]
        num = 1
        allNum = 0

        for i in range(1, len(listB)):
            if listB[i] == temp:
                num += 1
            else:
                allNum += self.getNum(num)
                temp = listB[i]
                num = 1
            if i == len(listB) -1 :
                allNum += self.getNum(num)
        return allNum

S = Solution()
a = [1,2,3,4,5,6]
print(S.numberOfArithmeticSlices(a))
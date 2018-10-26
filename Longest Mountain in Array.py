class Solution:
    def longestMountain(self, A):
        length = 0
        listF = [0] * len(A)
        for i in range(1,len(A)-1):
            if A[i] > A[i - 1]:
                length += 1
            else:
                length = 0
            listF[i] = length
        length = 0
        listB = [0] * len(A)
        B = A[::-1]
        for i in range(1,len(B)-1):
            if B[i] > B[i - 1]:
                length += 1
            else:
                length = 0
            listB[i] = length
        listB.reverse()
        ret = 0
        for i in range(1,len(A)):
            if listB[i] > 0 and listF[i] >0:
                temp = listB[i] +listF[i] + 1
                if temp > ret:
                    ret = temp
        return ret




        
    def longestMountain1(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        up = 0
        length = 0
        ret = 0
        upFlag = False
        A.append(A[-1])
        for i in range(len(A) - 1):
            if A[i+1] > A[i]:
                if up == 1:
                    length += 1
                    continue
                if up == -1:
                    if length > ret:
                        ret = length
                    length = 1
                    up = 1
                if up == 0:
                    up = 1
                    length = 1
                upFlag = True
            elif A[i+1] < A[i]:
                if up == 1:
                    length += 1
                    up = -1
                    continue
                if up == -1:
                    length += 1
                if up == 0:
                    up = -1
                    length = 0
            else:
                if not upFlag:
                    length = 0
                if up == -1:
                    if length > ret:
                        ret = length
                    length = 0
                    up = 0
                if up == 1:
                    length += 1
                upFlag = False
        return ret

S = Solution()
print(S.longestMountain([2,3,3,3,3,3,2]))


                

        
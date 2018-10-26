import bisect
class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A.sort()
        retList = []
        for n in B:
            index = bisect.bisect_right(A, n)
            if index == len(A):
                retList.append(A[0])
                del A[0]
            else:
                retList.append(A[index])
                del A[index]
        return retList

S = Solution()
print(S.advantageCount([12,24,8,32],[12,25,32,11]))


        
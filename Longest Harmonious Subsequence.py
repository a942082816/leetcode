from collections import defaultdict 
class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dictA = defaultdict(int)
        for v in nums:
            dictA[v] += 1
        it = dictA.items()
        it = sorted(it, key=lambda x: x[0])
        maxret = 0
        for i in range(len(it)-1):
            if it[i+1][0] - it[i][0] == 1:
                s = it[i+1][1] + it[i][1]
                if s > maxret:
                    maxret = s

        return maxret


    
        


S = Solution()
print(S.findLHS([1,3,2,2,5,2,3,7]))
        
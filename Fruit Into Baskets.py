class Solution(object):
    def totalFruit1(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        maxNum = 0
        numA = 0
        numB = 0
        a = -1
        b = -1
        lastA = 0
        lastB = 0
        for i, v in enumerate(tree):
            if a == v:
                numA += 1
                if tree[i - 1] == v:
                    lastA += 1
                else:
                    lastA = 1
                continue
            if b == v:
                numB += 1
                if tree[i - 1] == v:
                    lastB += 1
                else:
                    lastB = 1
                continue
            if a == -1:
                a = v
                numA += 1
                lastA += 1
                continue
            if b == -1:
                b = v
                numB += 1
                lastB += 1
                continue
            if v != a and v != b:
                if numA + numB > maxNum:
                    maxNum = numA + numB
                if tree[i - 1] == a:
                    numA = lastA
                else:
                    numA = lastB
                    a = b
                lastA = 0
                lastB = 1
                b = v
                numB = 1

        if numA + numB > maxNum:
            return numA + numB
        else:
            return maxNum

    def totalFruit(self, tree):
        prev, curr, res = [None, 0], [None, 0], 0
        for t in tree:
            if t == curr[0]:
                curr[1] += 1
            else:
                prev, curr = curr, prev
                if t == curr[0]:
                    prev[1] += curr[1]
                else:
                    res = max(res, prev[1] + curr[1])
                curr = [t, 1]
        return max(res, prev[1] + curr[1])
        
                
S = Solution()
print(S.totalFruit([6,2,1,1,3,6,6]))
        
        

        
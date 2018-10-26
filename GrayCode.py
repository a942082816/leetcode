import copy
class Solution:
    def product(self, n):
        if n == 1:
            return [[0],[1]]
        else:
            l = self.product(n-1)
            l.extend(copy.deepcopy(l[::-1]))
            for i in range(1, (1<<(n-1))+1):
                l[i-1].append(0)
                l[(1<<(n-1))+i-1].append(1)
            return l
                
    def grayCode1(self, n):
        if n == 0:
            return [0]
        listA = self.product(n)
        listB = []
        for v in listA:
            num = 0
            for i in range(len(v)):
                num += v[i]*(1<<i)
            listB.append(num)
        return listB

    def grayCode(self, n):
        seq = [0]
        for i in range(1, n+1):
            rseq = seq[::-1]
            for num in rseq:
                seq.append(num +(1<<(i-1)))
        return seq
                



        return listA
        """
        :type n: int
        :rtype: List[int]
        """
S = Solution()
a = S.grayCode(3)
print(a)
#思路: 1.遍历 许多无畏的判断
class Solution:
    # 类似于筛法 时间复杂度O(n) timelimit 
    def nthMagicalNumberOld(self, N, A, B): 
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        if A == B :
            return N * A % 1000000007
        if A % B == 0:
            return N * B % 1000000007
        if B % A == 0:
            return N * A % 1000000007
        numA = A
        numB = B
        count = 1
        while count < N:
            if numA < numB:
                numA += A
            elif numB < numA:
                numB += B
            else:
                numA += A
                numB += B
            count += 1
        return min(numA, numB) % 1000000007
    # 先用辗转相除求出最大公约数, 计算量减小为 N % lcm(A,B) AC 60ms
    def nthMagicalNumberOld1(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: in
        """
        
        def gcd(a, b):
            if a < b:
                a, b = b, a
            while b != 0:
                temp = a % b
                a = b
                b = temp
            return a

        def lcm(x, y):
            return x * y / gcd(x, y) 

        num = int(lcm(A, B))
        numA = num//A
        numB = num//B
        ret = num * (N // (numA + numB - 1))
        last = N % (numA + numB -1)
        count = 0
        nA = 0
        nB = 0
        while count < last:
            if nA < nB:
                nA += A
            elif nB < nA:
                nB += B
            else:
                nA += A
                nB += B
            count += 1
        return (min(nA, nB) + ret) % 1000000007
    # discuss 二分法, 复杂度O(log(n)) /O(n)  32ms
    def nthMagicalNumber(self, N, A, B):
        a, b = A, B
        while b: 
            a, b = b, a % b
        l, r, lcm = 2, 10**14, A * B / a
        while l < r:
            m = (l + r) // 2
            if m // A + m // B - m // lcm < N: 
                l = m + 1
            else: 
                r = m
        return l % (10**9 + 7)       

S = Solution()
ret = S.nthMagicalNumber(4,2,3)
print(ret)

    

        

from collections import defaultdict
class Solution1:
    def reorderedPowerOf2(self, N):
        n = 1
        listA = []
        while n < 10e9:
            t = n
            dictNum = defaultdict(int)
            while t > 0:
                number = t % 10
                dictNum[number] += 1
                t //= 10
            listA.append(dictNum)
            n = n << 1
        listN =[]
        while N > 0:
            number = N % 10
            listN.append(number)
            N //= 10
        for l in listA:
            flag = True
            for n in listN:
                if l[n] == 0:
                    flag = False
                    break
                l[n] -= 1
            if not flag:
                continue
            for i in range(10):
                if l[i] != 0:
                    flag = False
                    break
            if flag:
                return True
        return False


class Solution:
    def reorderedPowerOf2(self, N):
        n = 1
        listA = []
        while n < 10e9:
            t = n
            listB = []
            while t > 0:
                number = t % 10
                listB.append(number)
                t //= 10
            listB.sort()
            listA.append(listB)
            n = n << 1
        listN =[]
        while N > 0:
            number = N % 10
            listN.append(number)
            N //= 10
        listN.sort()
        for l in listA:
            if listN == l:
                return True
        return False
            
S = Solution()
print(S.reorderedPowerOf2(46))
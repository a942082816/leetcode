class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        maxN = 0
        count = 0
        listA = [] #(max,index) 储存之前碰到过的最大值和对应的index(从最右边开始)
        listB = []
        index = 0
        while num > 0:
            n = num % 10
            if n > maxN:
                maxN = n
                index = count
                listA.append((maxN, index))
            elif n == maxN:
                listA.append((maxN, count))
            else:
                listA.append((maxN, index))
            listB.append(n)
            list
            count += 1
            num //= 10
        print(listA)
        ret = 0
        for i, v in enumerate(listA[::-1]):
            if v[1] != len(listA)-i-1:
                temp = listB[-i-1]
                listB[-i-1] = v[0]
                listB[v[1]] = temp
                break
        for i,v in enumerate(listB):
            ret += v * pow(10,i)
        return ret

                


S = Solution()
print(S.maximumSwap(1993))
1993
98368
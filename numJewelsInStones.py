class Solution:
    def numJewelsInStones(self, J, S):
        mapHis = {}
        sum = 0
        if len(J)>len(S):
            for s in S:
                if s in mapHis:
                    sum += mapHis[s]
                    continue
                mapHis[s] = 0
                for j in J:
                    if s == j:
                        mapHis[s] +=1
                        sum +=1
        else:
            for j in J:
                if j in mapHis:
                    sum += mapHis[s]
                    continue
                mapHis[j] = 0
                for s in S:
                    if j == s:
                        mapHis[j]+=1
                        sum+=1
        return su   m


s = Solution()
a ='abcd'
b = 'ccc'
print(s.numJewelsInStones(a,b))
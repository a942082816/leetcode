from collections import defaultdict


class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 1:
            return len(s)
        if len(s) == 1:
            return 0
        dictA = defaultdict(int)
        dictB = {}
        listA = []
        for i,c in enumerate(s):
            dictA [c] += 1
            if c not in dictB:
                dictB[c] = []
                dictB[c].append(i)
            else:
                dictB[c].append(i)
        for key in dictA:
            if dictA[key] < k:
                listA.extend(dictB[key])
        listA.append(len(s))
        listA = list(set(listA))
        listA.sort()
        if listA[0] != 0:
            listA.insert(0,0)
        else:
            listA[0] = 1
        if len(listA) == 2 and listA[0] == 0:
            return len(s) 
        maxA = 0
        for i in range(1,len(listA)):
            if listA[i] - listA[i-1] < k:
                continue
            temp = self.longestSubstring(s[listA[i-1]:listA[i]], k)
            if temp > maxA:
                maxA = temp
        return maxA
class Solution1:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for cha in set(s):
            if s.count(cha) < k:
                return max(self.longestSubstring(t, k) for t in s.split(cha))
        return len(s)
S = Solution1()
print(S.longestSubstring("bbaaacbd", 3))
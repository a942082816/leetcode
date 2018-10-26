from collections import defaultdict
class Solution:
    def findTheDifference1(self, s, t):
        dictA = defaultdict(int)
        for c in s:
            dictA[c] += 1
        for cc in t:
            if dictA[cc] == 0:
                return cc
            dictA[cc] -= 1
        return ''
    def findTheDifference(self, s, t):
        ss = 0
        for i in range(len(s)):
            ss -= ord(s[i])
            ss += ord(t[i])
        ss += ord(t[-1])
        return chr(ss)

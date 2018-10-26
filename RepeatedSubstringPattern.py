class Solution:
    def isTrueSub(self, s, substr):
        sLen = len(s)
        subLen = len(substr)
        if sLen % subLen != 0:
            return False
        else:
            for i in range(subLen, sLen, subLen):
                for j in range(subLen):
                    if s[i+j] != substr[j]:
                        return False
        return True


    def repeatedSubstringPattern(self, s):
        substr = ''
        sLen =len(s)
        for i in range(int(sLen/2)+1):
            if i == 0:
                substr += s[i]
            else:
                if s[i] == s[0] and s[i-1] == s[sLen-1]:
                    if self.isTrueSub(s, substr):
                        return True
                substr += s[i]
        return False



s = Solution()
ret = s.repeatedSubstringPattern("abab")             
print(ret)

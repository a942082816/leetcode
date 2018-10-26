class Solution:
    def checkRecord(self, s):
        A = 0
        L = 0
        for c in s:
            if c == 'A':
                A += 1
                L = 0
            elif c == 'L':
                L += 1
            else:
                L = 0
            if A > 1 or L > 2:
                return False
        return True


S = Solution()
print(S.checkRecord("LALL"))
class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        if not S:
            return []
        S += 'A'
        count = 1
        start = 0
        ret = []
        for i, c in enumerate(S[1:]):
            if c == S[i]:
                count += 1
            else:
                if count >= 3:
                    ret.append([start, i])
                count = 1
                start = i + 1
        return ret


S = Solution()
print(S.largeGroupPositions("aaa"))



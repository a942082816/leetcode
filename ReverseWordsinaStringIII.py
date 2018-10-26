class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        listA = s.split(' ')
        listB = []
        for word in listA:
            listB.append(word[::-1])
            listB.append(' ')

        return ''.join(listB[0:-1])


S = Solution()
ret = S.reverseWords("Let's take LeetCode contest")
print(ret)
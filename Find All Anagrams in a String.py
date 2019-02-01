#由于为任意顺序,可以采用map<字符, 出现次数> 判断是否相等, 这里采用list[26]充当map, 判断的时候采用滑动窗口的思想, 减少常数项计算量,猜想如碰到
# p中未出现的字符,可以整个窗口跳过
#disscuss 思路基本一致

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        listA = [0] * 26
        listB = [0] * 26
        for c in p:
            listA[ord(c) - ord('a')] += 1
        for c in s[:len(p)]:
            listB[ord(c) - ord('a')] += 1
        ret = []
        for i in range(len(s) - len(p) + 1):
            if i >= 1:
                listB[ord(s[i-1]) - ord('a')] -= 1
                listB[ord(s[i + len(p) - 1]) - ord('a')] += 1
            if listA == listB:
                ret.append(i)
        return ret

S = Solution()
s = "abab"
p = "ab"
print(S.findAnagrams(s,p))



        
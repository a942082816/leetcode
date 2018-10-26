class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        w = 0
        h = 0
        l = 0
        for c in S:
            l = widths[ord(c)-ord('a')]
            if w + l <= 100:
                w += l
            else:
                w = l
                h += 1
        return [h+1, w] 

                

        
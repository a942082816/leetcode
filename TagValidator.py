class Solution:
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        def  parseTagStart(s, i):
            strT = '<'
            flag = False
            while s[i] != '>':
                strT += s[i]
            return strT
        
        def parseTagEnd(s): 
                




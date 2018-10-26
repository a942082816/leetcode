class Solution:
    def strongPasswordChecker(self, s):
        if len(s) < 4:
            return 6 - len(s)
        need = 0
        pre1 = s[0]
        pre2 = s[1]
        lowercase = 0
        uppercase = 0
        digit = 0
        i = 0
        flag = 2
        while i < len(s):
            if s[i].isdigit():
                digit += 1
            elif s[i].islower():
                lowercase += 1
            elif s[i].isupper():
                uppercase += 1
            if flag == 2:
                if  
            
        """
        :type s: str
        :rtype: int
        """
        
class Solution:

    def is_d(self, c):
        if ord(c) >= ord('0') and ord(c) <= ord('9'):
            return True
        return False

    def is_l(self, c):
        if (ord(c) >= ord('a') and ord(c) <= ord('z')) or ((ord(c) >= ord('A') and ord(c) <= ord('Z'))):
            return True
        return False

    def productStr(self, s):
        baseStr = ''
        retStr = ''
        index = 0
        timesStr = ''
        times = 0
        while index < len(s):
            if self.is_d(s[index]):
                timesStr += s[index]
                index +=1
            else:
                index +=1
                break
        times = int(timesStr)
        while index < len(s):
            c = s[index]
            if self.is_l(c):
                baseStr += c
            elif self.is_d(c):
                ret, l = self.productStr(s[index:])
                baseStr += ret
                index += (l-1)
            elif c == ']':
                for i in range(times):
                    retStr += baseStr
                index += 1
                break
            else:
                break
            index +=1
        return retStr, index

    def decodeString(self, s):
        if s == '':
            return ''
        index = 0
        retStr = ''
        while index < len(s):
            if self.is_l(s[index]):
                retStr += s[index]
                index += 1
            else:
                ret ,l = self.productStr(s[index:])
                retStr += ret
                index += l
        return retStr



S =Solution()
#s = '3[a]b'
s ="3[a]2[bc2[a]2[b]]"
#s = '3[ab2[a]]'
s = "3[a10[bc]]"

ret = S.decodeString(s)
print(ret)


                
            
            


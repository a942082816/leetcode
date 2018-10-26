class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        ret = ""
        if num < 0:
            num = pow(2,32) + num
        while num > 0:
            val = num % 16
            num //= 16
            temp = ''
            if val > 9:
                temp = chr(ord('a')+val-10)
            else:
                temp = chr(ord('0')+val)
            ret += temp
        return ret[::-1]


S =Solution()
print(S.toHex(-1))
print(bin(26))



            

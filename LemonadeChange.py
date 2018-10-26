class Solution:
    def lemonadeChange(self, bills):
        wallet = {}
        wallet[5] = 0
        wallet[10] = 0
        wallet[20] = 0
        for i in bills:
            if i == 5:
                wallet[5]+=1
            elif i == 10:
                if wallet[5] == 0:
                    return False
                wallet[5] -= 1
                wallet[10] +=1
            elif i == 20:
                if wallet[10] > 0 and wallet[5]>0:
                    wallet[10] -= 1
                    wallet[5] -= 1
                elif wallet[10] == 0 and wallet[5] >=3:
                    wallet[5] -= 3
                else:
                    return False
        return True


S = Solution()
print(S.lemonadeChange([5,5,10,10,20]))
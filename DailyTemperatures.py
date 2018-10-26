class Solution:
    def dailyTemperatures1(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        listA = [0] * len(T)
        for i in range(len(T)-1, -1, -1):
            if i == len(T) - 1:
                continue
            else:
                temp = 1
                endFlag = False
                while T[i] >= T[i+temp]:
                    if listA[i+temp] == 0:
                        temp += 1
                    else:
                        temp += listA[i+temp]
                    if i + temp >= len(T): 
                        endFlag = True
                        break
                if not endFlag:
                    listA[i] = temp
        return listA
    #栈顶元素为返回的游标, 
    def dailyTemperatures(self, T):
        ret = [0] * len(T)
        stack = []
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                temp = stack[-1]
                stack.pop()
                ret[temp] = i - temp
            stack.append(i)
            print(stack)
        return ret

S = Solution()
ret = S.dailyTemperatures([1,2,1,1,1,73])
print(ret)


                        
            
            

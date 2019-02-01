# 1. list + 最小堆?
# 2. 由于stack的性质只能移除栈顶,因此栈的每一个元素都能维护一个栈底到目前元素为止的最小元素 AC 
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minNum = 0
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append((x, x))
        elif x < self.stack[-1][1]:
            self.stack.append((x, x))
        else:
            self.stack.append((x, self.stack[-1][1]))

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
minStack = MinStack()
A = ["push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
B = [[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]
for i, funName in enumerate(A):
    func = getattr(minStack, funName)
    if not B[i]:
        print(func())
    else:
        func(B[i][0])
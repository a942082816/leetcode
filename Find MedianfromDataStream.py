import heapq
class MedianFinder:
    def __init__(self):
        self.heapLeft = []
        self.heapRight = []
        self.leftLen = 0
        self.rightLen = 0
        """
        initialize your data structure here.
        """

    def addNum(self, num):
        if self.leftLen == 0:
            heapq.heappush(self.heapLeft, -num)
            self.leftLen += 1
            return

        if self.leftLen > self.rightLen:
            if num > -self.heapLeft[0]:
                heapq.heappush(self.heapRight, num)
            else:
                heapq.heappush(self.heapRight, -heapq.heappop(self.heapLeft))
                heapq.heappush(self.heapLeft, -num)
            self.rightLen += 1
        elif self.leftLen < self.rightLen:
            if num < self.heapRight[0]:
                heapq.heappush(self.heapLeft, -num)
            else:
                heapq.heappush(self.heapLeft, -heapq.heappop(self.heapRight))
                heapq.heappush(self.heapRight, num)
            self.leftLen += 1
        else:
            if num > -self.heapLeft[0]:
                heapq.heappush(self.heapRight, num)
                self.rightLen += 1
            else:
                heapq.heappush(self.heapLeft, -num)
                self.leftLen += 1
        return


    def findMedian(self):
        if self.leftLen == 0:
            return float(self.heapRight[0])
        if self.rightLen == 0:
            return float(-self.heapLeft[0])
        if (self.leftLen+self.rightLen) % 2 == 0:
            return float((-self.heapLeft[0]+self.heapRight[0]) / 2.0)
        else:
            if self.leftLen > self.rightLen:
                return float(-self.heapLeft[0])
            else:
                return float(self.heapRight[0])



F = MedianFinder()
F.addNum(6)
print(F.findMedian())
F.addNum(10)
print(F.findMedian())
F.addNum(2)
print(F.findMedian())
F.addNum(6)
F.addNum(5)
F.addNum(0)
print(F.findMedian())
F.addNum(6)
F.addNum(3)
print(F.findMedian())
        

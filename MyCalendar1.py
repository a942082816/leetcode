import bisect
class MyCalendar:

    def __init__(self):
        self.beginList = []

    def book(self, start, end):

        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.beginList:
            self.beginList.append((start,end))
            return True
        i = bisect.bisect_left(self.beginList, (start, end))
        if i == 0 :
            if end > self.beginList[0][0]:
                return False
            else:
                self.beginList.insert(i, (start, end))
                return True
        if i == len(self.beginList):
            if start < self.beginList[i-1][1]:
                return False
            else:
                self.beginList.append((start, end))
                return True
        if i != len(self.beginList) and (start < self.beginList[i-1][1] or end > self.beginList[i][0]):
            return False
        self.beginList.insert(i, (start, end))
        return True

obj = MyCalendar()
print(obj.book(47,50))
print(obj.book(33,41))
print(obj.book(39,45))
print(obj.book(33,42))
print(obj.book(25,32))
print(obj.book(26,35))
print(obj.book(19,25))
print(obj.book(3,8))
print(obj.book(8,13))
print(obj.book(18,27))
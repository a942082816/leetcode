import bisect
class MyCalendarTwo:

    def __init__(self):
        self.twice = []
        self.once = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        ti = bisect.bisect_left(self.twice, (start, end))
        if ti:
            if ti == 0: 
                if end > self.twice[0][0]:
                    return False
            elif ti == len(self.twice):
                if start < self.twice[ti-1][1]:
                    return False
            else:
                if (start < self.twice[i-1][1] or end > self.twice[i][0]):
                    return False
        
        if not self.once:
            self.once.append((start, end))
        oi = bisect.bisect_left(self.once, (start, end))

        if i == 0 :


        

        
        
            
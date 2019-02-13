# init O(nlogn)  add (log k)
# discuss use heap
import bisect
class KthLargest:
    def __init__(self, k: 'int', nums: 'List[int]'):
        self.beforeK = sorted(nums)[-k:]
        self.k = k

    def add(self, val: 'int') -> 'int':
        if len(self.beforeK) < self.k: 
            bisect.insort_right(self.beforeK, val)
            return self.beforeK[0]

        if val <= self.beforeK[0]:
            return self.beforeK[0]
        bisect.insort_right(self.beforeK, val)
        self.beforeK.remove(self.beforeK[0])
        return self.beforeK[0]
        
        


# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(3, [5, -1])
print(obj.add(2))
print(obj.add(1))
print(obj.add(-1))
print(obj.add(3))
print(obj.add(4))
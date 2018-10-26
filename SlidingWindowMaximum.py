import heapq
import collections
class Solution:
    def maxSlidingWindow(self, nums, k):
        d = collections.deque()  #d[0] 最大值的index
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n: #如比当前数字小  队尾全都出队
                d.pop()
            d.append(i)               #当前元素入队
            if d[0] == i - k:     #最大元素刚好为移动过去的元素
                d.popleft()
            if i >= k - 1:              #k长度之前不做处理
                out.append(nums[d[0]])
        return out

    def maxSlidingWindow1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        heap = []
        setT = set()
        for i in range(k):
           heapq.heappush(heap, -nums[i])
        retList = []
        retList.append(-heap[0])
        dictA = defaultdict(int)
        dictA[nums[0]] = 1
        for i in range(k, len(nums)):
            heapq.heappush(heap, -nums[i])
            while dictA[-heap[0]] > 0:
                val = -heapq.heappop(heap)
                dictA[val] -= 1
            retList.append(-heap[0])
            dictA[nums[i-k+1]] += 1
        return retList


S =Solution()
ret = S.maxSlidingWindow([1,3,1,2,0,5],3)
print(ret)
# 统计每个元素出现的次数, 取出现次数最多的元素,中间插入 其他元素或者idle, 结果为 maxCount * (n + 1) -  (n - count)
from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: 'List[str]', n: 'int') -> 'int':
        countMap = defaultdict(int)
        for c in tasks:
            countMap[c] += 1
        
        sortList = sorted(countMap.values(), reverse=True)
        begin = sortList[0]
        count = 0
        for i in range(1, len(sortList)):
            if sortList[i] == begin:
                count += 1
            else:
                break
        return max(begin * (n+1) - (n - count), len(tasks))

s = Solution()
ret = s.leastInterval(["A","A","A","B","B","B"], 50)
print(ret)        

        
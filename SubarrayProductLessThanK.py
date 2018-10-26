import math
import bisect
class Solution:
    def numSubarrayProductLessThanK2(self, nums, k):
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans


    def numSubarrayProductLessThanK3(self, nums, k):
        if k == 0: return 0
        k = math.log(k)

        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + math.log(x))

        ans = 0
        for i, x in enumerate(prefix):
            j = bisect.bisect(prefix, x + k - 1e-9, i+1)
            ans += j - i - 1
        return ans

    def numSubarrayProductLessThanK1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        num = 0
        lenNums = len(nums)
        dp = [([0]* lenNums)for i in range(lenNums)]
        for i in range(lenNums):
            dp[i][i] = nums[i]
            if nums[i] < k:
                num +=1

        for i in range(lenNums):
            for j in range(i-1,-1,-1):
                dp[i][j] = nums[j]*dp[i][j+1]
                if dp[i][j] < k:
                    num += 1
        return num

S =Solution()
a = [10,5,2,6]
print(S.numSubarrayProductLessThanK(a,0))

        
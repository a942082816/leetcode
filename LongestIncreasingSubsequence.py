class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) ==0:
            return 0
        dp=[0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            for ii in range(i):
                if nums[ii] < nums[i]:
                    if dp[i] < dp[ii] +1:
                        dp[i] = dp[ii] + 1
            if dp[i] == 0:
                dp[i] = 1
        return max(dp)

S = Solution()
nums = [10,9,2,5,3,7,101,18]
num = S.lengthOfLIS(nums)
print(num)
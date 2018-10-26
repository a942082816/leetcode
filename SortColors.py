class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        begin = 0
        end = len(nums) - 1
        size = 0
        n = 0
        while n <= end:
            if nums[n] == 2:
                nums[n] = nums[end]
                nums[end] = 2
                end -= 1
            elif nums[n] == 1:
                n += 1
            else:
                nums[n] = nums[begin]
                nums[begin] = 0
                begin += 1
                n += 1
            
S = Solution()
l = [2,0,1]
S.sortColors(l)
print(l)

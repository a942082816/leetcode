class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.insert(0, -0xFFFFFFFF)
        nums.append(-0xFFFFFFFFF)
        retList = []
        for i, v in enumerate(nums[1:-1]):
            if v > nums[i] and v > nums[i+2]:
                return i
            
            
S =  Solution()
print(S.findPeakElement([1,2,3,1]))
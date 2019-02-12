#重点1 ≤ a[i] ≤ n ,因此可以使用 nums[nums[i] - 1] 的正负值来表示有没有出现过第二次
class Solution:
    def findDuplicates(self, nums: 'List[int]') -> 'List[int]':
        ret = []
        if not nums:
            return []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                ret.append(abs(nums[i]))
            else:
                nums[index] = -nums[index]
        return ret


S = Solution()
print(S.findDuplicates([10,2,5,10,9,1,1,4,3,7]))
        
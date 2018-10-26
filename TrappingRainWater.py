class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        r = 0
        l = len(height) - 1
        ret = 0 
        while r < l:
            minV = min(height[r],height[l])
            if minV ==  height[r]:
                while r<l and height[r]<=minV:
                    ret += minV - height[r]
                    r +=1
            else:
                while r<l and height[l] <= minV:
                    ret += minV - height[l]
                    l -= 1
        return ret



S = Solution()
print(S.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
def isBadVersion(version):
    if version >= 2:
        return True
    return False

class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n
        if n == 1:
            return 1
        while left != right:
            mid = int((left + right) / 2)
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                right = mid
            else:
                if isBadVersion(mid +1):
                    return mid+1
                left = mid

S = Solution()
ret = S.firstBadVersion(2)
print(ret)
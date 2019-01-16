import bisect
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        listA = []
        listB = []
        for i in matrix:
            if not i:
                continue
            listA.append(i[0])
            listB.append(i[-1])
        if not listA:
            return False
        index = bisect.bisect_left(listA, target)
        index1 = bisect.bisect_left(listB, target)
        if index == index1 and index >= len(matrix):
            return False
        index2 = bisect.bisect_left(matrix[min(index, index1)], target)
        if matrix[min(index, index1)][index2] == target:
            return True
        return False

matrix = [[1]]
S = Solution()
print(S.searchMatrix(matrix, 2))

        
class NumMatrix1:
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.dp1 = []
        for l in matrix:
            dpt = [([0] * len(l)) for i in range(len(l))]
            for i in range(len(l)):
                dpt[i][i] = l[i]
            for i in range(len(l)):
                for j in range(i-1, -1, -1):
                    dpt[j][i] = dpt[j+1][i] + l[j]
            self.dp1.append(dpt)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sumA = 0
        for i in range(row1, row2+1):
            sumA += self.dp1[i][col1][col2]
        return sumA


class NumMatrix:
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.dp1 = []

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """


        
# Your NumMatrix object will be instantiated and called as such:
'''
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
'''
matrix = [[-4, -5]]
obj = NumMatrix(matrix)
print(obj.sumRegion(0, 0, 0, 1))
# param_1 = obj.sumRegion(row1,col1,row2,col2)
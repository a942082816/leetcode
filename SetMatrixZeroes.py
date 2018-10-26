class Solution:
    def setZeroes1(self, matrix):

        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        if row == 0:
            return 0
        col = len(matrix[0])
        if row == 0 and col == 0:
            return 0
        setX = set()
        setY = set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    setX.add(i)
                    setY.add(j)
        
        for i in range(row):
            for j in range(col):
                if i in setX or j in setY:
                    matrix[i][j] = 0
        

                
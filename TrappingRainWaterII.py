class Solution:

    def trapRainWater(self, heightMap):
        row = len(heightMap)
        if row == 0:
            return 0
        col = len(heightMap[0])
        if row == 0 and col == 0:
            return 0
        listR = [([0] * col) for i in range(row)]
        listL = [([0] * col) for i in range(row)]
        listU = [([0] * row) for i in range(col)]
        listD = [([0] * row) for i in range(col)]
        maxR = 0
        maxL = 0
        maxU = 0
        maxD = 0

        for i in range(row):
            maxR = 0
            maxL = 0
            for j in range(col):
                if heightMap[i][j] > maxR:
                    maxR = heightMap[i][j]
                if heightMap[i][col - j - 1] > maxL:
                    maxL = heightMap[i][col - j - 1]
                listR[i][j] = maxR
                listL[i][col - j - 1] = maxL
        for i in range(col):
            maxU = 0
            maxD = 0
            for j in range(row):
                if heightMap[j][i] > maxU:
                    maxU = heightMap[j][i]
                if heightMap[row - j- 1][i] > maxD:
                    maxD = heightMap[row - j- 1][i]
                listU[i][j] = maxU
                listD[i][row - j - 1] = maxD
        ret = 0
        for i in range(row):
            for j in range(col):
                minV = min(listR[i][j], listL[i][j], listU[j][i], listD[j][i])
                if heightMap[i][j] < minV:
                    ret += minV - heightMap[i][j]
        return ret


S = Solution()
listA =[[12,13,1,12],
        [13,4,13,12],
        [13,8,10,12],
        [12,13,12,12],
        [13,13,13,13]]
print(S.trapRainWater(listA))                

class Solution(object):
    def solveNQueens1(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        retList = []
        def conflict(positions, position):
            for p in positions:
                if p[0] == position[0] or p[1] == position[1] or abs(p[0] - position[0]) == abs(p[1] - position[1]):
                    return False
            return True
        
        def solve(positions):
            if len(positions) == n:
                temp = [(['.'] * n) for i in range(n)]
                for v in positions:
                    temp[v[0]][v[1]] = 'Q'
                retList.append([''.join(i) for i in temp])
                return
            for i in range(n):
                if conflict(positions, (len(positions), i)):
                    positions.append((len(positions),i))
                    solve(positions)
                    positions.pop()
        positions = []
        for i in range(n):
            positions = [(0,i)]
            solve(positions)
        return retList

    def solveNQueens(self, n):
        def DFS(queens, xy_dif, xy_sum):
            print(queens,xy_dif,xy_sum)
            p = len(queens)
            if p == n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
        result = []
        DFS([],[],[])
        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]
    
    def totalNQueens(self, n):
        self.num = 0
        def DFS(queens, xy_dif, xy_sum):
            global num
            p = len(queens) 
            if p == n:
                self.num += 1
                return 
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
        DFS([],[],[])
        return self.num

S = Solution()
print(S.totalNQueens(4))
            

            



class Solution:
    def isNotInABCD(self, A, B, C, D, E, F, G, H):
        if (max(A, C) >= E and min(A, C) <= E) or (max(A, C) >= G and min(A, C) <= G) or (max(G,E)>=A and min (G,E)<=A) or (max(G,E)>=C and min (G,E)<=C):
            if(max(B, D) >= F and min(B, D) <= F) or(max(B, D) >= H and min(B, D) <= H) or (max(H,F) >=B and min(H,F)<=B) or(max(H,F) >=D and min(H,F)<=D) :
                return False
        return True


    def  isNotIN(self, A, B, C, D, E, F, G, H):
        return B>=H or E>=C or F>=D or A>=G
    
    def computeArea(self, A, B, C, D, E, F, G, H):
        S1 = abs((A-C) * (B-D))
        S2 = abs((G-E) * (F-H))
        if self.isNotIN(A, B, C, D, E, F, G, H):
            return S1+S2
        w = min(C,G) - max(A,E)
        h = min(D,H) - max(B,F)
        return S1 + S2 - abs(w*h)


so = Solution()
#S = so.computeArea(-3,0,3,4,0,-1,9,2)
#S = so.computeArea(0, 0, 0, 0, -1, -1, 1, 1)
#S = so.computeArea(-2, -2, 2, 2, 3, 3, 4, 4)
S = so.computeArea(-2, -2, 2, 2, -3, -3, 3, -1)
print(S)
# 先全加一遍 在挨个减 (阶梯状减)
class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        listA, sumN = [0], 0 
        for shift in shifts:
            sumN += shift
            listA.append(sumN)
        sumS = sum(shifts)
        listB = [((ord(c) - ord('a') + sumS - listA[i]) % 26) for i, c in enumerate(S)]
        return ''.join([chr(ord('a') + i) for i in listB])
    
solution = Solution()
print(solution.shiftingLetters("abc", [3,5,9]))

        



        
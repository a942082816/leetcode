#dict 映射 easy
class Solution:
    #AC 
    def isAlienSortedOld(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dictA = {}
        for i, v in enumerate(order):
            dictA[v] = i
        
        def isBigger(A, B):
            for i in range(min(len(A), len(B))):
                if dictA[A[i]] > dictA[B[i]]:
                    return True
                elif dictA[A[i]] < dictA[B[i]]:
                    return False
                else:
                    continue
            return len(A) >= len(B)


        for i in range(1, len(words)):
            if isBigger(words[i], words[i-1]):
                continue
            else:
                return False
        return True

    # 思路一样  diss 代码简化版
    def isAlienSorted(self, words, order):
        lookup = {ch: i for i, ch in enumerate(order)}
        X = sorted(words, key=lambda word: [lookup[ch] for ch in word])
        return X == words


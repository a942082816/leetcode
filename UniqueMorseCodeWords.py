
class Solution:
    def uniqueMorseRepresentations(self, words):
        listA =[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        listB = set(words)
        listC = set()
        for word in listB:
            temp = ''
            for w in word:
                temp += listA[ord(w-'a')]
            listC.add(temp)
        return len(listC)



        """
        :type words: List[str]
        :rtype: int
        """
        

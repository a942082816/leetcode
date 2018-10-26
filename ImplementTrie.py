class Node(object):
    def __init__(self, c=''):
        self.value = c
        self.next = [None] * 26
        self.isOver = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node() 

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        temp = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not temp.next[index]:
                temp.next[index] = Node(c)
            temp = temp.next[index]
        temp.isOver = True
        
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        temp = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not temp.next[index]:
                return False
            temp = temp.next[index]
        if not temp.isOver:
            return False
        return True
        
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        temp = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if not temp.next[index]:
                return False
            temp = temp.next[index]
        return True
        

trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))
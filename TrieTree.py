

class TrieNode(object):
    def __init__(self, *args, **kwargs):
        self.num = 1;
        self.child1 = []
        self.isEnd = False
        self.value = None

class TrieTree(object):
    def __init__(self, *args, **kwargs):
        self.size = 26
        self.root = TrieNode()

    def insert(self, str):
        if len(str) == 0:
            return
        for index in range(len(str)):
            pos = ord(str[index]) - ord('a')
            if self.node == 
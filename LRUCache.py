
class Node:
    def __init__(self, x):
        self.value = x
        self.next = None
        self.prev = None

class LinkList:
    def __init__(self):
        self.head = Node(None)
        self.head.next = self.head
        self.head.prev = self.head

    def insert(self, x):
        node = Node(x)
        node.next = self.head
        node.prev = self.head.prev
        self.head.prev.next = node
        self.head.prev = node
        return node

    def removeHead(self):
        value = self.head.next.value
        self.delete(self.head.next)
        return value

    def delete(self, node):
        if not node:
            self.showList()
            return False
        node.prev.next = node.next
        node.next.prev = node.prev
        return True

    def getHead(self):
        return self.head

    def getTail(self):
        return self.head.prev

    def isEmpty(self):
        return self.head.prev == self.head

    def find(self, x):
        begin = self.head.next
        while begin != self.head:
            if begin.value == x:
                return begin
            begin = begin.next
        return None

    def showList(self):
        it = self.head.next
        listT = []
        while it != self.head:
            listT.append(it.value)
            it = it.next
        print(listT)
        

class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dictA = {}
        self.dictB = {}
        self.size = 0
        self.capacity = capacity
        self.list = LinkList()
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dictB:
            node = self.dictB[key]
            self.list.delete(node)
            node = self.list.insert(key)
            self.dictB[key] = node
            return self.dictA[key]
        else:
            return -1

    def put(self, key, value):
        if key in self.dictA:
            self.dictA[key] = value
            node = self.dictB[key]
            self.list.delete(node)
            node = self.list.insert(key)
            self.dictB[key] = node
        else:
            if self.size < self.capacity:
                node = self.list.insert(key)
                self.dictA[key] = value
                self.dictB[key] = node
                self.size += 1
            else:
                x = self.list.removeHead()
                node = self.list.insert(key)
                self.dictA.pop(x)
                self.dictB.pop(x)
                self.dictA[key] = value
                self.dictB[key] = node

    
# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(10)
#print(cache.put(1, 1))
#print(cache.put(2, 2))
#print(cache.get(1))
#print(cache.put(3, 3))
#print(cache.get(2))
#print(cache.put(4, 4))
#print(cache.get(1))
#print(cache.get(3))
#print(cache.get(4))
func = ["put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
param = [[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
print(param[45])
for i in range(len(func)):
    function = getattr(cache,func[i])
    if func[i] == 'put':
        try:
            function(param[i][0],param[i][1])
        except Exception:
            print(cache.dictA)
            cache.list.showList()
            break
    else:
        function(param[i][0])

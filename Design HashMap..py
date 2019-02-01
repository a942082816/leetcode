#简单的取余hash + 链表解决冲突, 性能非常差,偶尔timelimit,可以采用更好的hash函数和以及rehash等优化

class Node:
    def __init__(self, k, v):
        self.next = None
        self.key = k
        self.val = v
class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket = []
        for i in range(4096):
            self.bucket.append(Node(0,0))
            
    def put(self, key, value):
        """
        :type key: int
        :rtype: void
        """
        index = self.hash(key)
        l = self.bucket[index]
        while l.next:
            if l.next.key == key:
                l.next.val = value
                return
            l = l.next
        node = Node(key, value)
        l.next = node

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        index = self.hash(key)
        l = self.bucket[index]
        while l.next:
            if l.next.key == key:
                ret = l.next.val
                l.next = l.next.next
                return 
            l = l.next
        

    def get(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        index = self.hash(key)
        l = self.bucket[index]
        while l.next:
            if l.next.key == key:
                return l.next.val
            l = l.next
        return -1


    def hash(self, key):
        return key & (len(self.bucket) - 1)

hashMap = MyHashMap()
hashMap.put(1, 1)
hashMap.put(2, 2)
print(hashMap.get(1))
print(hashMap.get(3))
hashMap.put(2, 1)
print(hashMap.get(2))
hashMap.remove(2)
print(hashMap.get(2))
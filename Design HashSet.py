#简单的取余hash + 链表解决冲突, 性能非常差,偶尔timelimit,可以采用更好的hash函数和以及rehash等优化
# tl 是因为list初始化时用的是通一个Node, hash退化成了链表

class Node:
    def __init__(self, v):
        self.next = None
        self.val = v
class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.bucket = [Node(0)] * 4096
        self.bucket = [Node(0) for i in range(1 << 16)]

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        index = self.hash(key)
        l = self.bucket[index]
        while l.next:
            if l.next.val == key:
                return
            l = l.next
        node = Node(key)
        l.next = node

        

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        index = self.hash(key)
        l = self.bucket[index]
        while l.next:
            if l.next.val == key:
                l.next = l.next.next
                return
            l = l.next
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        index = self.hash(key)
        l = self.bucket[index]
        while l.next:
            if l.next.val == key:
                return True
            l = l.next
        return False


    def hash(self, key):
        return key & (len(self.bucket) - 1)
        
    


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
obj.remove(1)
print(obj.contains(1))
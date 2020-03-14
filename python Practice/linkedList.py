class ListNode:
    def __init__(self,key=None,value=None):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value

    def __str__(self):
        return 'key: {}, value: {}'.format(self.key, self.value) if self.value else 'key: {}'.format(self.key)

class LinkedList:
    def __init__(self,lst=None):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        if lst:
            for key in lst:
                self.add(key)

    def add(self,otherKey,value=None,ind=None):
        if value:
            other = ListNode(otherKey,value)
        else:
            other = ListNode(otherKey)

        if ind and ind <= self.size:
            currNode = self.head
            for i in range(ind):
                currNode = currNode.next
            other.next = currNode
            other.prev = currNode.prev
            other.prev.next = other
            currNode.prev = other
        else:
            other.next = self.tail
            other.prev = self.tail.prev
            self.tail.prev.next = other
            self.tail.prev = other
        self.size += 1

    def remove(self,ind=-1):
        if self.size > 0:
            if ind > 0 and ind <= self.size:
                currNode = self.head
                for i in range(ind):
                    currNode = currNode.next
                currNode.prev.next = currNode.next
                currNode.next.prev = currNode.prev
            else:
                currNode = self.tail.prev
                self.tail.prev = self.tail.prev.prev
                self.tail.prev.next = self.tail
            self.size -= 1
            return currNode
        return None

    def removeKey(self,key):
        if self.size > 0:
            currNode = self.head.next
            while currNode:
                if currNode.key == key:
                    currNode.prev.next = currNode.next
                    currNode.next.prev = currNode.prev
                    self.size -= 1
                    return currNode
                currNode = currNode.next
        return None

    def getKey(self,key):
        if self.size > 0:
            currNode = self.head.next
            while currNode:
                if currNode.key == key:
                    return currNode
                currNode = currNode.next
        return None

    def get(self,ind=-1):
        if self.size > 0:
            if ind > 0 and ind <= self.size:
                currNode = self.head
                for i in range(ind):
                    currNode = currNode.next
                return currNode
            else:
                return self.tail.prev
        return None

    def contains(self,key):
        currNode = self.head.next
        while currNode:
            if currNode.key == key:
                return True
            currNode = currNode.next
        return False

    def __str__(self):
        lst = []
        currNode = self.head.next
        while currNode and currNode != self.tail:
            lst.append(str(currNode))
            currNode = currNode.next
        return 'size {}: {}'.format(self.size, str(lst))

if __name__ == '__main__':
    lst = LinkedList([1,2])
    lst.add(3,3)
    lst.removeKey(3)
    lst.removeKey(2)
    assert lst.size == 1
    print(lst)


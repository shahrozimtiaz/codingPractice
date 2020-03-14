from linkedList import *
import time

class Hashset:
    def __init__(self,toAdd=[]):
        self.maxSize = 10000
        self.size = 0
        self.lst = [None] * self.maxSize
        for obj in toAdd:
            self.put(obj)

    def put(self,other):
        if not self.contains(other):
            hsh = abs(hash(other)) % self.maxSize
            if not self.lst[hsh]:
                self.lst[hsh] = LinkedList()
            self.lst[hsh].add(other)
            self.size +=1

    def contains(self,other):
        hsh = abs(hash(other)) % self.maxSize
        if hsh > len(self.lst):
            return False
        if not self.lst[hsh]:
            return False
        return self.lst[hsh].contains(other)

    def remove(self,other):
        hsh = abs(hash(other)) % self.maxSize
        if hsh > len(self.lst):
            return False
        if not self.lst[hsh]:
            return False
        removed = self.lst[hsh].removeKey(other)
        if removed:
            self.size -=1
        if self.lst[hsh].size == 0:
            self.lst[hsh] = None
        return removed

    def __str__(self):
        for i in range(len(self.lst)):
            if self.lst[i]:
                print('bucket {} | {}'.format(i,self.lst[i]))
        return 'Hashmap size: {}'.format(self.size)


class Person:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'name: {}'.format(self.name)

if __name__ == '__main__':
    hashset = set()
    start_time = time.time()
    for i in range(100000):
        hashset.add(i)
    print("python set: {} seconds".format(time.time() - start_time))


    hashset = Hashset()
    start_time = time.time()
    for i in range(100000):
        hashset.put(i)
    print("my set: {} seconds".format(time.time() - start_time))

    for i in range(100000):
        hashset.put(i)
        assert hashset.contains(i) == True
        hashset.remove(i)
        assert hashset.contains(i) == False
    print('validation complete')

    # print(hashset)
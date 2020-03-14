from linkedList import *
import time

class Hashmap:
    def __init__(self,toAdd=[]):
        self.maxSize = 10000
        self.size = 0
        self.lst = [None] * self.maxSize
        for obj in toAdd:
            self.put(obj)

    def put(self,key,value):
        self.remove(key)
        hsh = abs(hash(key)) % self.maxSize
        if not self.lst[hsh]:
            self.lst[hsh] = LinkedList()
        self.lst[hsh].add(key,value=value)
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

    def get(self,key):
        hsh = abs(hash(key)) % self.maxSize
        if hsh > len(self.lst):
            return False
        if not self.lst[hsh]:
            return False
        entry = self.lst[hsh].getKey(key)
        if entry:
            return entry.value
        return None

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
    hashmap = {}
    start_time = time.time()
    for i in range(100000):
        hashmap[i]=i+1
    print("python set: {} seconds".format(time.time() - start_time))


    hashmap = Hashmap()
    start_time = time.time()
    for i in range(100000):
        hashmap.put(i,i+1)
    print("my set: {} seconds".format(time.time() - start_time))

    for i in range(100000):
        hashmap.put(i,i+1)
        assert hashmap.contains(i) == True
        assert hashmap.get(i) == i+1
        hashmap.remove(i)
        assert hashmap.contains(i) == False
    hashmap.put('hello','world')
    hashmap.put('hello','world2')
    assert hashmap.get('hello')=='world2'
    print('validation complete')

    print(hashmap)
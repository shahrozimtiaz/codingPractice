import numpy as np

def find_min(lst):
    smallest = lst[0]
    for i in range(1,len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]
    return smallest

def find_max(lst):
    smallest = lst[0]
    for i in range(1,len(lst)):
        if lst[i] > smallest:
            smallest = lst[i]
    return smallest

def selection_sort(lst):
    lst = lst.copy()
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

def quick_sort(lst):
    lst = lst.copy()
    def partition(low,high):
        pivot = lst[(low+high)//2]
        i = low - 1
        j = high + 1
        while True:
            i+=1
            while lst[i] < pivot:
                i+=1
            j-=1
            while lst[j] > pivot:
                j-=1
            if i >= j:
                return j
            lst[i],lst[j] = lst[j],lst[i]
    def _quick_sort(low,high):
        if low < high:
            split_index = partition(low,high)
            _quick_sort(low,split_index)
            _quick_sort(split_index+1,high)

    _quick_sort(0,len(lst)-1)
    return lst

def mode(lst):
    count = {}
    for item in lst:
        count[item] = count.get(item,0) + 1

    highest_key = None
    highest_value = 0

    for key,value in count.items():
        if value > highest_value:
            highest_key = key
            highest_value = value
    return highest_key

def mean(lst):
    sum = 0
    for num in lst:
        sum += num
    return sum/len(lst)

def median(lst):
    lst.sort()
    if len(lst) % 2 == 0:
        return (lst[int(len(lst) / 2)-1] + lst[int(len(lst) / 2 + 1)-1]) / 2
    return lst[int(len(lst)/2)]

def shuffle(lst):
    lst = lst.copy()
    for i in range(len(lst)-1,0,-1):
        n = np.random.randint(0,i+1)
        lst[i], lst[n] = lst[n],lst[i]
    return lst

def fib(n,lst):
    if n <= 1:
        return n
    if lst[n] != 0:
        return lst[n]
    else:
        comp = fib(n-1,lst) + fib(n-2,lst)
        lst[n] = comp
        return comp

def remove_duplicates(lst):
    lst.copy()
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[j] == lst[i]:
                del lst[j]
                i -= 1
                break
    return lst

def remove_duplicates(lst):
    lst_set = set()
    for item in lst:
        lst_set.add(item)
    return lst_set

def palindrome(string):
    i = 0
    j = len(string)-1
    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True

def phoneLetterCombinations(digits: str):
    def combos(letters, n, output, currLettersInd, combo):
        if currLettersInd > n:
            if not combo == '':
                output.append(combo)
            return output
        for letter in letters[currLettersInd]:
            output = combos(letters, n, output, currLettersInd + 1, combo + letter)
        return output
    dic = {}
    dic['2'] = 'abc'
    dic['3'] = 'def'
    dic['4'] = 'ghi'
    dic['5'] = 'jkl'
    dic['6'] = 'mno'
    dic['7'] = 'pqrs'
    dic['8'] = 'tuv'
    dic['9'] = 'wxyz'
    letters = []
    for digit in digits:
        letters.append(dic[digit])
    n = len(letters) - 1
    return combos(letters, n, [], 0, '')

def wordsGenerator(letters:str):
    count = {}
    for letter in letters:
        count[letter] = count.get(letter,0)+1
    myWords = []
    words = open('words.txt').readlines()
    for i in range(len(words)):
        word = words[i]
        word = word.replace('\n','')
        # if len(word) == len(letters):
        if len(word) > 1:
            myWords.append(word)
    words = myWords
    wordsGen = []
    for word in words:
        valid = True
        dic = count.copy()
        for letter in word:
            if letter not in letters:
                valid = False
                break
            dic[letter] = dic.get(letter) - 1
        if valid:
            valid2 = True
            for value in dic.values():
                if value < 0:
                    valid2 = False
            if valid2:
                wordsGen.append(word)
    return 'random words using {}: {}'.format(letters,wordsGen) if len(wordsGen) > 0 else 'random words using {}: no word can be formed'.format(letters)

def removeNthFromEndSinglePass(self, head, n: int):
    p1 = p2 = head
    for _ in range(n):
        p2 = p2.next
    if not p2:
        return head.next
    while p2.next:
        p2 = p2.next
        p1 = p1.next
    p1.next = p1.next.next
    return head


def removeNthFromEnd(head, n: int):
    def _removeNthRecur(n, head, prev, curr, count):
        if not curr:
            return 0
        count = _removeNthRecur(n, head, curr, curr.next, count) + 1
        if count == n:
            if prev:
                prev.next = curr.next
            else:
                head.val = curr.next.val
                head.next = curr.next.next
        return count

    if not head.next:
        head = None
    else:
        _removeNthRecur(n, head, None, head, 0)
    return head

class ListNode:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

if __name__ == '__main__':
    # print('min:',find_min([3,4,1,5,6]))
    # print('max:',find_max([3,4,7,1,5,6]))
    # n = 14
    # print('{}th digit of fibonacci: {}'.format(n,fib(n, np.zeros(n+1, dtype=object))))
    # unsorted_lst = list(np.random.randint(0,1000,10))
    # print('sorted list:',quick_sort(unsorted_lst))
    # print(mode([1,2,3,2,3,3]))
    # print(mean([1,2,2]))
    # print(median([1,5,4,6]))
    # print(shuffle([1,5,4,6]))
    # print(remove_duplicates([1,1,2,2,3,3]))
    # print(palindrome('racecar'))
    # print(phoneLetterCombinations('23'))
    print(wordsGenerator('wertyui'))
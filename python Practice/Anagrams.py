def anagramCheck(str1, str2):
    mp = {}
    for c in str1:
        mp[c]= mp.get(c,0)+1
    for c in str2:
        mp[c]= mp.get(c,0)-1
    for v in mp.values():
        if(v !=0):
            return False
    return True

while True:
    s1 = input()
    if(s1 == "stop"):
        print('stopping')
        raise SystemExit()
    s2 = input()
    print(anagramCheck(s1,s2))
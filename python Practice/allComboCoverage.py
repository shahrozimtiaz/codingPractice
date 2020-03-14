#REQUIREMENTS
# a1,a2,a3,a4 = 'non-empty string without special characters', 'non-empty string with special characters', 'more than 1 string as input','empty string'
# b1,b2,b3 = 'clear chosen strings', 'submit', 'restart'
# c1,c2 = 'with replacement', 'without replacement'
# d1,d2 = 'clicked', 'not clicked'

#TEST CASES
a1,a2,a3,a4 = '"software testing"', '"software\\ntesting"', '"software""testing"','""'
b1,b2,b3 = 'clear chosen strings', 'submit', 'restart'
c1,c2 = 'with replacement', 'without replacement'
d1,d2 = 'click refresh', 'don\'t click refresh'

a = [a1,a2,a3,a4]
b = [b1,b2,b3]
c = [c1,c2]
d = [d1,d2]
i = 1
for ab in a:
    s = '{ ' + ab
    for bb in b:
        s1 = ', ' + bb
        s+= s1
        for cb in c:
            s2 = ', ' + cb
            s+= s2
            for db in d:
                s3 = ', ' + db + ' }'
                s += s3
                print('TC{}:\n inputs ={}\n expected output:\n   input box:\n   output box:\n   string chosen box:\n'.format(i, s))
                i += 1
                s = s[:-len(s3)]
            s = s[:-len(s2)]
        s = s[:-len(s1)]
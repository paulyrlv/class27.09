s = str(input())
le = len(s)
sTwo = ''
i = 0
count = 1
while i < le - 1:
    if (i + 1 == le - 1) and (i + 1 != i):
        sTwo = sTwo + s[i]
        sTwo = sTwo + '2'
        count = 1
        i = i + 1
    elif i + 1 == le - 1:
        sTwo = sTwo + s[i]
        sTwo = sTwo + '2'
        count = 1
        i = i + 1
    elif s[i] == s[i + 1]:
        count = count + 1
        i = i + 1
    else:
        sTwo = sTwo + s[i]
        sTwo = sTwo + str(count)
        count = 1
        i = i + 1
    if le == 1:
        sTwo = s[i] + '1'
if s[-1] != s[-2]:
    sTwo = sTwo + s[-1] + '1'
print(sTwo)

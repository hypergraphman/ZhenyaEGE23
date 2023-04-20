s = open('test.txt').read()

k = 0
for i in range(2, len(s)):
    if (s[i - 2] in 'BCD' and
       s[i - 2] != s[i - 1] and s[i - 1] in 'BDE' and
       s[i - 1] != s[i] and s[i] in 'BCE'):
        k += 1
print(k)

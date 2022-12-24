from itertools import permutations

alf = 'капкан'
s = set()
for letters in permutations(alf):
    word = ''.join(letters)
    if 'кк' not in word and 'аа' not in word:
        s.add(word)
print(s)
print(len(s))
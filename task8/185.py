from itertools import product

alf = '0123456789'
k = 0
for letters in product(alf, repeat=6):
    word = ''.join(letters)
    if (word[0] > word[1] > word[2] > word[3] > word[4] > word[5] and
        ((int(word[0]) % 2 == int(word[2]) % 2 == int(word[4]) % 2 == 1 and
         int(word[1]) % 2 == int(word[3]) % 2 == int(word[5]) % 2 == 0) or
        (int(word[0]) % 2 == int(word[2]) % 2 == int(word[4]) % 2 == 0 and
         int(word[1]) % 2 == int(word[3]) % 2 == int(word[5]) % 2 == 1))):
        k += 1
print(k)
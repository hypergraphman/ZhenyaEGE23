s = open('24.txt').read()
s = s.replace('GFE', '.').replace('EGF', '.')
cur_len = 0
max_len = 0
for c in s:
    if c == '.':
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
    else:
        cur_len = 0
print(max_len)
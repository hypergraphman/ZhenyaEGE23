s = open('test.txt').read()

max_len = 0
cur_len = 0
temp = 'EAB'
for c in s:
    if c == temp[cur_len % len(temp)]:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
    elif c == temp[0]:
        cur_len = 1
    else:
        cur_len = 0
print(max_len)
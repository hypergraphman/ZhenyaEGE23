s = open('test.txt').read()
cur_len = 1
max_len = 1
max_chars = []
for i in range(1, len(s)):
    if s[i - 1] == s[i]:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
            max_chars = [s[i]]
        elif cur_len == max_len:
            max_chars.append(s[i])
    else:
        cur_len = 1
print(max_len, max_chars)
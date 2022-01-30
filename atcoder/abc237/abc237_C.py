s = input()
cnt = 0
# 文字列の末尾のaの数
for i in s[::-1]:
    if i != "a":
        break
    cnt += 1
# 文字列の先頭のaの数
for i in s:
    if i != "a":
        break
    cnt -= 1
ans = "a"*cnt+s
if ans == ''.join(reversed(ans)):
    print('Yes')
else:
    print('No')
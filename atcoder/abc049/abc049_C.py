S = input()
x = ["dream","dreamer","erase","eraser"]
S = S[::-1]
for i in range(len(x)):
    x[i] = x[i][::-1]
ansnum = len(S)
i = 0
while i < len(S):
    if S[:5] == "maerd":
        S = S[5:]
        ansnum -= 5
    elif S[:5] == "esare":
        S = S[5:]
        ansnum -= 5
    elif S[:7] == "remaerd":
        S = S[7:]
        ansnum -= 7
    elif S[:6] == "resare":
        S = S[6:]
        ansnum -= 6
    else:
        i += len(S)
if ansnum == 0:
    print("YES")
else:
    print("NO")